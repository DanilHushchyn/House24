from django.urls import path

import admin_panel.views

urlpatterns = [
    path("statistic", admin_panel.views.statistic, name='statistic'),
    path("paybox", admin_panel.views.paybox, name='paybox'),
    path("receipt", admin_panel.views.receipt, name='receipt'),


    path("personal_accounts", admin_panel.views.PersonalAccountListView.as_view(), name='personal_accounts'),
    path("personal_accounts/add", admin_panel.views.CreatePersonalAccount.as_view(), name='add_personal_account'),
    path("personal_accounts/update/<str:pk>", admin_panel.views.UpdatePersonalAccount.as_view(), name='update_personal_account'),
    path("personal_accounts/delete/<str:pk>", admin_panel.views.DeletePersonalAccount.as_view(), name='delete_personal_account'),


    path("flats", admin_panel.views.FlatListView.as_view(), name='flats'),
    path("flats/add", admin_panel.views.CreateFlatView.as_view(), name='add_flat'),
    path("flats/update/<str:pk>", admin_panel.views.UpdateFlatView.as_view(), name='update_flat'),
    path("flats/delete/<str:pk>", admin_panel.views.DeleteFlatView.as_view(), name='delete_flat'),


    path("clients", admin_panel.views.ClientListView.as_view(), name='clients'),
    path("clients/add", admin_panel.views.ClientSignUpView.as_view(), name='add_client'),
    path("clients/update/<str:pk>", admin_panel.views.UpdateClientView.as_view(), name='update_client'),
    path("clients/delete/<str:pk>", admin_panel.views.DeleteClientView.as_view(), name='delete_client'),


    path("houses", admin_panel.views.HouseListView.as_view(), name='houses'),
    path("houses/add", admin_panel.views.CreateHouseView.as_view(), name='add_house'),
    path("house/update/<str:pk>", admin_panel.views.UpdateHouseView.as_view(), name='update_house'),
    path("house/delete/<str:pk>", admin_panel.views.DeleteHouseView.as_view(), name='delete_house'),


    path("message", admin_panel.views.message, name='message'),
    path("application", admin_panel.views.application, name='application'),
    path("indications", admin_panel.views.indications, name='indications'),

    path("system_services", admin_panel.views.ServicesView.as_view(), name='system_services'),
    path("system_tariffs", admin_panel.views.TariffsListView.as_view(), name='system_tariffs'),
    path("system_tariffs/add", admin_panel.views.CreateTariffView.as_view(), name='add_tariff'),
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
    path("get_section-info/<str:pk>", admin_panel.views.GetSectionInfoView.as_view(), name='get_section-info'),
    path("get_flat-info/<str:pk>", admin_panel.views.GetFlatInfoView.as_view(), name='get_flat-info'),
]
