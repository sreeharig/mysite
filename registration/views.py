from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.views.generic.edit import FormView, UpdateView
from django.core.urlresolvers import reverse_lazy
from registration.forms import *

class Home(TemplateView):
    template_name = "index.html"

class UserRegistrationView(AnonymousRequiredMixin, FormView):
    template_name = "register_user.html"
    form_class = UserRegistrationForm
    success_url = 'user/success/'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)


class AddChocolateView(FormView):
   template_name="add_chocolate.html"
   form_class= ChocolateAddForm
   success_url = '/registration/user/success/'

   def form_valid(self, form):
       form.save()
       return FormView.form_valid(self, form)