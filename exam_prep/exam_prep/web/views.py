from django.shortcuts import render, redirect
from exam_prep.web.models import Profile, Album
from exam_prep.web.forms import *


def home_page(request):
    albums = Album.objects.all()
    form = ProfileCreateModelForm()
    profile = Profile.objects.first()

    if request.method == "POST":
        form = ProfileCreateModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path_info)  # reload page

    context = {"profile": profile, "albums": albums, "form": form}

    if profile:
        return render(request, "profiles/home-with-profile.html", context)

    else:
        return render(request, "profiles/home-no-profile.html", context)


def album_add(request):
    form = AlbumAddModelForm()
    profile = Profile.objects.first()

    if request.method == "POST":
        form = AlbumAddModelForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)  # new
            album.profile = profile  # new
            form.save()  # new

            return redirect("home page")

    context = {"form": form, "profile": profile}

    return render(request, "albums/add-album.html", context)


def album_details(request, id):
    album = Album.objects.filter(id=id).first()

    context = {
        "album": album
    }

    return render(request, "albums/album-details.html", context)


def album_edit(request, id):
    album = Album.objects.filter(id=id).first()
    form = AlbumEditModelForm(instance=album)

    if request.method == "POST":
        form = AlbumAddModelForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        "form": form,
        "album": album
    }

    return render(request, "albums/edit-album.html", context)


def album_delete(request, id):

    album = Album.objects.filter(id=id).first()
    form = AlbumDeleteModelForm(instance=album)

    if request.method == "POST":
        form = AlbumAddModelForm(request.POST, instance=album)
        if form.is_valid():

            album.delete()
            return redirect('home page')

    context = {
        "form": form,
        "album": album
    }

    return render(request, "albums/delete-album.html", context)


def profile_details(request):
    form = ProfileDetailsModelForm()
    profile = Profile.objects.all().first()
    albums = Album.objects.filter(profile_id=profile.pk)
    albums_len = len(albums)

    context = {
        "form": form,
        "profile": profile,
        "albums_len": albums_len
    }

    return render(request, "profiles/profile-details.html", context)


def profile_delete(request):
    profile = Profile.objects.all().first()

    if request.method == "POST":
        profile.delete()
        return redirect('home page')

    return render(request, "profiles/profile-delete.html")
