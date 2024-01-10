from .models import Postdetail
import django_filters

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='Bookname', lookup_expr='icontains')

    class Meta:
        model = Postdetail
        fields = '__all__'
