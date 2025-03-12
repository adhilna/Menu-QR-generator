from django.shortcuts import render
from .forms import QRcodeForm
import qrcode


def generate_qr_code(request):
    if request.method == 'POST':
        form = QRcodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']


            # GENERATE QR CODE
            qr = qrcode.make(url)
            file_name = res_name.replace(' ', '_').lower() + '_menu.png'
            qr.save(file_name)

    else:
        form = QRcodeForm()
        context = {
            'form' : form
        }
        return render(request, 'generate_qr_code.html', context)