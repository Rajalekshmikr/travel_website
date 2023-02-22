from django.urls import path
from . import views
urlpatterns=[
    path('home',views.demo,name='demo'),
    # path('about',views.about,name='about'),
    # path('contact',views.contact,name='contact'),
    # path('details',views.details,name='details'),
    #path('thanx',views.thanx,name='tahnx')

]