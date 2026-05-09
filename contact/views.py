import ssl
import certifi
from django.shortcuts import render
from django.core.mail import get_connection, send_mail
from django.conf import settings
from .models import Contact

def contact_view(request):
    success = False

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)

            ssl_context = ssl.create_default_context(cafile=certifi.where())

            connection = get_connection(
                host='smtp.gmail.com',
                port=587,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=True,
                ssl_context=ssl_context,
            )

            send_mail(
                subject=f"Yangi xabar: {name}",
                message=f"Kimdan: {name}\nEmail: {email}\n\nXabar:\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['husaynsocial@gmail.com'],
                connection=connection,
                fail_silently=False,
            )

            success = True

    return render(request, 'contact.html', {'success': success})