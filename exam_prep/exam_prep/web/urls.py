from django import urls
from django.urls import path
from exam_prep.web import views

urlpatterns = [
    path("", views.home_page, name="home page"),

    path("album/add/", views.album_add, name="add album"),
    path("album/deatils/<int:id>/", views.album_details, name="details album"),
    path("album/edit/<int:id>/", views.album_edit, name="edit album"),
    path("album/delete/<int:id>/", views.album_delete, name="delete album"),

    path("profile/details/", views.profile_details, name="details profile"),
    path("profile/delete", views.profile_delete, name="delete profile"),
]
