from django.shortcuts import render, get_object_or_404
from store.models import Product, Collection
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from store.serializers import ProductSerializer  # Import the ProductSerializer

class CollectionProductsView(APIView):
    def get(self, request, collection_id, *args, **kwargs):
        products = Product.objects.filter(collection_id=collection_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

def index(request):
    products = Product.objects.all()
    return render(request, 'core/index.html', {'products': products})

def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    return render(request, 'core/contact.html')

def collection_products(request, collection_id):
    # Ensure you have a Collection model and filter products based on the collection
    collection = get_object_or_404(Collection, id=collection_id)
    products = Product.objects.filter(collection=collection)  # Adjust this line if your relation is different

    # Prepare the data to send back in the response
    products_data = [{
        'id': product.id,
        'title': product.title,
        'unit_price': product.unit_price,
        'images': [{'image': product.image.url} for product in product.images.all()]
    } for product in products]

    return JsonResponse(products_data, safe=False)
