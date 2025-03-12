from django import forms

class QRcodeForm(forms.Form):
    restaurant_name = forms.CharField(max_length=128, label='Restaurant Name')
    url = forms.URLField(max_length=128, label='Menu URL')