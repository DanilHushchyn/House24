from django.shortcuts import render


def main_page(request):
    return render(request, 'admin_panel/manage_site/main_page.html')


def about_us(request):
    return render(request, 'admin_panel/manage_site/about_us.html')


def services(request):
    return render(request, 'admin_panel/manage_site/services.html')


def tariffs(request):
    return render(request, 'admin_panel/manage_site/tariffs.html')


def contacts(request):
    return render(request, 'admin_panel/manage_site/contacts.html')
