from django.shortcuts import render


def customhandler404(request, exception=None):
    response = render(request, 'admin_panel/errors/404.html', )
    response.status_code = 404
    return response


def customhandler500(request, exception=None):
    response = render(request, 'admin_panel/errors/500.html', )
    response.status_code = 500
    return response
