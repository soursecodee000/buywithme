from django.views.generic import TemplateView
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from store.views import CollectionViewSet

# URLConf
router = DefaultRouter()
router.register(r'store/collections', CollectionViewSet, basename='collection')

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/home.html'), name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('store/collections/<int:collection_id>/products/', views.CollectionProductsView.as_view(), name='collection-products'),
    
    # Include all routes defined by the router after specific routes
    path('', include(router.urls)),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
