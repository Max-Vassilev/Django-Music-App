from exam_prep.web.models import Profile, Album
from django import forms


class ProfileCreateModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Username",
                },
            ),
            "email": forms.TextInput(
                attrs={
                    "placeholder": "Email",
                },
            ),
            "age": forms.TextInput(
                attrs={
                    "placeholder": "Age",
                },
            ),
        }


class AlbumAddModelForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        exclude = ["profile"]

        widgets = {
            "album_name": forms.TextInput(
                attrs={
                    "placeholder": "Album name",
                },
            ),
            "artist": forms.TextInput(
                attrs={
                    "placeholder": "Artist",
                },
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Description",
                },
            ),
            "image_url": forms.TextInput(
                attrs={
                    "placeholder": "Image URL",
                },
            ),
            "price": forms.TextInput(
                attrs={
                    "placeholder": "Price",
                },
            ),
        }


class AlbumEditModelForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        exclude = ["profile"]

        widgets = {
            "album_name": forms.TextInput(
                attrs={
                    "placeholder": "Album name",
                },
            ),
            "artist": forms.TextInput(
                attrs={
                    "placeholder": "Artist",
                },
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Description",
                },
            ),
            "image_url": forms.TextInput(
                attrs={
                    "placeholder": "Image URL",
                },
            ),
            "price": forms.TextInput(
                attrs={
                    "placeholder": "Price",
                },
            ),
        }


class AlbumDeleteModelForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        exclude = ["profile"]

        widgets = {
            "album_name": forms.TextInput(
                attrs={
                    "placeholder": "Album name",
                },
            ),
            "artist": forms.TextInput(
                attrs={
                    "placeholder": "Artist",
                },
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Description",
                },
            ),
            "image_url": forms.TextInput(
                attrs={
                    "placeholder": "Image URL",
                },
            ),
            "price": forms.TextInput(
                attrs={
                    "placeholder": "Price",
                },
            ),
        }


class ProfileDetailsModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

