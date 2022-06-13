from django.urls import path



from . import views

urlpatterns = [
    
    path('',views.home, name= 'home'),
    # path('toggle-status/<int:pk>/', toggle_status, name='toggle-status'),
]