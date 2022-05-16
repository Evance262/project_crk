'''Form to submit new gigs'''
from django import forms
from .models import Gig
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify


class GigCreateForm(forms.ModelForm):
    class Meta:
        model = Gig
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }


        def clean_url(self):
            url = self.cleaned_data['url']
            valid_extensions = ['jpg', 'jpeg', 'png']
            extensions = url.rsplit('.', 1)[1].lower()
            if extension not in valid_extensions:
                raise forms.ValidationError('The given URL does not ' \
                                            'match valid gigs extensions.')
            return url


        def save(self, force_insert=False,
                 force_update=False,
                 commit=True):
            '''Overiding the save method to allow whether specied
            objects have to be persisted to the database'''
            gig = super().save(commit=False)
            gig_url = self.cleaned_data['url']
            name = slugify(gig.title)
            extension = gig_url.rsplit('.', 1)[1].lower()
            gig_name = f'{name}.{extension}'

            # download gig from the given URL
            response = request.urlopen(gig_url)
            gig.gig.save(gig_name,
                             ContentFile(response.read()),
                             save=False)


            if commit:
                gig.save()
            return gig