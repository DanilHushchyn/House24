from django.urls import path

import cabinet.views

urlpatterns = [
    path("statistic", cabinet.views.statistic, name='cabinet_statistic'),

    path("applications", cabinet.views.ApplicationList.as_view(), name='applications_cabinet'),
    path("application/add", cabinet.views.CreateApplication.as_view(), name='add_application_cabinet'),


    path("profile", cabinet.views.Profile.as_view(), name='profile'),
    path("profile/update/<str:pk>", cabinet.views.UpdateProfileView.as_view(), name='update_profile'),

    path("mailbox", cabinet.views.MailboxList.as_view(), name='mailboxes_cabinet'),
    path("filtered_messages", cabinet.views.MailboxFilteredList.as_view(),
         name='filtered_messages_cabinet'),
    path("mailbox/detail/<str:pk>", cabinet.views.MailboxDetail.as_view(), name='mailbox_detail_cabinet'),
    path("mailbox/delete/<str:pk>", cabinet.views.DeleteMailbox.as_view(),
         name='delete_mailbox_cabinet'),

    path("tariff/detail/<str:flat_id>", cabinet.views.TariffDetail.as_view(), name='get_tariff'),

]
