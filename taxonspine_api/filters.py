import django_filters
from .models import Taxon

class TaxonFilter(django_filters.FilterSet):
    class Meta:
        model = Taxon
        fields  = {
            'dassco_name':['icontains'],
            'dassco_author':['icontains'],
            'dassco_fullname':['icontains'],
            'dassco_epithet':['icontains'],
            'dassco_rankid':['exact'],
            
        }