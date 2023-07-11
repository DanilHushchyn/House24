from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *

from admin_panel.forms import ClientUpdateForm, SearchMessageFilterForm
from admin_panel.models import *
from cabinet.forms import CreateApplicationForm


def statistic(request):
    return render(request, 'cabinet/statistic.html')


class Profile(TemplateView):
    template_name = 'cabinet/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flats'] = Flat.objects.filter(flat_owner__user=self.request.user)
        return context


class UpdateProfileView(UpdateView):
    model = CustomUser
    form_class = ClientUpdateForm
    template_name = 'cabinet/update_profile.html'
    success_url = reverse_lazy('profile')
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
        return render(request, 'cabinet/update_profile.html', context=data)


class ApplicationList(ListView):
    template_name = 'cabinet/applications.html'
    context_object_name = 'applications'
    paginate_by = 20

    def get_queryset(self):
        client = self.request.user.client.id
        return Application.objects.filter(flat__flat_owner_id=client)


class CreateApplication(CreateView):
    model = Application
    template_name = 'admin_panel/get_application_form.html'
    form_class = CreateApplicationForm

    def get(self, request, *args, **kwargs):
        form = CreateApplicationForm()
        client = request.user.client
        form.fields["flat"].queryset = Flat.objects.filter(flat_owner_id=client.id)

        data = {
            'form': form,
        }
        return render(request, 'cabinet/get_application_form.html', context=data)

    success_url = reverse_lazy('applications_cabinet')


class MailboxList(ListView):
    template_name = 'cabinet/mailbox.html'
    context_object_name = 'mailboxes'

    def get_queryset(self):
        result = MailBox.objects.filter(flat_owners__user_id=self.request.user.id)
        return result

    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = SearchMessageFilterForm()
        return context


class MailboxFilteredList(ListView):
    template_name = 'cabinet/mailbox.html'
    context_object_name = 'mailboxes'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = SearchMessageFilterForm(initial=self.request.GET)
        return context

    def get_queryset(self):
        search_filter = SearchMessageFilterForm(self.request.GET)
        mailboxes = MailBox.objects.filter(flat_owners__user_id=self.request.user.id)
        qs = []
        if search_filter.is_valid():
            if search_filter.cleaned_data['search_row']:
                qs.append(Q(description__icontains=search_filter.cleaned_data['search_row']))
                qs.append(Q(title__icontains=search_filter.cleaned_data['search_row']))
            q = Q()
            for item in qs:
                q = q | item
            mailboxes = mailboxes.filter(q)
        return mailboxes


class MailboxDetail(DetailView):
    model = MailBox
    template_name = 'cabinet/read_mailbox.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mailbox'] = MailBox.objects.get(pk=self.kwargs['pk'])
        return context


class DeleteMailbox(DeleteView):
    success_url = reverse_lazy('mailboxes_cabinet')

    def post(self, request, pk, *args, **kwargs):
        obj = MailBox.objects.get(pk=pk)
        obj.flat_owners.remove(self.request.user.client)
        obj.save()
        data = {
            'mailboxes': MailBox.objects.all()
        }
        return render(request, 'cabinet/mailbox.html', context=data)


class TariffDetail(TemplateView):
    model = TariffSystem
    template_name = 'cabinet/read_tariff.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flat = Flat.objects.get(pk=self.kwargs['flat_id'])
        context['flat'] = flat

        if flat.tariff:
            context['tariff'] = flat.tariff
            context['tariffservices'] = flat.tariff.tariffservice_set.all()
        else:
            context['tariff'] = None
            context['tariffservices'] = None
        return context