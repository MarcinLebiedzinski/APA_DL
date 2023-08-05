from django.shortcuts import render
from django.views import View

# Create your views here.


class Main(View):
    def get(self, request):
        ctx = {}
        return render(request, 'index.html', ctx)
