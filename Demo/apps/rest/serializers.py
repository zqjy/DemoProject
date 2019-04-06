# coding=utf-8
from rest_framework import serializers
from apps.rest.models import Goods, GoodsCategory


class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()

    class Meta:
        model = Goods
        # fields = ('id', 'name', 'click_num', 'sold_num', 'market_price', 'add_time')
        fields = '__all__'

# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Goods.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         # instance.title = validated_data.get('title', instance.title)
#         # instance.code = validated_data.get('code', instance.code)
#         # instance.linenos = validated_data.get('linenos', instance.linenos)
#         # instance.language = validated_data.get('language', instance.language)
#         # instance.style = validated_data.get('style', instance.style)
#         # instance.save()
#         return instance
