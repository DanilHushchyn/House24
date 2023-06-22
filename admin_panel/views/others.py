import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import *

from admin_panel.forms import *
from admin_panel.models import *


def statistic(request):
    return render(request, 'admin_panel/statistic.html')


def paybox(request):
    return render(request, 'admin_panel/paybox.html')


class ReceiptList(ListView):
    template_name = 'admin_panel/receipts.html'
    context_object_name = 'receipts'
    queryset = PersonalAccount.objects.all()


class CreateReceipt(CreateView):
    model = Receipt
    template_name = 'admin_panel/get_receipt_form.html'
    form_class = ReceiptForm
    success_url = reverse_lazy('receipts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['indications'] = Indication.objects.order_by('date_published').all()
        return context


#
# class UpdatePersonalAccount(UpdateView):
#     model = PersonalAccount
#     template_name = 'admin_panel/update_personal_account.html'
#     form_class = PersonalAccountForm
#     success_url = reverse_lazy('personal_accounts')
#
#
# class DeletePersonalAccount(DeleteView):
#     success_url = reverse_lazy('personal_accounts')
#     queryset = PersonalAccount.objects.all()


class FlatListView(ListView):
    template_name = 'admin_panel/flats.html'
    context_object_name = 'flats'
    queryset = Flat.objects.all()


class CreateFlatView(CreateView):
    model = Flat
    template_name = 'admin_panel/get_flat_form.html'
    form_class = FlatForm
    success_url = reverse_lazy('flats')


class UpdateFlatView(UpdateView):
    model = Flat
    template_name = 'admin_panel/update_flat.html'
    form_class = FlatForm
    success_url = reverse_lazy('flats')


class DeleteFlatView(DeleteView):
    success_url = reverse_lazy('flats')
    queryset = Flat.objects.all()


class PersonalAccountListView(ListView):
    template_name = 'admin_panel/personal_accounts.html'
    context_object_name = 'personal_accounts'
    queryset = PersonalAccount.objects.all()


class CreatePersonalAccount(CreateView):
    model = PersonalAccount
    template_name = 'admin_panel/get_personal_account_form.html'
    form_class = PersonalAccountForm
    success_url = reverse_lazy('personal_accounts')


class UpdatePersonalAccount(UpdateView):
    model = PersonalAccount
    template_name = 'admin_panel/update_personal_account.html'
    form_class = PersonalAccountForm
    success_url = reverse_lazy('personal_accounts')


class DeletePersonalAccount(DeleteView):
    success_url = reverse_lazy('personal_accounts')
    queryset = PersonalAccount.objects.all()


class ClientListView(ListView):
    template_name = 'admin_panel/clients.html'
    context_object_name = 'clients'
    queryset = FlatOwner.objects.all()


class ClientSignUpView(CreateView):
    model = CustomUser
    form_class = ClientSignUpForm
    template_name = 'admin_panel/get_client_form.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return redirect('clients')


class UpdateClientView(UpdateView):
    model = CustomUser
    form_class = ClientUpdateForm
    template_name = 'admin_panel/update_client.html'
    success_url = reverse_lazy('clients')
    queryset = CustomUser.objects.all()

    def get(self, request, pk, *args, **kwargs):
        user = CustomUser.objects.get(pk=pk)
        owner = FlatOwner.objects.get(user=user)
        form = ClientUpdateForm(instance=user,
                                initial={'birthday': owner.birthday, 'viber': owner.viber, 'telegram': owner.telegram,
                                         'patronymic': owner.patronymic, 'ID': owner.ID,
                                         'bio': owner.bio, })
        data = {
            'form': form,
        }
        return render(request, 'admin_panel/update_client.html', context=data)


class DeleteClientView(DeleteView):
    success_url = reverse_lazy('clients')
    queryset = CustomUser.objects.all()


class HouseListView(ListView):
    template_name = 'admin_panel/houses.html'
    context_object_name = 'houses'
    queryset = House.objects.all()


class HouseDetail(DetailView):
    model = House
    template_name = 'admin_panel/read_house.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        house = House.objects.prefetch_related('gallery__photo_set','houseuser_set').get(pk=self.kwargs['pk'])
        photos = house.gallery.photo_set.all()
        users = house.houseuser_set.all()
        context['house'] = house
        context['photos'] = photos
        context['users'] = users

        return context


class CreateHouseView(FormView):
    def get(self, request, *args, **kwargs):
        house_form = HouseForm()
        personals = Personal.objects.all()
        photo_formset = HousePhotoFormset(queryset=Photo.objects.none(), prefix='gallery')
        section_formset = SectionFormset(queryset=Section.objects.none(), prefix='section')
        floor_formset = FloorFormset(queryset=Floor.objects.none(), prefix='floor')
        house_user_formset = HouseUserFormset(queryset=HouseUser.objects.none(), prefix='personal')
        data = {
            'house_form': house_form,
            'personals': personals,
            'photo_formset': photo_formset,
            'section_formset': section_formset,
            'floor_formset': floor_formset,
            'house_user_formset': house_user_formset,
        }
        return render(request, 'admin_panel/get_house_form.html', context=data)

    def post(self, request, *args, **kwargs):

        house_form = HouseForm(request.POST, request.FILES)
        section_formset = SectionFormset(request.POST, request.FILES, prefix='section')
        floor_formset = FloorFormset(request.POST, request.FILES, prefix='floor')
        photo_formset = HousePhotoFormset(request.POST, request.FILES, prefix='gallery')
        house_user_formset = HouseUserFormset(request.POST, request.FILES, prefix='personal')

        if section_formset.is_valid() and floor_formset.is_valid() and house_form.is_valid() and photo_formset.is_valid() and house_user_formset.is_valid():
            house_obj = house_form.save()
            house_user_instances = house_user_formset.save(commit=False)
            for instance in house_user_instances:
                instance.house_id = house_obj.id
                instance.save()
            gallery = Gallery.objects.create()
            house_obj.gallery_id = gallery.id
            for photo_form in photo_formset:
                instance = photo_form.save(commit=False)
                instance.gallery_id = gallery.id
                instance.save()
            section_instances = section_formset.save(commit=False)
            floor_instances = floor_formset.save(commit=False)
            for instance in section_instances:
                instance.house_id = house_obj.id

                instance.save()
            for instance in floor_instances:
                instance.house_id = house_obj.id
                instance.save()
            house_obj.save()

        else:
            data = {
                'house_form': house_form,
                'section_formset': section_formset,
                'floor_formset': floor_formset,
                'photo_formset': photo_formset,
                'house_user_formset': house_user_formset,
            }
            return render(request, 'admin_panel/get_house_form.html', context=data)
        return redirect('houses')


class UpdateHouseView(FormView):
    def get(self, request, pk, *args, **kwargs):
        personals = Personal.objects.all()
        house = House.objects.get(pk=pk)
        house_form = HouseForm(instance=house)
        photo_formset = PhotoFormset(queryset=Photo.objects.filter(gallery_id=house.gallery_id), prefix='gallery')
        section_formset = SectionFormset(queryset=Section.objects.filter(house=house), prefix='section')
        floor_formset = FloorFormset(queryset=Floor.objects.filter(house=house), prefix='floor')
        house_user_formset = HouseUserFormset(queryset=HouseUser.objects.filter(house_id=house.id), prefix='personal')
        data = {
            'house_form': house_form,
            'personals': personals,
            'house': house,
            'photo_formset': photo_formset,
            'section_formset': section_formset,
            'floor_formset': floor_formset,
            'house_user_formset': house_user_formset,
        }
        return render(request, 'admin_panel/update_house.html', context=data)

    def post(self, request, pk, *args, **kwargs):
        house = House.objects.get(pk=pk)
        house_form = HouseForm(request.POST, request.FILES, instance=house)
        section_formset = SectionFormset(request.POST, request.FILES, prefix='section')
        floor_formset = FloorFormset(request.POST, request.FILES, prefix='floor')
        photo_formset = PhotoFormset(request.POST, request.FILES, prefix='gallery')
        house_user_formset = HouseUserFormset(request.POST, request.FILES, prefix='personal')

        if section_formset.is_valid() and floor_formset.is_valid() and house_form.is_valid() and photo_formset.is_valid() and house_user_formset.is_valid():
            house_obj = house_form.save()
            house_user_instances = house_user_formset.save(commit=False)
            for instance in house_user_instances:
                instance.house_id = house_obj.id
                instance.save()
            photo_instances = photo_formset.save(commit=False)
            gallery = Gallery.objects.get(house=house)
            for photo_instance in photo_instances:
                photo_instance.gallery_id = gallery.id
                photo_instance.save()

            section_instances = section_formset.save(commit=False)
            floor_instances = floor_formset.save(commit=False)
            for instance in section_instances:
                instance.house_id = house_obj.id
                instance.save()
            for instance in floor_instances:
                instance.house_id = house_obj.id
                instance.save()
            house_obj.save()

        else:
            data = {
                'house_form': house_form,
                'section_formset': section_formset,
                'floor_formset': floor_formset,
                'photo_formset': photo_formset,
                'house_user_formset': house_user_formset,
            }
            return render(request, 'admin_panel/get_house_form.html', context=data)
        return redirect('houses')


class GetRoleView(View):
    def get(self, request, pk):
        personal = Personal.objects.get(pk=pk)
        data = {
            'role': personal.get_role_display(),
        }

        return HttpResponse(json.dumps(data), content_type='application/json')


class GetSectionInfoView(View):
    def get(self, request, pk):
        section = Section.objects.prefetch_related('flat_set').get(pk=pk)
        flats = serializers.serialize('json', section.flat_set.all())
        data = {
            "flats": flats,
        }
        return JsonResponse(data, safe=False)


class GetFlatInfoView(View):
    def get(self, request, pk):
        flat = Flat.objects.get(pk=pk)
        flat_owner = FlatOwner.objects.get(flat=flat)
        user = CustomUser.objects.get(flatowner=flat_owner)
        flat_owner = serializers.serialize('json', [flat_owner])
        user = serializers.serialize('json', [user])
        data = {
            "flat_owner": flat_owner,
            "user": user,
        }
        return JsonResponse(data, safe=False)


class GetHouseInfoView(View):
    def get(self, request, pk):
        house = House.objects.prefetch_related('section_set', 'floor_set', 'flat_set').get(pk=pk)
        sections = serializers.serialize('json', house.section_set.all())
        floors = serializers.serialize('json', house.floor_set.all())
        flats = serializers.serialize('json', house.flat_set.all())
        house = serializers.serialize('json', [house])
        data = {
            "house": house,
            "sections": sections,
            "floors": floors,
            "flats": flats,
        }
        return JsonResponse(data, safe=False)


class GetFlatOwnerInfo(View):
    def get(self, request, pk):
        flat_owner = FlatOwner.objects.prefetch_related('flat_set').get(pk=pk)
        flats = serializers.serialize('json', flat_owner.flat_set.select_related('house').all())

        data = {
            "flats": flats,
        }
        return JsonResponse(data, safe=False)


class GetAllFlats(View):
    def get(self, request):
        flats = Flat.objects.all()
        flats = serializers.serialize('json', flats)

        data = {
            "flats": flats,
        }
        return JsonResponse(data, safe=False)


class DeleteHouseView(DeleteView):
    def post(self, request, pk, *args, **kwargs):
        house = House.objects.get(pk=pk)
        gallery = Gallery.objects.get(pk=house.gallery_id)
        house.delete()
        gallery.delete()
        return redirect('houses')


class MailboxList(ListView):
    template_name = 'admin_panel/mailbox.html'
    context_object_name = 'mailboxes'
    queryset = MailBox.objects.all()


class CreateMailbox(CreateView):
    model = MailBox
    template_name = 'admin_panel/get_mailbox_form.html'
    form_class = MailBoxForm
    success_url = reverse_lazy('mailboxes')


class MailboxDetail(DetailView):
    model = MailBox
    template_name = 'admin_panel/read_mailbox.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mailbox'] = MailBox.objects.get(pk=self.kwargs['pk'])
        return context


class DeleteMailbox(DeleteView):
    success_url = reverse_lazy('mailboxes')
    queryset = MailBox.objects.all()


class ApplicationList(ListView):
    template_name = 'admin_panel/applications.html'
    context_object_name = 'applications'
    queryset = Application.objects.all()


class ApplicationDetail(DetailView):
    model = Application
    template_name = 'admin_panel/read_application.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        application = Application.objects.get(pk=self.kwargs['pk'])
        context['application'] = application
        return context


class CreateApplication(CreateView):
    model = Application
    template_name = 'admin_panel/get_application_form.html'
    form_class = CreateApplicationForm
    success_url = reverse_lazy('applications')


class UpdateApplication(UpdateView):
    model = Application
    template_name = 'admin_panel/update_application.html'
    form_class = ApplicationForm
    success_url = reverse_lazy('applications')


class DeleteApplication(DeleteView):
    success_url = reverse_lazy('applications')
    queryset = Application.objects.all()


class CounterList(ListView):
    template_name = 'admin_panel/counters.html'
    context_object_name = 'indications'
    queryset = Indication.objects.order_by('flat', 'service', '-date_published').distinct('flat', 'service')


class CounterIndicationsList(ListView):
    template_name = 'admin_panel/counter_indications_list.html'
    context_object_name = 'indications'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flat'] = Flat.objects.get(pk=self.kwargs['flat'])
        context['service'] = Service.objects.get(pk=self.kwargs['service'])
        return context

    def get_queryset(self):
        queryset = Indication.objects.filter(flat_id=self.kwargs['flat'], service_id=self.kwargs['service'])
        return queryset


class IndicationDetail(DetailView):
    model = Indication
    template_name = 'admin_panel/read_indication.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        indication = Indication.objects.get(pk=self.kwargs['pk'])
        context['indication'] = indication
        return context


class CreateIndication(CreateView):
    model = Indication
    template_name = 'admin_panel/get_indication_form.html'
    form_class = IndicationForm
    success_url = reverse_lazy('counters')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_new_indication'] = False
        return context

    def post(self, request, *args, **kwargs):
        indication_form = IndicationForm(request.POST)
        if indication_form.is_valid():
            obj = indication_form.save()
            if request.POST['action'] == 'save_and_new':
                indication_form = IndicationForm(initial={'indication_val': obj.indication_val, 'service': obj.service})
                data = {
                    'form': indication_form
                }
                return render(request, 'admin_panel/get_indication_form.html', context=data)
            else:
                return redirect('counters')
        else:
            data = {
                'form': indication_form
            }
            return render(request, 'admin_panel/get_indication_form.html', context=data)


class CreateNewIndication(CreateView):
    model = Indication
    template_name = 'admin_panel/get_indication_form.html'
    form_class = IndicationForm

    def get_success_url(self):
        category = self.kwargs['category']  # Retrieve the category value from the URL
        return '/category/{}/'.format(category)  # Build the URL using the retrieved value

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_new_indication'] = True
        return context

    def get_initial(self):
        initial = super().get_initial()
        flat = Flat.objects.get(pk=self.kwargs['flat'])
        service = Service.objects.get(pk=self.kwargs['service'])
        initial['house'] = flat.house
        initial['section'] = flat.section
        initial['flat'] = flat
        initial['service'] = service
        return initial

    def post(self, request, *args, **kwargs):
        form = IndicationForm(request.POST)
        if form.is_valid():
            obj = form.save()
            if request.POST['action'] == 'save_and_new':
                indication_form = IndicationForm(initial={'indication_val': obj.indication_val, 'service': obj.service})
                data = {
                    'form': indication_form
                }
                return render(request, 'admin_panel/get_indication_form.html', context=data)
            else:
                url = reverse('counter_indications', args=[obj.flat.id, obj.service.id])
                return redirect(url)
        else:
            data = {
                'form': form,
                'create_new_indication': True,
            }
            return render(request, 'admin_panel/get_indication_form.html', context=data)


class UpdateIndication(UpdateView):
    model = Indication
    template_name = 'admin_panel/update_indication.html'
    form_class = IndicationForm
    success_url = reverse_lazy('counters')

    def get(self, request, pk, *args, **kwargs):
        obj = Indication.objects.get(pk=pk)
        form = IndicationForm(instance=obj, initial={'house': obj.flat.house, 'section': obj.flat.section, })
        data = {
            'form': form,
        }
        return render(request, 'admin_panel/update_indication.html', context=data)


class DeleteIndication(DeleteView):
    success_url = reverse_lazy('counters')
    queryset = Indication.objects.all()
