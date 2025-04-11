from .models import Ad
from .forms import AdForm
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ads.utils import q_search


#class CatalogView(ListView):
#    model = Ad
#    template_name = "goods/catalog.html"
#    context_object_name = "goods"
#    paginate_by = 3
#    allow_empty = False
#    slug_url_kwarg = "category_slug"
#
#    def get_queryset(self):
#        category_slug = self.kwargs.get(self.slug_url_kwarg)
#        on_sale = self.request.GET.get("on_sale")
#        order_by = self.request.GET.get("order_by")
#        query = self.request.GET.get("q")
#
#        if category_slug == "all":
#            goods = super().get_queryset()
#        elif query:
#            goods = q_search(query)
#        else:
#            goods = super().get_queryset().filter(category__slug=category_slug)
#            if not goods.exists():
#                raise Http404()
#
#        if on_sale:
#            goods = goods.filter(discount__gt=0)
#
#        if order_by and order_by != "default":
#            goods = goods.order_by(order_by)
#
#        return goods
#    
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context["title"] = "Home - Каталог"
#        context["slug_url"] = self.kwargs.get(self.slug_url_kwarg)
#        return context
#
#



#def catalog_view(request, category_slug, page = 1):
#    if category_slug == "all":
#        ads = Ad.objects.all() 
#    else:
#        ads = get_object_or_404(Ad.objects.filter(category_slug=category_slug))
#
#    paginator = Paginator(ads, 8)
#    current_page = paginator.page(page)
#    context = {
#        'title': 'Каталог товаров',
#        'ads': current_page,
#    }
#    return render(request, 'catalog.html', context)

def catalog_view(request, page = 1):
    ads = Ad.objects.all() 
    paginator = Paginator(ads, 8)
    current_page = paginator.page(page)
    context = {
        'title': 'Каталог товаров',
        'ads': current_page
    }
    return render(request, 'catalog.html', context)


def create_ad(request) -> HttpResponse:
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user 
            ad.save()  
            return redirect('ads:catalog')  
        form = AdForm()
    else:
        form = AdForm()
    context: dict = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, "create_ad.html", context)


def ad_detail_view(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, 'ad_detail.html', {'ad': ad})


def update_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id) 

    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad) 
        if form.is_valid():
            form.save()  
            return redirect('ads:catalog') 
    else:
        form = AdForm(instance=ad)  

    context = {
        'title': 'Редактирование объявления',
        'form': form,
        'ad': ad, 
    }
    return render(request, "update_ad.html", context)


def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    ad.delete() 
    return redirect('ads:catalog') 