from django.shortcuts import render
from classes.models import OrganicClass


def start_page(request):
    organic_classes = OrganicClass.objects.all()
    return render(request, 'organic_class_page.html', locals())

