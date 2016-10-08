from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo, VISIBILITY_PUBLIC


def home(request):
    """
    Renderiza el home con un listado de fotos
    :param request: objeto HttpRequest con los datos de la petición.
    :return: objeto HttpResponse con los datos de la respuesta
    """

    photos = Photo.objects.filter(visibility=VISIBILITY_PUBLIC).order_by('-created_at')  # recupera todas las fotos de la base de datos
    context = {'photos_list': photos[:5]}
    return render(request, 'photos/home.html', context)
