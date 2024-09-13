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
            'dassco_acceptedid':['exact'],
            'dwc_taxonID':['exact'],
			'dassco_extinct':['exact'],
			'dwc_scientificName':['icontains'],
			'dwc_scientificNameAuthor':['icontains'],
			'dwc_parentNameUsageID':['exact'],
			'dwc_parentNameUsage':['icontains'],
			'dwc_acceptedNameUsageID':['exact'],
			'dwc_acceptedNameUsage':['icontains'],
			'dwc_taxonomicStatus':['exact'],
			'dwc_taxonRank':['exact'],
			'sp_taxonID':['exact'],
			'sp_fullname':['icontains'],
			'sp_author':['icontains'],
			'sp_rankid':['exact'],
			'sp_rankname':['exact'],
			'sp_parentname':['icontains'],
			'sp_taxonnr':['exact'],
			'sp_taxonnrsource':['icontains'],
        }