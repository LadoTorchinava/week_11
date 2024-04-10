from django.urls import path
from .views import contact, submit_form, another_page


urlpatterns = [
    path('', contact, name = 'contact_page'),
    path('submit/', submit_form, name='submit_form'),
    path('another_page/', another_page, name='another_page'),
 
]