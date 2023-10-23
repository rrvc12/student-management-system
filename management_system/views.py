from django.views.generic import View
from django.http import HttpResponse

class HomeView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World")
    

class HomeContactView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, Contact")