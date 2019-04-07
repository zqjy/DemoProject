from rest_framework import filters as drf_filter
from django_filters import rest_framework as filters
from django.db.models import Q

from apps.rest.models import Goods


class GoodsFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="shop_price", lookup_expr='gte', label='本店价格的开始区间', help_text='最低价格')
    max_price = filters.NumberFilter(field_name="shop_price", lookup_expr='lte', label='本店价格的结束区间', help_text='最高价格')
    # name = filters.CharFilter(field_name='name', lookup_expr='icontains', label='模糊查询商品名')
    top_category = filters.NumberFilter(method='top_category_filter', label='类别商品', help_text='类别ID')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value)
                               | Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        # fields = ['min_price', 'max_price', 'name']
        fields = ['min_price', 'max_price', 'top_category']
