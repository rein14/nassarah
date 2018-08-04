from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from shortuuid import get_alphabet

from oscar.core.application import Application

from . import views


class SupportApplication(Application):
    name = 'support'

    ticket_list_view = views.TicketListView
    ticket_create_view = views.TicketCreateView
    ticket_update_view = views.TicketUpdateView

    def get_urls(self):
        urls = [
            url(
                r'accounts/support/$',
                login_required(self.ticket_list_view.as_view()),
                name='customer-ticket-list'
            ),
            url(
                r'accounts/support/ticket/create/$',
                login_required(self.ticket_create_view.as_view()),
                name='customer-ticket-create'
            ),
            url(
                r'accounts/support/ticket/(?P<pk>[{0}]+)/update/$'.format(
                    get_alphabet()
                ),
                login_required(self.ticket_update_view.as_view()),
                name='customer-ticket-update'
            ),
        ]
        return self.post_process_urls(urls)


application = SupportApplication()
