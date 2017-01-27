from django.contrib.auth.mixins import LoginRequiredMixin #TODO
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.forms.utils import ErrorList
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import get_template
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



from .forms import ContactForm
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
    #success_url = reverse_lazy('contacts')

def home_page_view(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_message = form.cleaned_data['contact_message']

            template = get_template('contact_template.txt')

            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_message': contact_message,
                })
            content = template.render(context)

            email = EmailMessage('New contact form submission',
                                    content,
                                    'Your website <hello@toddkovalsky.com>',
                                    ['youremail@gmail.com'],
                                    headers = {'Reply-To': contact_email },
                                    )
            email.send()
            return redirect('home')

    return render(request, 'home.html', { 'form': form_class, })
