from django.contrib.auth.mixins import LoginRequiredMixin #TODO
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.forms.utils import ErrorList
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


#from .forms import UserCreationForm, UserLoginForm
from .models import Contact



# Create your views here.

class ContactsListView(ListView):
    model = Contact

    def get_context_data(self, *args, **kwargs):
        context = super(ContactsListView, self).get_context_data(*args, **kwargs)

class ContactDetailView(DetailView):
    model = Contact

class ContactCreateView(CreateView):
    #can use fields or form_class
    #form_class = AddSaleForm
    model = Contact
    fields = '__all__'

class ContactUpdateView(UpdateView):
    model = Contact
    fields = '__all__'

class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts')

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context
