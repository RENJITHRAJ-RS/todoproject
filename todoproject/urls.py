
from django.urls import path, include
from greeting import views
from django.views.generic.base import RedirectView
urlpatterns = [
    path('', views.greeting,name='home'),
    path('about-us', views.aboutUs,name='about'),
    path('page/<str:title>/', views.pages,name='page'),
    path('count/<int:num>/', views.count,name='count'),
    path('contactus/', include('contactus.urls')),
    path('login/', RedirectView.as_view(url='/home/')),
    path('products/',include('products.urls')),
]