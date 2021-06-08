import django_filters
from .models import *

class BenchFilter(django_filters.FilterSet):
    class Meta:
        model = BenchResource
        fields = '__all__'