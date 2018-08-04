import requests

from django.db.models import get_model

from easyrec.errors import EasyRecException


Product = get_model('catalogue', 'Product')


class EasyRec():

    _base_url = "api/1.0/json/"
    _default_item_type = 'ITEM'

    def __init__(self, endpoint, tenant, api_key):
        if not endpoint.startswith('http'):
            raise RuntimeError("EASYREC_ENDPOINT should include the http")
        if endpoint.endswith("/"):
            endpoint = endpoint[:-1]
        self._endpoint = "/".join((endpoint, self._base_url))
        self._tenant = tenant
        self._api_key = api_key
        self._requests = requests
        self.initialised = False

    def get_item_types(self):
        if hasattr(self, "_item_types"):
            return self._item_types
        url = self._build_url('itemtypes')
        options = {
            'apikey': self._api_key,
            'tenantid': self._tenant
        }
        try:
            response = self._fetch_response(url, params=options)
        except:
            return ['ITEM',]
        try:
            return response['itemTypes']['itemType']
        except KeyError:
            return ['ITEM',]

    def _get_item_type(self, item_type):
        item_type = item_type.upper()
        if item_type in self.get_item_types():
            return item_type
        return self._default_item_type

    def add_view(self, session_id, item_id, item_desc, item_url,
                 item_type='ITEM', user_id=None, image_url=None,
                 action_time=None):
        options = {
            'apikey': self._api_key,
            'tenantid': self._tenant,
            'sessionid': session_id,
            'itemid': item_id,
            'itemdescription': item_desc,
            'itemurl': item_url,
            'itemtype': self._get_item_type(item_type)
        }
        if user_id:
            options['userid'] = user_id

        if image_url:
            options['imageurl'] = image_url

        if action_time:
            options['actiontime'] = action_time.strftime("%d_%m_%Y_%H_%M_%S")

        url = self._build_url('view')
        return self._fetch_response(url, params=options)

    def add_buy(self, session_id, item_id, item_desc, item_url,
                item_type='ITEM', user_id=None, image_url=None,
                action_time=None):
        options = {
            'apikey': self._api_key,
            'tenantid': self._tenant,
            'sessionid': session_id,
            'itemid': item_id,
            'itemdescription': item_desc,
            'itemurl': item_url,
            'itemtype': self._get_item_type(item_type)
        }
        if user_id:
            options['userid'] = user_id

        if image_url:
            options['imageurl'] = image_url

        if action_time:
            options['actiontime'] = action_time.strftime("%d_%m_%Y_%H_%M_%S")

        url = self._build_url('buy')
        return self._fetch_response(url, params=options)

    def add_rating(self, session_id, item_id, item_desc, item_url, rating,
                   item_type='ITEM',  user_id=None, image_url=None,
                   action_time=None):
        options = {
            'apikey': self._api_key,
            'tenantid': self._tenant,
            'sessionid': session_id,
            'itemid': item_id,
            'itemdescription': item_desc,
            'itemurl': item_url,
            'itemtype': self._get_item_type(item_type),
            'ratingvalue': rating,
        }
        if user_id:
            options['userid'] = user_id

        if image_url:
            options['imageurl'] = image_url

        if action_time:
            options['actiontime'] = action_time.strftime("%d_%m_%Y_%H_%M_%S")

        url = self._build_url('rate')
        return self._fetch_response(url, params=options)

    def add_action(self, session_id, item_id, item_desc, item_url, action,
                   value=None, item_type='ITEM',  user_id=None, image_url=None,
                   action_time=None):
        options = {
            'apikey': self._api_key,
            'tenantid': self._tenant,
            'sessionid': session_id,
            'itemid': item_id,
            'itemdescription': item_desc,
            'itemurl': item_url,
            'itemtype': self._get_item_type(item_type),
            'actiontype': action,
        }

        if value:
            options['actionvalue'] = value

        if user_id:
            options['userid'] = user_id

        if image_url:
            options['imageurl'] = image_url

        if action_time:
            # dd_MM_yyyy_HH_mm_ss
            options['actiontime'] = action_time.strftime("%d_%m_%Y_%H_%M_%S")

        url = self._build_url('rate')
        return self._fetch_response(url, params=options)

    def get_user_recommendations(self, user_id, max_results=None,
        requested_item_type=None, action_type=None):
        options = {
            'apikey': self._api_key,
            'tenantid': self._tenant,
            'userid': user_id
        }

        if max_results:
            options['numberOfResults'] = max_results

        if requested_item_type:
            options['requesteditemtype'] = self._get_item_type(requested_item_type)

        if action_type:
            options['actiontype'] = action_type

        url = self._build_url('recommendationsforuser')
        recommendations = self._fetch_response(url, params=options)
        return self._recommendations_to_products(recommendations)

    def get_other_users_also_bought(self, item_id, user_id=None,
        max_results=None, item_type=None, requested_item_type=None):
        kwargs = {
            'item_id': item_id,
            'user_id': user_id,
            'max_results': max_results,
            'item_type': item_type,
            'requested_item_type': requested_item_type
        }
        return self._get_item_based_recommendation('otherusersalsobought',
            **kwargs)

    def get_other_users_also_viewed(self, item_id, user_id=None,
        max_results=None, item_type=None, requested_item_type=None):
        kwargs = {
            'item_id': item_id,
            'user_id': user_id,
            'max_results': max_results,
            'item_type': item_type,
            'requested_item_type': requested_item_type
        }
        return self._get_item_based_recommendation('otherusersalsoviewed',
            **kwargs)

    def get_items_rated_as_good_by_other_users(self, item_id, user_id=None,
        max_results=None, item_type=None, requested_item_type=None):
        kwargs = {
            'item_id': item_id,
            'user_id': user_id,
            'max_results': max_results,
            'item_type': item_type,
            'requested_item_type': requested_item_type
        }
        return self._get_item_based_recommendation('itemsratedgoodbyotherusers',
            **kwargs)


    def get_related_items(self, item_id, max_results=None, assoc_type=None,
                                    requested_item_type=None):
        kwargs = {
            'item_id': item_id,
            'max_results': max_results,
            'assoc_type': assoc_type,
            'requested_item_type': requested_item_type
        }
        return self._get_item_based_recommendation('relateditems', **kwargs)

    def _recommendations_to_products(self, recommendations):
        upcs = []
        if ('recommendeditems' not in recommendations
            or 'item' not in recommendations['recommendeditems']):
            return Product.browsable.none()

        for item in recommendations['recommendeditems']['item']:
            upcs.append(item['id'])

        return Product.browsable.filter(upc__in=upcs)

    def _get_item_based_recommendation(self, recommendation_type, **kwargs):
        options = {
            'apikey': self._api_key,
            'tenantid': self._tenant,
            'itemid': kwargs['item_id'],
        }

        if kwargs.get('user_id'):
            options['userid'] = kwargs['user_id']

        if kwargs.get('max_results'):
            options['numberOfResults'] = kwargs['max_results']

        if kwargs.get('item_type'):
            options['itemtype'] = self._get_item_type(kwargs['item_type'])

        if kwargs.get('requested_item_type'):
            options['requesteditemtype'] = self._get_item_type(
                kwargs['requested_item_type']
            )

        if kwargs.get('assoc_type'):
            options['assoctype'] = kwargs['assoc_type']

        url = self._build_url(recommendation_type)
        recommendations = self._fetch_response(url, params=options)
        return self._recommendations_to_products(recommendations)

    def _build_url(self, path):
        if path.startswith('/'):
            path = path[1:]
        if path.endswith('/'):
            path = path[:-1]
        url = "%s%s" % (self._endpoint, path)
        return url

    def _fetch_response(self, url, method="GET", params=None):
        func = {
            'GET': self._requests.get,
            'POST': self._requests.post
        }.get(method, self._requests.get)
        response = func(url, params=params)
        response.raise_for_status()
        content = response.json()
        self.check_response_for_errors(content)
        return content

    def check_response_for_errors(self, json):
        if json.get('error', False):
            raise EasyRecException(json['error'])


class DummyResponse(object):

    def __init__(self, response={}):
        self.response = response

    def json(self):
        return self.response

    def raise_for_status(self):
        pass


class DummyRequests(object):
    """
        Replaces requests if in dummy mode
    """
    def __init__(self, response={}):
        self.response = response

    def get(self, *args, **kwargs):
        return DummyResponse(self.response)

    def post(self, *args, **kwargs):
        return DummyResponse(self.response)
