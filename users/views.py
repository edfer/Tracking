from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect
from users.forms import LoginForm


def login(request):
    """

    :param request:
    :return:
    """

    error_message = ""
    login_form = LoginForm(request.POST) if request.method == "POST" else LoginForm()
    if request.method == "POST":
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_message = "Usuario o contraseña incorrectas"
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect(request.GET.get('next', '/'))
                else:
                    error_message = "Cuenta de usuario inactiva"

    context = {'error': error_message, 'form': login_form}
    return render(request, 'users/login.html', context)

def logout(request):
    """

    :param request:
    :return:
    """
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('/')