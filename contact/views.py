from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"""
            You have received a new contact message.

            Name: {name}
            Email: {email}
            Subject: {subject}

            Message:
            {message}
            """

            send_mail(
                subject=f"CEK Contact: {subject}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully.")
            return redirect('home')

        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = ContactForm()

    return render(request, 'home.html', {'contact_form': form})
