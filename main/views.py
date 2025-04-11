from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Главная'
        context['content'] = "Магазин обмена товарами"
        return context


def about(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Главная',
    }
    return render(request, "index.html", context)
