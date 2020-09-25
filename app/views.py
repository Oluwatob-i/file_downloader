from django.shortcuts import render
import os, socket, pathlib, requests

# Create your views here.

def test(request):
    host = socket.gethostname()
    print(next(os.walk(pathlib.Path.home())))
    ip = socket.gethostbyname(host)

    context = {'ip': ip}
    return render(request, 'downloader/test.html', context)
