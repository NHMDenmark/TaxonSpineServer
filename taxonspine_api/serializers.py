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

  PURPOSE: Serializers for model classes used for serving through api.  
"""

from rest_framework import serializers
from .models import Taxon

class TaxonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxon 
        fields = ["dassco_name",
                  "dassco_author",
                  "dassco_taxonID",
                  "dassco_fullname",
                  "dassco_epithet",
                  "dassco_rankid",
                  "dassco_extinct",
                  "dwc_taxonID",
                  "dwc_scientificName",
                  "dwc_scientificNameAuthorship",
                  "dwc_parentNameUsageID",
                  "dwc_parentNameUsage",
                  "dwc_acceptedNameUsageID",
                  "dwc_acceptedNameUsage",
                  "dwc_taxonomicStatus",
                  "dwc_taxonRank",
                  "sp_taxonID",
                  "sp_fullname",
                  "sp_author",
                  "sp_rankid",
                  "sp_rankname",
                  "sp_parentname",
                  "sp_taxonnr",
                  "sp_taxonnrsource"]