from django.core.exceptions import ValidationError

from photos.models import Photo
from django.forms import  ModelForm


BADWORDS = ("meapilas", "aparcabicis", "afinabanjos", "abrazafarolas")

class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        exclude = ['owner']

    def clean(self):
        """

        :return:
        """

        cleaned_data = super().clean()
        description = cleaned_data.get('description', '')
        for badword in BADWORDS:
            if badword in description:
                raise ValidationError("La palabra {0} no está permitida".format(badword))
        return cleaned_data