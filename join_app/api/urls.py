from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CardList, CategoryViewSet, ContactViewSet, ContactSingleViewSet, ContactViewDetail, CardViewDetail

# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet)
# router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('cards/', CardList.as_view()),
    path('cards/<int:pk>', CardViewDetail.as_view()),
    path('contacts/', ContactViewSet.as_view()),
    path('contacts/<int:pk>', ContactViewDetail.as_view()),
    path('categories/', CategoryViewSet.as_view()),
]
