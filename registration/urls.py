from django.conf.urls import include, url
from registration.views import *
from registration.models import *


urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),

    url(r'^user/success/', TemplateView.as_view(template_name='success.html'),
    name='page'),
    url(r'^chocolate/add/', AddChocolateView.as_view(), name='add_chocolates')
    ]
