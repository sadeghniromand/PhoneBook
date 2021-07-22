from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'phone', views.PhoneViewSet)
user_list = views.ReadPhoneViewSet.as_view({'get': 'list'})
app_name = 'phones'
urlpatterns = [
    path('creat-phone/', views.CreatPhoneNumber.as_view(), name='creat-phone'),
    path('search-phone/', views.SearchPhoneNumber.as_view(), name='search-phone'),
    path('phone-book',views.ListPhoneBookView.as_view(),name='phone-book'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('read/', user_list, name='read'),
]
