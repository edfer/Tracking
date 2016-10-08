from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from photos.models import Photo, VISIBILITY_PUBLIC


def home(request):
    """
    Renderiza el home con un listado de fotos
    :param request: objeto HttpRequest con los datos de la petición.
    :return: objeto HttpResponse con los datos de la respuesta
    """

    # recupera todas las fotos de la base de datos
    photos = Photo.objects.filter(visibility=VISIBILITY_PUBLIC).order_by('-created_at')
    context = {'photos_list': photos[:5]}
    return render(request, 'photos/home.html', context)

def photo_detail(request, pk):
    """
    Renderiza el detalle de una imagen
    :param request: objeto HttpRequest con los datos de la petición.
    :return: objeto HttpResponse con los datos de la respuesta
    """
    possible_photos = Photo.objects.filter(pk=pk)
    if len(possible_photos) == 0:
        return HttpResponseNotFound("La imagen no existe")
    elif len(possible_photos) > 1:
        return HttpResponse("Múltiples opciones", status=300)

    photo = possible_photos[0]
    context = {'photo': photo}

    return render(request, 'photos/photo_detail.html', context)