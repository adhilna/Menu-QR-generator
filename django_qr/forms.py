from django import forms

class QRcodeForm(forms.Form):
    restaurant_name = forms.CharField(
        max_length=128,
        label='Restaurant Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Restaurant Name',

        })
        )
    url = forms.URLField(
        max_length=128,
        label='Menu URL',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the URL for your online-menu'
        })
        )