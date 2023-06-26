from django.urls import path

import admin_panel.views

urlpatterns = [
    path("statistic", admin_panel.views.statistic, name='statistic'),
    path("paybox", admin_panel.views.paybox, name='paybox'),



    path("receipts", admin_panel.views.ReceiptList.as_view(), name='receipts'),
    path("receipt/add", admin_panel.views.CreateReceipt.as_view(), name='add_receipt'),
    path("receipt/update/<str:pk>", admin_panel.views.UpdateReceipt.as_view(), name='update_receipt'),
    path("receipt/copy/<str:pk>", admin_panel.views.CopyReceipt.as_view(), name='copy_receipt'),
    path("receipt/detail/<str:pk>", admin_panel.views.ReceiptDetail.as_view(), name='read_receipt'),
    path("receipt/delete/<str:pk>", admin_panel.views.DeleteReceipt.as_view(), name='delete_receipt'),



    path("personal_accounts", admin_panel.views.PersonalAccountListView.as_view(), name='personal_accounts'),
    path("personal_accounts/add", admin_panel.views.CreatePersonalAccount.as_view(), name='add_personal_account'),
    path("personal_accounts/update/<str:pk>", admin_panel.views.UpdatePersonalAccount.as_view(), name='update_personal_account'),
    path("personal_accounts/detail/<str:pk>", admin_panel.views.PersonalAccountDetail.as_view(), name='read_personal_account'),
    path("personal_accounts/delete/<str:pk>", admin_panel.views.DeletePersonalAccount.as_view(), name='delete_personal_account'),


    path("flats", admin_panel.views.FlatListView.as_view(), name='flats'),
    path("flats/add", admin_panel.views.CreateFlatView.as_view(), name='add_flat'),
    path("flats/update/<str:pk>", admin_panel.views.UpdateFlatView.as_view(), name='update_flat'),
    path("flats/detail/<str:pk>", admin_panel.views.FlatDetail.as_view(), name='read_flat'),
    path("flats/delete/<str:pk>", admin_panel.views.DeleteFlatView.as_view(), name='delete_flat'),


    path("clients", admin_panel.views.ClientListView.as_view(), name='clients'),
    path("clients/add", admin_panel.views.ClientSignUpView.as_view(), name='add_client'),
    path("clients/update/<str:pk>", admin_panel.views.UpdateClientView.as_view(), name='update_client'),
    path("clients/detail/<str:pk>", admin_panel.views.ClientDetail.as_view(), name='read_client'),
    path("clients/delete/<str:pk>", admin_panel.views.DeleteClientView.as_view(), name='delete_client'),


    path("houses", admin_panel.views.HouseListView.as_view(), name='houses'),
    path("houses/add", admin_panel.views.CreateHouseView.as_view(), name='add_house'),
    path("house/update/<str:pk>", admin_panel.views.UpdateHouseView.as_view(), name='update_house'),
    path("house/detail/<str:pk>", admin_panel.views.HouseDetail.as_view(), name='read_house'),

    path("house/delete/<str:pk>", admin_panel.views.DeleteHouseView.as_view(), name='delete_house'),


    path("mailbox", admin_panel.views.MailboxList.as_view(), name='mailboxes'),
    path("mailbox/add", admin_panel.views.CreateMailbox.as_view(), name='add_mailbox'),
    path("mailbox/detail/<str:pk>", admin_panel.views.MailboxDetail.as_view(), name='mailbox_detail'),

    path("mailbox/delete/<str:pk>", admin_panel.views.DeleteMailbox.as_view(),
         name='delete_mailbox'),


    path("applications", admin_panel.views.ApplicationList.as_view(), name='applications'),
    path("application/add", admin_panel.views.CreateApplication.as_view(), name='add_application'),
    path("application/update/<str:pk>", admin_panel.views.UpdateApplication.as_view(),
         name='update_application'),
    path("application/detail/<str:pk>", admin_panel.views.ApplicationDetail.as_view(), name='read_application'),

    path("application/delete/<str:pk>", admin_panel.views.DeleteApplication.as_view(),
         name='delete_application'),

    path("counters", admin_panel.views.CounterList.as_view(), name='counters'),
    path("counter_indications/<str:flat>/<str:service>", admin_panel.views.CounterIndicationsList.as_view(), name='counter_indications'),
    path("indication/add", admin_panel.views.CreateIndication.as_view(), name='add_indication'),
    path("indication/add_new/<str:flat>/<str:service>", admin_panel.views.CreateNewIndication.as_view(), name='add_new_indication'),
    path("indication/update/<str:pk>", admin_panel.views.UpdateIndication.as_view(), name='update_indication'),
    path("indication/detail/<str:pk>", admin_panel.views.IndicationDetail.as_view(), name='read_indication'),
    path("indication/delete/<str:pk>", admin_panel.views.DeleteIndication.as_view(), name='delete_indication'),


    path("system_services", admin_panel.views.ServicesView.as_view(), name='system_services'),
    path("system_tariffs", admin_panel.views.TariffsListView.as_view(), name='system_tariffs'),
    path("system_tariffs/add", admin_panel.views.CreateTariffView.as_view(), name='add_tariff'),
    path("system_tariffs/detail/<str:pk>", admin_panel.views.TariffDetail.as_view(), name='tariff_detail'),
    path("system_tariffs/delete/<str:pk>", admin_panel.views.DeleteTariffView.as_view(), name='delete_tariff'),
    path("system_tariffs/update/<str:pk>", admin_panel.views.UpdateTariffView.as_view(), name='update_tariff'),
    path("system_tariffs/copy/<str:pk>", admin_panel.views.CopyTariffView.as_view(), name='copy_tariff'),
    path("system_payment_details", admin_panel.views.UpdatePaymentDetailView.as_view(), name='system_payment_details'),

    path("personals", admin_panel.views.PersonalListView.as_view(),
         name='personals'),
    path("personals/add", admin_panel.views.PersonalSignUpView.as_view(),
         name='add_personal'),
    path("personals/update/<str:pk>", admin_panel.views.UpdatePersonalView.as_view(),
         name='update_personal'),
    path("personal/detail/<str:pk>", admin_panel.views.PersonalDetail.as_view(), name='read_personal'),

    path("personals/delete/<str:pk>", admin_panel.views.DeletePersonalView.as_view(),
         name='delete_personal'),

    path("system_payment_articles", admin_panel.views.PaymentArticlesListView.as_view(), name='system_payment_articles'),
    path("system_payment_article/add", admin_panel.views.CreatePaymentArticleView.as_view(), name='add_payment_article'),
    path("system_payment_article/update/<str:pk>", admin_panel.views.UpdatePaymentArticleView.as_view(), name='update_payment_article'),
    path("system_payment_article/delete/<str:pk>", admin_panel.views.DeletePaymentArticleView.as_view(), name='delete_payment_article'),

    path("main_page", admin_panel.views.MainPageView.as_view(), name='main_page'),
    path("about_us", admin_panel.views.AboutUsView.as_view(), name='about_us'),
    path("services", admin_panel.views.SiteServicesView.as_view(), name='services'),
    path("tariffs", admin_panel.views.SiteTariffsView.as_view(), name='tariffs'),
    path("contacts", admin_panel.views.ContactsView.as_view(), name='contacts'),


    path("photo/delete/<str:pk>", admin_panel.views.DeletePhotoView.as_view(), name='delete_photo'),
    path("doc/delete/<str:pk>", admin_panel.views.DeleteDocView.as_view(), name='delete_doc'),

    path("get_measure/<str:pk>", admin_panel.views.GetMeasureView.as_view(), name='get_measure'),
    path("get_role/<str:pk>", admin_panel.views.GetRoleView.as_view(), name='get_role'),
    path("get_house-info/<str:pk>", admin_panel.views.GetHouseInfoView.as_view(), name='get_house-info'),
    path("get_flat_owner-info/<str:pk>", admin_panel.views.GetFlatOwnerInfo.as_view(), name='get_flat_owner-info'),
    path("get_section-info/<str:pk>", admin_panel.views.GetSectionInfoView.as_view(), name='get_section-info'),
    path("get_flat-info/<str:pk>", admin_panel.views.GetFlatInfoView.as_view(), name='get_flat-info'),
    path("get_tariff-info/<str:pk>", admin_panel.views.GetTariffInfoView.as_view(), name='get_tariff-info'),
    path("get_all_flats", admin_panel.views.GetAllFlats.as_view(), name='get_all_flats'),
    path("get_service-info/<str:pk>", admin_panel.views.GetServiceInfoView.as_view(), name='get_service-info'),
    path("get_indication-info/<str:flat_id>/<str:service_id>", admin_panel.views.GetIndicationInfoView.as_view(), name='get_indication-info'),
    path("get_indication-sorted-list/<str:flat_id>", admin_panel.views.GetIndicationsSortedList.as_view(), name='get_indication-sorted-list'),
]
