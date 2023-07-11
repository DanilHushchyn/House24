from admin_panel.models import Flat


def flats(request):
    return {'flats': Flat.objects.filter(flat_owner_id=request.user.client.id)}