from django.urls import path
from .views import (
    UploadView,
    DisketDetailView,
    HomeView,
    DisketShelfView,
    DisketUpdateView,
)

urlpatterns = [
    path("upload/", UploadView.as_view(), name="upload_disket"),
    path(
        "disket/<slug:slug>/", DisketDetailView.as_view(), name="disket_detail"
    ),
    path(
        "disket/<slug:slug>/update/",
        DisketUpdateView.as_view(),
        name="disket_edit",
    ),
    path("shelf/<str:shelf>/", DisketShelfView.as_view(), name="shelf"),
    path("", HomeView.as_view(), name="homepage"),
]
