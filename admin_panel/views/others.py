from django.shortcuts import render


def statistic(request):
    return render(request, 'admin_panel/statistic.html')


def paybox(request):
    return render(request, 'admin_panel/paybox.html')


def receipt(request):
    return render(request, 'admin_panel/receipt.html')


def personal_account(request):
    return render(request, 'admin_panel/personal_account.html')


def flat(request):
    return render(request, 'admin_panel/flat.html')


def client(request):
    return render(request, 'admin_panel/clients.html')


def house(request):
    return render(request, 'admin_panel/house.html')


def message(request):
    return render(request, 'admin_panel/message.html')


def application(request):
    return render(request, 'admin_panel/application.html')


def indications(request):
    return render(request, 'admin_panel/indications.html')


def system_services(request):
    return render(request, 'admin_panel/system_settings/services.html')


def system_tarrifs(request):
    return render(request, 'admin_panel/system_settings/tariffs.html')


def system_users(request):
    return render(request, 'admin_panel/system_settings/users.html')


def system_payment_details(request):
    return render(request, 'admin_panel/system_settings/payment_details.html')


def system_payment_articles(request):
    return render(request, 'admin_panel/system_settings/payment_articles.html')

