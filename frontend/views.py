from django.shortcuts import render
from classes.models import OrganicClass


def start_page(request):
    organic_classes = OrganicClass.objects.all()
    return render(request, 'start_page.html', locals())


def class_page(request, class_text_id):
    organic_classes = OrganicClass.objects.all()
    organic_class = OrganicClass.objects.get(text_id=class_text_id)
    return render(request, 'organic_class_page.html', locals())
