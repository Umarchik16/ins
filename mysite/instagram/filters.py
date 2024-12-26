import django_filters
from django_filters.rest_framework import FilterSet
from .models import *


class PostFilter(django_filters.FilterSet):
    created_at = django_filters.DateFilter(field_name="created_at", lookup_expr="date")
    user = django_filters.CharFilter(field_name="user__username", lookup_expr="icontains")

    class Meta:
        model = Post
        fields = ['user', 'created_at']

