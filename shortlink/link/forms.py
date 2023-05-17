from django import forms
from django.db import models

from .models import Link


class LinkForm(forms.ModelForm):
    llink = forms.CharField(
        label='Длинная ссылка',
        required=True,
        help_text='Нельзя вводить более 250 символов',
        widget=forms.TextInput(attrs={'oninput': 'lengthFunction()'})
    )

    slink = forms.CharField(
        label='Короткая ссылка',
        required=True,
        widget=forms.TextInput()
    )
    class Meta:
        model = Link

        fields = ['avtor', 'llink', 'slink']

        widgets = {'avtor': forms.HiddenInput()}

        constraints = [models.UniqueConstraint(fields=['avtor', 'slink'], name='unique_userlink')]
