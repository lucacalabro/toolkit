from django.shortcuts import render
from allauth.account.decorators import verified_email_required


# Create your views here.


@verified_email_required
def verified_users_only_view(request):
    return render(request, "social_app/altrapagina.html", {"request": request.user.email})


def not_logged_view(request):
    return render(request, "social_app/paginanonloggata.html")
