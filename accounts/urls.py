from django.urls import path
from accounts import views



urlpatterns = [
    
    path('create/', views.create_account, name='create-account'),
    path('delete/', views.delete_account, name='delete-account'),
    path('details/', views.account_details, name='account-details'),
]
