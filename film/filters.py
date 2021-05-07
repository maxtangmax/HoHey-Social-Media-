import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class film_profile_filter(django_filters.FilterSet):
	start_date = DateFilter(field_name="Year", lookup_expr='gte')
	end_date = DateFilter(field_name="Year", lookup_expr='lte')
	film_name = CharFilter(field_name="film_name", lookup_expr='icontains')

	class Meta:
		model=film_profile
		fields=['film_name','Director',
				'Producer',
				'Year',
				'Language',
				'Actors']
		exclude = 'Year'