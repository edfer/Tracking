from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect


def login(request):
    """

    :param request:
    :return:
    """

    error_message = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user is None:
            error_message = "Usuario o contraseña incorrectas"
        else:
            if user.is_active:
                django_login(request, user)
                return redirect('/')
            else:
                error_message = "Cuenta de usuario inactiva"

    return render(request, 'users/login.html', {'error': error_message})

def logout(request):
    """

    :param request:
    :return:
    """
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('/')