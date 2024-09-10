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

  PURPOSE: Viewset for models to be served and accessed through api.  
"""

from rest_framework import viewsets, permissions 
from .models import Taxon
from .serializers import TaxonSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TaxonFilter
from typing import Optional

class TaxonViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for editing or viewing a taxon
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = Taxon.objects.all()
    serializer_class = TaxonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaxonFilter       
    search_fields = ['dassco_name']

    def get_queryset(self):
        dassco_name: Optional[str] = self.request.query_params.get("dassco_name", None)
        if dassco_name is not None: 
            return Taxon.objects.filter(dassco_name=dassco_name)
        
        dassco_author: Optional[str] = self.request.query_params.get("dassco_author", None)
        if dassco_author is not None: 
            return Taxon.objects.filter(dassco_author=dassco_author)
        
        dassco_fullname: Optional[str] = self.request.query_params.get("dassco_fullname", None)
        if dassco_fullname is not None: 
            return Taxon.objects.filter(dassco_fullname=dassco_fullname)
        
        dassco_epithet: Optional[str] = self.request.query_params.get("dassco_epithet", None)
        if dassco_epithet is not None: 
            return Taxon.objects.filter(dassco_epithet=dassco_epithet)
        
        dassco_rankid: Optional[str] = self.request.query_params.get("dassco_rankid", None)
        if dassco_rankid is not None: 
            return Taxon.objects.filter(dassco_rankid=dassco_rankid)


        return super().get_queryset()