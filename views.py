# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView
from .models import Product
from django.shortcuts import render
from .models import News

from django.shortcuts import render
from .models import News


class ProductsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Product
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'name'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'products.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'products'


def news_list(request):
    news = News.objects.all().order_by('-publication_date')
    return render(request, 'news_list.html', {'news': news})


def news_detail(request, news_id):
    article = News.objects.get(id=news_id)
    return render(request, 'news_detail.html', {'article': article})


def news_detail(request, id):
    news_item = News.objects.get(id=id)
    return render(request, 'news_detail.html', {'news': news_item})
