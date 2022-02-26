from django.urls import path
from .views import favstore_list

urlpatterns = [
  path('report/favstores', favstore_list),
]
