from django.urls import path
from . import views




urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('links', views.LinksPage.as_view(), name='links')

]


