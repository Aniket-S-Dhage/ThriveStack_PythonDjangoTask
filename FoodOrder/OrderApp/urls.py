from django.urls import path
from .views import ListOrdersView, AddOrderView

urlpatterns = [
    path('showlist/', ListOrdersView.as_view()),
    path('', ListOrdersView.as_view()),
    path('register/', AddOrderView.as_view()),
]