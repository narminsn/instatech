from django.urls import path
from . import views

urlpatterns = [
    path('',views.profile_view, name='profile'),
    path('settings/', views.settings_view, name="settings-view"),
    path('logout/', views.logout_view, name='logout'),
    path('shotadd/', views.shotadd_view, name='shotadd'),
    path('add/shot/', views.shot_add, name='imageadd'),
    path('deleteshot/', views.shotdelete_view, name='picture-delete'),
    path('form', views.form_view, name='form'),
    path('modal<int:id>/', views.postmodal_view, name='modal'),
    path('explore-page/',views.explore_people, name='explorepage'),
    path('followers/', views.user_followers, name='user-followers'),
    path('following/', views.user_following, name='user-following'),
    path('social_settings/', views.social_settings,name='social_settings'),

]