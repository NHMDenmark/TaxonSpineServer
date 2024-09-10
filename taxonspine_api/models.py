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
import uuid

# Create your models here.

class Taxon(models.Model):
    '''
    The taxon class encapsulates all of the data fields for the taxon concept as child nodes of the taxon spine. 
    It combines taxa from three different sources, and to reflect this, the fields are divided in three kinds identified by prefixes "dassco", "dwc" and "specify". 
    The dwc fields derive from the GBIF taxonomic backbone and the specify fields derive from the Specify taxon tree.
    The dassco fields are derived from both and where dwc and specify overlap, the name fields are identical; 
    In cases of no overlap either the dwc or the specify fields are empty, but the dwc fields then never. 
    '''

    dassco_taxonID = models.CharField(max_length=32) #models.UUIDField(default=uuid.uuid4, null=False)
    dassco_name = models.CharField(max_length=255)
    dassco_author = models.CharField(max_length=255, null=True)
    dassco_fullname = models.CharField(max_length=255)
    dassco_epithet = models.CharField(max_length=255, null=True)
    dassco_rankid = models.CharField(max_length=4)
    dassco_acceptedid = models.IntegerField(null=True)
    dassco_extinct = models.BooleanField(null=True)
    dwc_taxonID = models.IntegerField(null=True)
    dwc_scientificName = models.CharField(max_length=255, null=True)
    dwc_scientificNameAuthorship = models.CharField(max_length=255, null=True)
    dwc_parentNameUsageID = models.IntegerField(null=True)
    dwc_parentNameUsage = models.CharField(max_length=255, null=True)
    dwc_acceptedNameUsageID = models.IntegerField(null=True)
    dwc_acceptedNameUsage = models.CharField(max_length=255, null=True)
    dwc_taxonomicStatus = models.CharField(max_length=32)
    dwc_taxonRank = models.CharField(max_length=16, null=True)
    sp_taxonID = models.IntegerField(null=True)
    sp_fullname = models.CharField(max_length=255, null=True)
    sp_author = models.CharField(max_length=255, null=True)
    sp_rankid = models.CharField(max_length=4)
    sp_rankname = models.CharField(max_length=16, null=True)
    sp_parentname = models.CharField(max_length=255, null=True)
    sp_taxonnr = models.CharField(max_length=255, null=True)
    sp_taxonnrsource = models.CharField(max_length=255, null=True)
    timestamp_created = models.DateTimeField(auto_now_add=True,auto_now=False, blank=True)
    timestamp_updated = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.dassco_fullname