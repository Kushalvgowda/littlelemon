from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/', views.MenuItemViews.as_view(), name='menu-list'),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('booking/', views.BookingViews.as_view(), name='booking-list'),
    path('booking/<int:pk>', views.SingleBookingView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('page/', views.page, name='page'),
]
