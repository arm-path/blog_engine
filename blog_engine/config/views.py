from django.http import HttpResponse
from django.shortcuts import redirect


def redirect_blog(request):
    return redirect('post_list_url')


def testing_request(request):
    print('------->REQUEST<-------')
    print('------->request: ', request)
    print('------->dir(request): ', dir(request))
    print('------->request.URL: ', request.path)
    print('------->request.COOKIES: ', request.COOKIES)
    print('------->request.FILES: ', request.FILES)
    print('------->request.GET: ', request.GET)
    print('------->request.META: ', request.META)
    print('------->request.POST: ', request.POST)
    print('------->dir(request): ', dir(request))
    print('------->request.accepted_types', request.accepted_types)
    print('------->request.accepts', request.accepts)
    print('------->request.body', request.body)
    print('------->request.build_absolute_uri', request.build_absolute_uri)
    print('------->request.get_full_path', request.get_full_path)

    return HttpResponse('<h1>Hello world!</h1>')
