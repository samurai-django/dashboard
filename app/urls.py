from django.urls import path
from .views import DashboardTemplateView

app_name = 'app'

urlpatterns = [
    path('', DashboardTemplateView.as_view(), name='dashboard'),

]