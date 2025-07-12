# 🌐 QR Code Generator

A simple Django-based web app that lets you generate QR codes for URLs — and **stores them on Cloudinary** for easy sharing or downloading.

## 🚀 Live Demo

🔗 [Visit the Live Site on Render](https://menu-qr-generator.onrender.com/)


---

## 📸 Features

- ✅ Generate QR codes from any URL
- ☁️ Upload QR images to **Cloudinary**
- 🔗 Get a **shareable QR image link**
- 📥 Download the QR as a PNG
- 🎨 Beautiful animated UI with Bootstrap

---

## 🛠️ Built With

- [Python 3.10+](https://www.python.org/)
- [Django 5.1](https://www.djangoproject.com/)
- [Cloudinary](https://cloudinary.com/) (Media hosting)
- [Render](https://render.com/) (Deployment)
- [Bootstrap 5](https://getbootstrap.com/) (Styling)
- [qrcode](https://pypi.org/project/qrcode/) Python library

---

## 🧰 Environment Variables

To run locally or deploy, add these in your `.env` file or Render settings:

```env
DJANGO_SECRET_KEY=your-secret-key
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

🖥️ Run Locally

git clone https://github.com/adhilna/Menu-QR-generator
cd qr-code-generator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py runserver

🌩️ Deployment Notes

Deployed on Render
Static/media files stored via Cloudinary
Used environment variables for production secrets
cloudinary_storage handles file uploads

⭐️ Show Your Support
If you like this project, give it a ⭐ on GitHub and share it with others!
