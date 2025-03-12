from django.shortcuts import render
from .forms import QRcodeForm


def generate_qr_code(request):
    if request.method == 'POST':
        form = QRcodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']
    else:
        form = QRcodeForm()
        context = {
            'form' : form
        }
        return render(request, 'generate_qr_code.html', context)