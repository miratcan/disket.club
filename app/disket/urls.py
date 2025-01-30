from django.urls import path
from .views import DisketUploadView, DisketDetailView, HomeView

urlpatterns = [
    path('upload/', DisketUploadView.as_view(), name='upload_disket'),
    path('disket/<slug:slug>/', DisketDetailView.as_view(), name='disket_detail'),
    path('', HomeView.as_view(), name='homepage'),
] 