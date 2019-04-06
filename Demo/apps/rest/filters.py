from rest_framework import filters as drf_filter
from django_filters import rest_framework as filters
from apps.rest.models import Goods


class GoodsFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="shop_price", lookup_expr='gte', label='本店价格的开始区间')
    max_price = filters.NumberFilter(field_name="shop_price", lookup_expr='lte', label='本店价格的结束区间')
    # name = filters.CharFilter(field_name='name', lookup_expr='icontains', label='模糊查询商品名')

    class Meta:
        model = Goods
        # fields = ['min_price', 'max_price', 'name']
        fields = ['min_price', 'max_price']
