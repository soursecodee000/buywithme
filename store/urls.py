# store/urls.py
from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet, basename='collections')
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')

# Nested router for products and their reviews/images
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')
products_router.register('images', views.ProductImageViewSet, basename='product-images')

# Nested router for carts and their items
carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

# Nested router for collections to fetch products
collections_router = routers.NestedDefaultRouter(router, 'collections', lookup='collection')
collections_router.register('products', views.CollectionProductsViewSet, basename='collection-products')
collections_router.register('images', views.CollectionImageViewSet, basename='collection-images')
# URLConf
urlpatterns = router.urls + products_router.urls + carts_router.urls + collections_router.urls
