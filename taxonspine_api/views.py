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

class TaxonViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for editing or viewing a taxon
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = Taxon.objects.all()
    serializer_class = TaxonSerializer