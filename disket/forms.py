import os
import zipfile

from os.path import join, basename
from django import forms
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from .models import Disket, DisketVersion


class DisketUploadForm(forms.ModelForm):
    class Meta:
        model = Disket
        fields = ["label", "tagline", "shelf", "visibility", "zip_file"]

    def clean_zip_file(self):
        zip_file = self.cleaned_data.get("zip_file")
        if zip_file.size > 1.44 * 1024 * 1024:
            raise forms.ValidationError(
                "The upload size must not exceed 1.44MB."
            )
        try:
            with zipfile.ZipFile(zip_file, "r") as zip_ref:
                if "index.html" not in zip_ref.namelist():
                    raise forms.ValidationError(
                        "index.html is missing in the uploaded zip file."
                    )
                zip_folder_name = basename(zip_file.name)
                base_dir = os.path.join("page", zip_folder_name)
                for file_name in zip_ref.namelist():
                    if file_name.endswith("/"):
                        continue  # Skip directories
                    file_data = zip_ref.read(file_name)
                    file_path = join(base_dir, file_name)
                    default_storage.save(file_path, ContentFile(file_data))
                self.instance.content_path = str(base_dir)
        except zipfile.BadZipFile:
            raise forms.ValidationError(
                "The uploaded file is not a valid zip file."
            )
        except KeyError as e:
            raise forms.ValidationError(
                f"Error accessing item in the zip file: {e}"
            )
        return zip_file


class DisketEditForm(forms.ModelForm):
    log = forms.CharField(
        max_length=255, required=False, help_text="Log of the changes made"
    )

    class Meta:
        model = Disket
        fields = ["label", "tagline", "shelf", "visibility", "zip_file"]

    def clean_zip_file(self):
        return self.cleaned_data.get("zip_file")

    def save(self, commit=True):
        disket = super().save(commit)
        DisketVersion.objects.create(
            disket=disket, log=self.cleaned_data.get("log")
        )
        return disket
