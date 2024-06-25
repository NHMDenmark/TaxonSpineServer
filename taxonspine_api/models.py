# -*- coding: utf-8 -*-
"""
  Created on June 25, 2024
  @author: Fedor Alexander Steeman, NHMD
  Copyright 2024 Natural History Museum of Denmark (NHMD)
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

  PURPOSE: Model classes for taxon spine server api 
"""

from django.db import models

# Create your models here.

class Taxon(models.Model):
    '''
    The taxon class encapsulates all of the data fields for the taxon concept as child nodes of the taxon spine. 
    It combines taxa from three different sources, and to reflect this, the fields are divided in three kinds identified by prefixes "dassco", "dwc" and "specify". 
    The dwc fields derive from the GBIF taxonomic backbone and the specify fields derive from the Specify taxon tree.
    The dassco fields are derived from both and where dwc and specify overlap, the name fields are identical; 
    In cases of no overlap either the dwc or the specify fields are empty, but the dwc fields then never. 
    '''

    dassco_taxonID = models.CharField(max_length=255, null=False)
    dassco_taxonID = models.CharField(max_length=255)
    dassco_name = models.CharField(max_length=255)
    dassco_author = models.CharField(max_length=255)
    dassco_fullname = models.CharField(max_length=255)
    dassco_epithet = models.CharField(max_length=255)
    dassco_rankid = models.CharField(max_length=255)
    dassco_extinct = models.CharField(max_length=255)
    dwc_taxonID = models.CharField(max_length=255)
    dwc_scientificName = models.CharField(max_length=255)
    dwc_scientificNameAuthorship = models.CharField(max_length=255)
    dwc_parentNameUsageID = models.CharField(max_length=255)
    dwc_parentNameUsage = models.CharField(max_length=255)
    dwc_acceptedNameUsageID = models.CharField(max_length=255)
    dwc_acceptedNameUsage = models.CharField(max_length=255)
    dwc_taxonomicStatus = models.CharField(max_length=255)
    dwc_taxonRank = models.CharField(max_length=255)
    sp_taxonID = models.CharField(max_length=255)
    sp_fullname = models.CharField(max_length=255)
    sp_author = models.CharField(max_length=255)
    sp_rankid = models.CharField(max_length=255)
    sp_rankname = models.CharField(max_length=255)
    sp_parentname = models.CharField(max_length=255)
    sp_taxonnr = models.CharField(max_length=255)
    sp_taxonnrsource = models.CharField(max_length=255)
    timestamp_created = models.DateTimeField(auto_now_add=True,auto_now=False, blank=True)
    timestamp_updated = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.dassco_fullname