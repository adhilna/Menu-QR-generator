from django.shortcuts import render
from .forms import QRcodeForm
import qrcode
from django.conf import settings
import os
import logging

logger = logging.getLogger(__name__)

def generate_qr_code(request):
    if request.method == 'POST':
        try:
            form = QRcodeForm(request.POST)
            if form.is_valid():
                res_name = form.cleaned_data['restaurant_name']
                url = form.cleaned_data['url']

                # Generate QR code
                qr = qrcode.make(url)
                file_name = res_name.replace(' ', '_').lower() + '_menu.png'
                file_path = os.path.join(settings.MEDIA_ROOT, file_name)

                # Ensure media directory exists
                os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

                qr.save(file_path)

                qr_url = settings.MEDIA_URL + file_name
                context = {
                    'res_name': res_name,
                    'qr_url': qr_url,
                    'file_name': file_name,
                }
                return render(request, 'rq_result.html', context)
            else:
                return render(request, 'generate_qr_code.html', {'form': form})
        except Exception as e:
            logger.error("QR generation error: %s", e, exc_info=True)
            return render(request, 'generate_qr_code.html', {
                'form': QRcodeForm(),
                'error': "An error occurred while generating the QR code."
            })
    else:
        form = QRcodeForm()
        return render(request, 'generate_qr_code.html', {'form': form})
