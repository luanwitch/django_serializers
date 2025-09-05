from django.http import HttpResponse

def home(request):
    return HttpResponse("Django está rodando no projeto django_serializers 🚀")
