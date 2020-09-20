from django.shortcuts import render
import os, socket, pathlib, requests
# Create your views here.

def test(request):
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    context = {'ip': ip}
    return render(request, 'downloader/test.html', context)
