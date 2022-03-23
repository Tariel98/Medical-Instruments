from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


def about(request):
    print(Partner.objects.filter(status='p'))
    return render(request, 'Instruments/about.html', {'partners': Partner.objects.filter(status='p')})


class HomeListView(ListView):
    template_name = 'Instruments/home.html'
    queryset = Category.objects.filter(status='p')
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['BannerItems'] = BannerItems.objects.order_by('-date').filter(status='p')
        return context


class ProductView(ListView):
    template_name = 'Instruments/products.html'
    queryset = Instrument.objects.filter(status='p')
    context_object_name = 'instruments'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by('-date').filter(status='p')
        return context


class CategoryView(ListView):
    template_name = 'Instruments/products.html'
    queryset = Category.objects.filter(status='p')

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['filtred_Instruments'] = Instrument.objects.filter(instrument_category__slug=self.kwargs['slug'],
                                                                   status='p').order_by('-date')
        context['categories'] = Category.objects.filter(status='p')
        return context


class InstrumentView(DetailView):
    queryset = Instrument.objects.filter(status='p')
    context_object_name = 'instruments'
    template_name = 'Instruments/InstrumentView.html'

    def get_context_data(self, **kwargs):
        context = super(InstrumentView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(status='p')
        return context
