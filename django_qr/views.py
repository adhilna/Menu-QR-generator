from django.shortcuts import render
from .forms import QRcodeForm
import qrcode
from django.conf import settings
import os


def generate_qr_code(request):
    if request.method == 'POST':
        form = QRcodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']


            # GENERATE QR CODE
            qr = qrcode.make(url)
            file_name = res_name.replace(' ', '_').lower() + '_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)   # ../media/the_kitchen_menu.png
            qr.save(file_path)


            # CREATE IMAGE URL
            qr_url = settings.MEDIA_URL + file_name  # This should be correct


            context = {
                'res_name': res_name,
                'qr_url': qr_url
            }
            return render(request, 'rq_result.html', context)

    else:
        form = QRcodeForm()
        context = {
            'form' : form
        }
        return render(request, 'generate_qr_code.html', context)