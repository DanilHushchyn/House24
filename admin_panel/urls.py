from django.urls import path

import admin_panel.views

urlpatterns = [
    path("statistic", admin_panel.views.statistic, name='statistic'),
    path("paybox", admin_panel.views.paybox, name='paybox'),
    path("receipt", admin_panel.views.receipt, name='receipt'),
    path("personal_account", admin_panel.views.personal_account, name='personal_account'),
    path("flat", admin_panel.views.flat, name='flat'),
    path("client", admin_panel.views.client, name='client'),
    path("house", admin_panel.views.house, name='house'),
    path("message", admin_panel.views.message, name='message'),
    path("application", admin_panel.views.application, name='application'),
    path("indications", admin_panel.views.indications, name='indications'),
    path("system_services", admin_panel.views.system_services, name='system_services'),
    path("system_tarrifs", admin_panel.views.system_tarrifs, name='system_tarrifs'),
    path("system_users", admin_panel.views.system_users, name='system_users'),
    path("system_payment_details", admin_panel.views.system_payment_details, name='system_payment_details'),
    path("system_payment_articles", admin_panel.views.system_payment_articles, name='system_payment_articles'),

    path("main_page", admin_panel.views.main_page, name='main_page'),
    path("about_us", admin_panel.views.about_us, name='about_us'),
    path("services", admin_panel.views.services, name='services'),
    path("tariffs", admin_panel.views.tariffs, name='tariffs'),
    path("contacts", admin_panel.views.contacts, name='contacts'),

]
