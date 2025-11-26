from django import forms

class QRcodeForm(forms.Form):
    restaurant_name = forms.CharField(
        max_length=128,
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter name for your QR',

        })
        )
    url = forms.URLField(
        max_length=128,
        label='URL',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the URL'
        })
        )