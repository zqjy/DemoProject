from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.rest.models import Goods
from apps.rest.serializers import GoodsSerializer
from apps.rest.filters import GoodsFilter


# 自定义分页类 代替REST_FRAMEWORK中分页配置
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表
    """
    queryset = Goods.objects.all()  # 已配置分页  # 被get_queryset() 替代  # 结合django-filter使用
    serializer_class = GoodsSerializer  # 指定序列化类
    pagination_class = GoodsPagination  # 指定自定义分页类
    # filter_backends = (DjangoFilterBackend,)  # 设置过滤类
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # 设置过滤类 配置drf的过滤器
                                                                                            # 配置排序过滤器
    # filter_fields = ('name', 'shop_price')  # 设置过滤属性 # 被自定义过滤替换
    filter_class = GoodsFilter  # 配置自定义过滤类
    search_fields = ('name', 'goods_brief', 'goods_desc')  # 配置搜索的字段
    ordering_fields = ('sold_num', 'add_time')  # 配置排序字段
    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's MySQL backend.)
    # '$' Regex search.


    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     # 获取url参数中传过来的"要查询的商品的价格阈值",如果没有传就设置为0
    #     price_min = self.request.query_params.get('price_min', 0)
    #     if price_min:
    #         queryset = queryset.filter(shop_price__gt=int(price_min))
    #
    #     return queryset
        # return Goods.objects.filter(shop_price__gt=100)


class GoodListView(generics.ListAPIView):
    """
    商品列表页
    """
    # queryset = Goods.objects.all()[:10]  # 未配置分页
    queryset = Goods.objects.all()  # 已配置分页
    serializer_class = GoodsSerializer  # 指定序列化类
    pagination_class = GoodsPagination  # 指定自定义分页类

# class GoodListView(mixins.ListModelMixin, generics.GenericAPIView):
#     """
#     商品列表页
#     """
#     queryset = Goods.objects.all()[:10]
#     serializer_class = GoodsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# class GoodListView(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)
#
#     def post(self, request, format=None):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
