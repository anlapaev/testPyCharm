from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.template.response import TemplateResponse
from .forms import UserForm


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст - {1}</h3>".format(name,age)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "firstapp/my_form.html", {"form": userform})


def about(request):
    header = "Lad академия"
    langs = ["Python", "C#", "JS"]
    user = {"name": "Andrey", "city": "NN"}
    addr = ("Урицкого", 68)
    data = {"header": header, "langs": langs, "user": user, "adress": addr}
    return TemplateResponse(request, "firstapp/about.html", data)


def my_form(request):
    my_form = UserForm()
    context = {'form': my_form}
    return render(request, 'firstapp/my_form.html', context)


def contact(request):
    return HttpResponseRedirect("/about/123")


def details(request):
    return HttpResponsePermanentRedirect("/")


def products(request, productid=0):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0} Категория: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request, id, name):
    output = '<h2>Имя: {0}, ID: {1}</h2>'.format(name, id)
    return HttpResponse(output)


def m404(request):
    return HttpResponseNotFound('<h1>Страничка потерялась!</h1>')