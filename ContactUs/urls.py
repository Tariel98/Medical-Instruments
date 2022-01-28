from .views import *
from django.urls import path
urlpatterns = [
    path('', contact_view, name='contact')


]