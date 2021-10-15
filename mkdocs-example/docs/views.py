from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.staticfiles.views import serve
import os
#use this import to make the document password protected
from django.contrib.auth.decorators import login_required

# use @login_required auth decorator to make the page accessible if the user has an active session
#@login_required(login_url='login')
def serve_docs(request,path):
    #get the mkdocs dir path
    docs_path = os.path.join(settings.DOCS_DIR, path)

    if os.path.isdir(docs_path):
        #automatically display index.html page in home page
        path = os.path.join(path, 'index.html')

    path = os.path.join(settings.DOCS_STATIC_NAMESPACE, path)

    return serve(request, path)
    #use return serve(request, path, insecure=True) in production mode 