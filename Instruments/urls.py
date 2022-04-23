from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import ModelDetailView, HomeListView, ProductView, about, CategoryView, InstrumentView, search, \
    AllModelsDetailView

urlpatterns = [
    path('', HomeListView.as_view(), name='Home'),
    path('Products/', ProductView.as_view(), name='products'),
    path('About/', about, name='about'),
    path('categories/<slug:slug>/', CategoryView.as_view(), name='CategoryView'),
    path('instrument/<slug:slug>/', InstrumentView.as_view(), name='InstrumentView'),
    path('search/', search, name='search'),
    path('models/<int:pk>/', ModelDetailView.as_view(), name='model_detail_view'),
    path('all_models<int:pk>', AllModelsDetailView.as_view(), name='all_models'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
