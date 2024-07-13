from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    
    path('accounts/', views.AccountListView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', views.AccountDetailView.as_view(), name='account-detail'),
    path('accounts/create/', views.AccountCreateView.as_view(), name='account-create'),
    path('accounts/<int:pk>/update/', views.AccountUpdateView.as_view(), name='account-update'),
    path('accounts/<int:pk>/delete/', views.AccountDeleteView.as_view(), name='account-delete'),
    path('destinations/', views.DestinationListView.as_view(), name='destination-list'),
    
    path('destinations/<int:pk>/', views.DestinationDetailView.as_view(), name='destination-detail'),
    path('destinations/create/', views.DestinationCreateView.as_view(), name='destination-create'),
    path('destinations/<int:pk>/update/', views.DestinationUpdateView.as_view(), name='destination-update'),
    path('destinations/<int:pk>/delete/', views.DestinationDeleteView.as_view(), name='destination-delete'),
    
    path('api/account/<int:account_id>/destinations/', views.get_account_destinations, name='account-destinations'),
    path('server/incoming_data', views.incoming_data, name='incoming_data'),
]