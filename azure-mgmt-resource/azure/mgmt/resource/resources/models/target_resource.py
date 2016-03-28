# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TargetResource(Model):
    """
    Target resource.

    :param id: Gets or sets the ID of the resource.
    :type id: str
    :param resource_name: Gets or sets the name of the resource.
    :type resource_name: str
    :param resource_type: Gets or sets the type of the resource.
    :type resource_type: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'resource_name': {'key': 'resourceName', 'type': 'str'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
    }

    def __init__(self, id=None, resource_name=None, resource_type=None, **kwargs):
        self.id = id
        self.resource_name = resource_name
        self.resource_type = resource_type
