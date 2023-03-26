from django.db.models import Prefetch, OuterRef, Subquery, Min
from rest_framework import viewsets

from .models import Product, Price, Size
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    last_price_for_size_subquery = Subquery(
        Price.objects.filter(product_size=OuterRef("id"))
        .order_by('-updated_at')
        .values('price')[:1]
    )

    queryset = (
        Product.objects.all()
        .prefetch_related(
            'brand',
            Prefetch('sizes', queryset=Size.objects.annotate(price=last_price_for_size_subquery)),
        )
    )
    serializer_class = ProductSerializer
