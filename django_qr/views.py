from django.shortcuts import render
from .forms import QRcodeForm
import qrcode
from django.core.files.base import ContentFile
from io import BytesIO
import logging
from django.conf import settings
import os
import traceback
import uuid
import cloudinary.utils

logger = logging.getLogger(__name__)

def generate_qr_code(request):
    print("DEBUG: DEFAULT_FILE_STORAGE =", settings.DEFAULT_FILE_STORAGE)
    print("DEBUG: CLOUDINARY_STORAGE =", getattr(settings, 'CLOUDINARY_STORAGE', None))
    print("DEBUG: DJANGO_SETTINGS_MODULE =", os.environ.get('DJANGO_SETTINGS_MODULE'))
    print("DEBUG: request method =", request.method)

    if request.method == 'POST':
        try:
            form = QRcodeForm(request.POST)
            print("DEBUG: form.is_valid() =", form.is_valid())

            if form.is_valid():
                res_name = form.cleaned_data['restaurant_name']
                url = form.cleaned_data['url']
                print(f"DEBUG: restaurant_name = {res_name}")
                print(f"DEBUG: url = {url}")

                # Generate QR code in memory
                qr = qrcode.make(url)
                buffer = BytesIO()
                qr.save(buffer, format='PNG')
                buffer.seek(0)
                print("DEBUG: buffer size =", len(buffer.getvalue()))

                # Generate safe, unique file name
                file_name = f"{res_name.replace(' ', '_').lower()}_{uuid.uuid4().hex[:8]}.png"
                print(f"DEBUG: file_name = {file_name}")

                # Import storage here to avoid early evaluation
                from django.utils.module_loading import import_string
                default_storage = import_string(settings.DEFAULT_FILE_STORAGE)()

                print("DEBUG: default_storage class =", default_storage.__class__)

                # Save to default storage (Cloudinary)
                file_content = ContentFile(buffer.getvalue())
                saved_path = default_storage.save(file_name, file_content)
                from cloudinary.utils import cloudinary_url
                qr_url, options = cloudinary_url(
                saved_path,
                resource_type="image",
                type="upload",
                transformation=[
                    {"flags": "attachment"}
                ],
                attachment=file_name
                )
                print("✅ SAVED_PATH =", saved_path)
                print("✅ QR_URL =", qr_url)

                context = {
                    'res_name': res_name,
                    'qr_url': qr_url,
                    'file_name': file_name,
                }
                print("DEBUG CONTEXT:", context)
                return render(request, 'rq_result.html', context)

            else:
                print("DEBUG: Form errors =", form.errors)
                return render(request, 'generate_qr_code.html', {'form': form})

        except Exception as e:
            logger.error("QR generation error: %s", e, exc_info=True)
            traceback.print_exc()
            return render(request, 'generate_qr_code.html', {
                'form': QRcodeForm(),
                'error': "An error occurred while generating the QR code."
            })

    else:
        form = QRcodeForm()
        print("DEBUG: GET request — rendering blank form")
        return render(request, 'generate_qr_code.html', {'form': form})
