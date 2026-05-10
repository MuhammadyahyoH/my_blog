from django.shortcuts import render
from django.core.mail import send_mail
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

            send_mail(
                subject=f"Yangi xabar: {name}",
                message=f"Kimdan: {name}\nEmail: {email}\n\nXabar:\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['husaynsocial@gmail.com'],
                fail_silently=False,
            )

            success = True

    return render(request, 'contact.html', {'success': success})