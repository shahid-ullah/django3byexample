# images/forms.py

from urllib import request

from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError(
                'The Given URL does not match valid image extensions.'
            )
        return url

    def save(self, force_insert=False, force_update=False, commit=False):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']

        # generate image name
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'

        # Download image from the give URL
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image.save()
        return image
