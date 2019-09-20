from django.urls import path
from userApp.views import home_view
from .import views


urlpatterns = [
   path('', home_view, name="base-view"),
   path('verify/<str:token>/<int:user_id>/', views.verify_view, name='verify_view'),
   path('about/', views.about_view, name='about-view'),
   path('contact/', views.contact_view, name='contact-view'),
   path('explore/', views.explore_view, name='explore-view'),
   path('input/', views.input, name='input_view'),
   path('fag/', views.fag_view, name='page-fag')


]