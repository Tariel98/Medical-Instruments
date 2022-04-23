from django.shortcuts import render, redirect
from .models import BannerItems, Category, Partner, Instrument, InstrumentModel
from django.views.generic import ListView, DetailView
from .forms import SearchForm


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
        print(context['BannerItems'])
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
                                                                   status='p').order_by('created_at')
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


class ModelDetailView(DetailView):
    queryset = InstrumentModel.objects.all()
    context_object_name = 'models'
    template_name = 'Instruments/modelview.html'

    def get_context_data(self, **kwargs):
        context = super(ModelDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(status='p')
        return context


class AllModelsDetailView(DetailView):
    queryset = Instrument.objects.all()
    context_object_name = 'instruments'
    template_name = 'Instruments/models_all.html'

    def get_context_data(self, **kwargs):
        context = super(AllModelsDetailView, self).get_context_data(**kwargs)

        context['categories'] = Category.objects.filter(status='p')
        return context


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return render(request, 'Instruments/products.html', {
                'instruments': [i for i in Instrument.objects.all() if
                                request.POST['search'].lower() in i.name.lower()],
                'categories': Category.objects.filter(status='p')})

    return redirect('products')
