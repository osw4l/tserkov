from django import forms
from .models import Musician


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = (
            'username',
            'first_name',
            'last_name',
            'instruments'
        )

