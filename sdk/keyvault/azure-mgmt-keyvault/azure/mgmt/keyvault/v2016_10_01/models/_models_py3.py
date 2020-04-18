# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

import msrest.serialization


class AccessPolicyEntry(msrest.serialization.Model):
    """An identity that have access to the key vault. All identities in the array must use the same tenant ID as the key vault's tenant ID.

    All required parameters must be populated in order to send to Azure.

    :param tenant_id: Required. The Azure Active Directory tenant ID that should be used for
     authenticating requests to the key vault.
    :type tenant_id: str
    :param object_id: Required. The object ID of a user, service principal or security group in the
     Azure Active Directory tenant for the vault. The object ID must be unique for the list of
     access policies.
    :type object_id: str
    :param application_id: Application ID of the client making request on behalf of a principal.
    :type application_id: str
    :param permissions: Required. Permissions the identity has for keys, secrets and certificates.
    :type permissions: ~azure.mgmt.keyvault.v2016_10_01.models.Permissions
    """

    _validation = {
        'tenant_id': {'required': True},
        'object_id': {'required': True},
        'permissions': {'required': True},
    }

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'application_id': {'key': 'applicationId', 'type': 'str'},
        'permissions': {'key': 'permissions', 'type': 'Permissions'},
    }

    def __init__(
        self,
        *,
        tenant_id: str,
        object_id: str,
        permissions: "Permissions",
        application_id: Optional[str] = None,
        **kwargs
    ):
        super(AccessPolicyEntry, self).__init__(**kwargs)
        self.tenant_id = tenant_id
        self.object_id = object_id
        self.application_id = application_id
        self.permissions = permissions


class CheckNameAvailabilityResult(msrest.serialization.Model):
    """The CheckNameAvailability operation response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name_available: A boolean value that indicates whether the name is available for you to
     use. If true, the name is available. If false, the name has already been taken or is invalid
     and cannot be used.
    :vartype name_available: bool
    :ivar reason: The reason that a vault name could not be used. The Reason element is only
     returned if NameAvailable is false. Possible values include: 'AccountNameInvalid',
     'AlreadyExists'.
    :vartype reason: str or ~azure.mgmt.keyvault.v2016_10_01.models.Reason
    :ivar message: An error message explaining the Reason value in more detail.
    :vartype message: str
    """

    _validation = {
        'name_available': {'readonly': True},
        'reason': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CheckNameAvailabilityResult, self).__init__(**kwargs)
        self.name_available = None
        self.reason = None
        self.message = None


class DeletedVault(msrest.serialization.Model):
    """Deleted vault information with extended details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The resource ID for the deleted key vault.
    :vartype id: str
    :ivar name: The name of the key vault.
    :vartype name: str
    :ivar type: The resource type of the key vault.
    :vartype type: str
    :param properties: Properties of the vault.
    :type properties: ~azure.mgmt.keyvault.v2016_10_01.models.DeletedVaultProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'DeletedVaultProperties'},
    }

    def __init__(
        self,
        *,
        properties: Optional["DeletedVaultProperties"] = None,
        **kwargs
    ):
        super(DeletedVault, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.properties = properties


class DeletedVaultListResult(msrest.serialization.Model):
    """List of vaults.

    :param value: The list of deleted vaults.
    :type value: list[~azure.mgmt.keyvault.v2016_10_01.models.DeletedVault]
    :param next_link: The URL to get the next set of deleted vaults.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DeletedVault]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["DeletedVault"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(DeletedVaultListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class DeletedVaultProperties(msrest.serialization.Model):
    """Properties of the deleted vault.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar vault_id: The resource id of the original vault.
    :vartype vault_id: str
    :ivar location: The location of the original vault.
    :vartype location: str
    :ivar deletion_date: The deleted date.
    :vartype deletion_date: ~datetime.datetime
    :ivar scheduled_purge_date: The scheduled purged date.
    :vartype scheduled_purge_date: ~datetime.datetime
    :ivar tags: A set of tags. Tags of the original vault.
    :vartype tags: dict[str, str]
    """

    _validation = {
        'vault_id': {'readonly': True},
        'location': {'readonly': True},
        'deletion_date': {'readonly': True},
        'scheduled_purge_date': {'readonly': True},
        'tags': {'readonly': True},
    }

    _attribute_map = {
        'vault_id': {'key': 'vaultId', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'deletion_date': {'key': 'deletionDate', 'type': 'iso-8601'},
        'scheduled_purge_date': {'key': 'scheduledPurgeDate', 'type': 'iso-8601'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DeletedVaultProperties, self).__init__(**kwargs)
        self.vault_id = None
        self.location = None
        self.deletion_date = None
        self.scheduled_purge_date = None
        self.tags = None


class LogSpecification(msrest.serialization.Model):
    """Log specification of operation.

    :param name: Name of log specification.
    :type name: str
    :param display_name: Display name of log specification.
    :type display_name: str
    :param blob_duration: Blob duration of specification.
    :type blob_duration: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'blob_duration': {'key': 'blobDuration', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display_name: Optional[str] = None,
        blob_duration: Optional[str] = None,
        **kwargs
    ):
        super(LogSpecification, self).__init__(**kwargs)
        self.name = name
        self.display_name = display_name
        self.blob_duration = blob_duration


class Operation(msrest.serialization.Model):
    """Key Vault REST API operation definition.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: Display metadata associated with the operation.
    :type display: ~azure.mgmt.keyvault.v2016_10_01.models.OperationDisplay
    :param origin: The origin of operations.
    :type origin: str
    :param service_specification: One property of operation, include metric specifications.
    :type service_specification: ~azure.mgmt.keyvault.v2016_10_01.models.ServiceSpecification
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
        'service_specification': {'key': 'properties.serviceSpecification', 'type': 'ServiceSpecification'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["OperationDisplay"] = None,
        origin: Optional[str] = None,
        service_specification: Optional["ServiceSpecification"] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.origin = origin
        self.service_specification = service_specification


class OperationDisplay(msrest.serialization.Model):
    """Display metadata associated with the operation.

    :param provider: Service provider: Microsoft Key Vault.
    :type provider: str
    :param resource: Resource on which the operation is performed etc.
    :type resource: str
    :param operation: Type of operation: get, read, delete, etc.
    :type operation: str
    :param description: Description of operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationListResult(msrest.serialization.Model):
    """Result of the request to list Storage operations. It contains a list of operations and a URL link to get the next set of results.

    :param value: List of Storage operations supported by the Storage resource provider.
    :type value: list[~azure.mgmt.keyvault.v2016_10_01.models.Operation]
    :param next_link: The URL to get the next set of operations.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Operation"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class Permissions(msrest.serialization.Model):
    """Permissions the identity has for keys, secrets, certificates and storage.

    :param keys: Permissions to keys.
    :type keys: list[str or ~azure.mgmt.keyvault.v2016_10_01.models.KeyPermissions]
    :param secrets: Permissions to secrets.
    :type secrets: list[str or ~azure.mgmt.keyvault.v2016_10_01.models.SecretPermissions]
    :param certificates: Permissions to certificates.
    :type certificates: list[str or ~azure.mgmt.keyvault.v2016_10_01.models.CertificatePermissions]
    :param storage: Permissions to storage accounts.
    :type storage: list[str or ~azure.mgmt.keyvault.v2016_10_01.models.StoragePermissions]
    """

    _attribute_map = {
        'keys': {'key': 'keys', 'type': '[str]'},
        'secrets': {'key': 'secrets', 'type': '[str]'},
        'certificates': {'key': 'certificates', 'type': '[str]'},
        'storage': {'key': 'storage', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        keys: Optional[List[Union[str, "KeyPermissions"]]] = None,
        secrets: Optional[List[Union[str, "SecretPermissions"]]] = None,
        certificates: Optional[List[Union[str, "CertificatePermissions"]]] = None,
        storage: Optional[List[Union[str, "StoragePermissions"]]] = None,
        **kwargs
    ):
        super(Permissions, self).__init__(**kwargs)
        self.keys = keys
        self.secrets = secrets
        self.certificates = certificates
        self.storage = storage


class Resource(msrest.serialization.Model):
    """Key Vault resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The Azure Resource Manager resource ID for the key vault.
    :vartype id: str
    :ivar name: The name of the key vault.
    :vartype name: str
    :ivar type: The resource type of the key vault.
    :vartype type: str
    :param location: Required. The supported Azure location where the key vault should be created.
    :type location: str
    :param tags: A set of tags. The tags that will be assigned to the key vault.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class ResourceListResult(msrest.serialization.Model):
    """List of vault resources.

    :param value: The list of vault resources.
    :type value: list[~azure.mgmt.keyvault.v2016_10_01.models.Resource]
    :param next_link: The URL to get the next set of vault resources.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Resource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Resource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ResourceListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ServiceSpecification(msrest.serialization.Model):
    """One property of operation, include log specifications.

    :param log_specifications: Log specifications of operation.
    :type log_specifications: list[~azure.mgmt.keyvault.v2016_10_01.models.LogSpecification]
    """

    _attribute_map = {
        'log_specifications': {'key': 'logSpecifications', 'type': '[LogSpecification]'},
    }

    def __init__(
        self,
        *,
        log_specifications: Optional[List["LogSpecification"]] = None,
        **kwargs
    ):
        super(ServiceSpecification, self).__init__(**kwargs)
        self.log_specifications = log_specifications


class Sku(msrest.serialization.Model):
    """SKU details.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar family: Required. SKU family name. Default value: "A".
    :vartype family: str
    :param name: Required. SKU name to specify whether the key vault is a standard vault or a
     premium vault. Possible values include: 'standard', 'premium'.
    :type name: str or ~azure.mgmt.keyvault.v2016_10_01.models.SkuName
    """

    _validation = {
        'family': {'required': True, 'constant': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'family': {'key': 'family', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    family = "A"

    def __init__(
        self,
        *,
        name: Union[str, "SkuName"],
        **kwargs
    ):
        super(Sku, self).__init__(**kwargs)
        self.name = name


class Vault(Resource):
    """Resource information with extended details.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The Azure Resource Manager resource ID for the key vault.
    :vartype id: str
    :ivar name: The name of the key vault.
    :vartype name: str
    :ivar type: The resource type of the key vault.
    :vartype type: str
    :param location: Required. The supported Azure location where the key vault should be created.
    :type location: str
    :param tags: A set of tags. The tags that will be assigned to the key vault.
    :type tags: dict[str, str]
    :param properties: Required. Properties of the vault.
    :type properties: ~azure.mgmt.keyvault.v2016_10_01.models.VaultProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'VaultProperties'},
    }

    def __init__(
        self,
        *,
        location: str,
        properties: "VaultProperties",
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(Vault, self).__init__(location=location, tags=tags, **kwargs)
        self.properties = properties


class VaultAccessPolicyParameters(msrest.serialization.Model):
    """Parameters for updating the access policy in a vault.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource id of the access policy.
    :vartype id: str
    :ivar name: The resource name of the access policy.
    :vartype name: str
    :ivar type: The resource name of the access policy.
    :vartype type: str
    :ivar location: The resource type of the access policy.
    :vartype location: str
    :param properties: Required. Properties of the access policy.
    :type properties: ~azure.mgmt.keyvault.v2016_10_01.models.VaultAccessPolicyProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'VaultAccessPolicyProperties'},
    }

    def __init__(
        self,
        *,
        properties: "VaultAccessPolicyProperties",
        **kwargs
    ):
        super(VaultAccessPolicyParameters, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = None
        self.properties = properties


class VaultAccessPolicyProperties(msrest.serialization.Model):
    """Properties of the vault access policy.

    All required parameters must be populated in order to send to Azure.

    :param access_policies: Required. An array of 0 to 16 identities that have access to the key
     vault. All identities in the array must use the same tenant ID as the key vault's tenant ID.
    :type access_policies: list[~azure.mgmt.keyvault.v2016_10_01.models.AccessPolicyEntry]
    """

    _validation = {
        'access_policies': {'required': True},
    }

    _attribute_map = {
        'access_policies': {'key': 'accessPolicies', 'type': '[AccessPolicyEntry]'},
    }

    def __init__(
        self,
        *,
        access_policies: List["AccessPolicyEntry"],
        **kwargs
    ):
        super(VaultAccessPolicyProperties, self).__init__(**kwargs)
        self.access_policies = access_policies


class VaultCheckNameAvailabilityParameters(msrest.serialization.Model):
    """The parameters used to check the availability of the vault name.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The vault name.
    :type name: str
    :ivar type: Required. The type of resource, Microsoft.KeyVault/vaults. Default value:
     "Microsoft.KeyVault/vaults".
    :vartype type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    type = "Microsoft.KeyVault/vaults"

    def __init__(
        self,
        *,
        name: str,
        **kwargs
    ):
        super(VaultCheckNameAvailabilityParameters, self).__init__(**kwargs)
        self.name = name


class VaultCreateOrUpdateParameters(msrest.serialization.Model):
    """Parameters for creating or updating a vault.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The supported Azure location where the key vault should be created.
    :type location: str
    :param tags: A set of tags. The tags that will be assigned to the key vault.
    :type tags: dict[str, str]
    :param properties: Required. Properties of the vault.
    :type properties: ~azure.mgmt.keyvault.v2016_10_01.models.VaultProperties
    """

    _validation = {
        'location': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'VaultProperties'},
    }

    def __init__(
        self,
        *,
        location: str,
        properties: "VaultProperties",
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(VaultCreateOrUpdateParameters, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.properties = properties


class VaultListResult(msrest.serialization.Model):
    """List of vaults.

    :param value: The list of vaults.
    :type value: list[~azure.mgmt.keyvault.v2016_10_01.models.Vault]
    :param next_link: The URL to get the next set of vaults.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Vault]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Vault"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(VaultListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class VaultPatchParameters(msrest.serialization.Model):
    """Parameters for creating or updating a vault.

    :param tags: A set of tags. The tags that will be assigned to the key vault.
    :type tags: dict[str, str]
    :param properties: Properties of the vault.
    :type properties: ~azure.mgmt.keyvault.v2016_10_01.models.VaultPatchProperties
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'VaultPatchProperties'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        properties: Optional["VaultPatchProperties"] = None,
        **kwargs
    ):
        super(VaultPatchParameters, self).__init__(**kwargs)
        self.tags = tags
        self.properties = properties


class VaultPatchProperties(msrest.serialization.Model):
    """Properties of the vault.

    :param tenant_id: The Azure Active Directory tenant ID that should be used for authenticating
     requests to the key vault.
    :type tenant_id: str
    :param sku: SKU details.
    :type sku: ~azure.mgmt.keyvault.v2016_10_01.models.Sku
    :param access_policies: An array of 0 to 16 identities that have access to the key vault. All
     identities in the array must use the same tenant ID as the key vault's tenant ID.
    :type access_policies: list[~azure.mgmt.keyvault.v2016_10_01.models.AccessPolicyEntry]
    :param enabled_for_deployment: Property to specify whether Azure Virtual Machines are permitted
     to retrieve certificates stored as secrets from the key vault.
    :type enabled_for_deployment: bool
    :param enabled_for_disk_encryption: Property to specify whether Azure Disk Encryption is
     permitted to retrieve secrets from the vault and unwrap keys.
    :type enabled_for_disk_encryption: bool
    :param enabled_for_template_deployment: Property to specify whether Azure Resource Manager is
     permitted to retrieve secrets from the key vault.
    :type enabled_for_template_deployment: bool
    :param enable_soft_delete: Property specifying whether recoverable deletion ('soft' delete) is
     enabled for this key vault. The property may not be set to false.
    :type enable_soft_delete: bool
    :param create_mode: The vault's create mode to indicate whether the vault need to be recovered
     or not. Possible values include: 'recover', 'default'.
    :type create_mode: str or ~azure.mgmt.keyvault.v2016_10_01.models.CreateMode
    :param enable_purge_protection: Property specifying whether protection against purge is enabled
     for this vault; it is only effective if soft delete is also enabled. Once activated, the
     property may no longer be reset to false.
    :type enable_purge_protection: bool
    """

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'access_policies': {'key': 'accessPolicies', 'type': '[AccessPolicyEntry]'},
        'enabled_for_deployment': {'key': 'enabledForDeployment', 'type': 'bool'},
        'enabled_for_disk_encryption': {'key': 'enabledForDiskEncryption', 'type': 'bool'},
        'enabled_for_template_deployment': {'key': 'enabledForTemplateDeployment', 'type': 'bool'},
        'enable_soft_delete': {'key': 'enableSoftDelete', 'type': 'bool'},
        'create_mode': {'key': 'createMode', 'type': 'str'},
        'enable_purge_protection': {'key': 'enablePurgeProtection', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        tenant_id: Optional[str] = None,
        sku: Optional["Sku"] = None,
        access_policies: Optional[List["AccessPolicyEntry"]] = None,
        enabled_for_deployment: Optional[bool] = None,
        enabled_for_disk_encryption: Optional[bool] = None,
        enabled_for_template_deployment: Optional[bool] = None,
        enable_soft_delete: Optional[bool] = None,
        create_mode: Optional[Union[str, "CreateMode"]] = None,
        enable_purge_protection: Optional[bool] = None,
        **kwargs
    ):
        super(VaultPatchProperties, self).__init__(**kwargs)
        self.tenant_id = tenant_id
        self.sku = sku
        self.access_policies = access_policies
        self.enabled_for_deployment = enabled_for_deployment
        self.enabled_for_disk_encryption = enabled_for_disk_encryption
        self.enabled_for_template_deployment = enabled_for_template_deployment
        self.enable_soft_delete = enable_soft_delete
        self.create_mode = create_mode
        self.enable_purge_protection = enable_purge_protection


class VaultProperties(msrest.serialization.Model):
    """Properties of the vault.

    All required parameters must be populated in order to send to Azure.

    :param tenant_id: Required. The Azure Active Directory tenant ID that should be used for
     authenticating requests to the key vault.
    :type tenant_id: str
    :param sku: Required. SKU details.
    :type sku: ~azure.mgmt.keyvault.v2016_10_01.models.Sku
    :param access_policies: An array of 0 to 16 identities that have access to the key vault. All
     identities in the array must use the same tenant ID as the key vault's tenant ID. When
     ``createMode`` is set to ``recover``\ , access policies are not required. Otherwise, access
     policies are required.
    :type access_policies: list[~azure.mgmt.keyvault.v2016_10_01.models.AccessPolicyEntry]
    :param vault_uri: The URI of the vault for performing operations on keys and secrets.
    :type vault_uri: str
    :param enabled_for_deployment: Property to specify whether Azure Virtual Machines are permitted
     to retrieve certificates stored as secrets from the key vault.
    :type enabled_for_deployment: bool
    :param enabled_for_disk_encryption: Property to specify whether Azure Disk Encryption is
     permitted to retrieve secrets from the vault and unwrap keys.
    :type enabled_for_disk_encryption: bool
    :param enabled_for_template_deployment: Property to specify whether Azure Resource Manager is
     permitted to retrieve secrets from the key vault.
    :type enabled_for_template_deployment: bool
    :param enable_soft_delete: Property specifying whether recoverable deletion is enabled for this
     key vault. Setting this property to true activates the soft delete feature, whereby vaults or
     vault entities can be recovered after deletion. Enabling this functionality is irreversible -
     that is, the property does not accept false as its value.
    :type enable_soft_delete: bool
    :param create_mode: The vault's create mode to indicate whether the vault need to be recovered
     or not. Possible values include: 'recover', 'default'.
    :type create_mode: str or ~azure.mgmt.keyvault.v2016_10_01.models.CreateMode
    :param enable_purge_protection: Property specifying whether protection against purge is enabled
     for this vault. Setting this property to true activates protection against purge for this vault
     and its content - only the Key Vault service may initiate a hard, irrecoverable deletion. The
     setting is effective only if soft delete is also enabled. Enabling this functionality is
     irreversible - that is, the property does not accept false as its value.
    :type enable_purge_protection: bool
    """

    _validation = {
        'tenant_id': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'access_policies': {'key': 'accessPolicies', 'type': '[AccessPolicyEntry]'},
        'vault_uri': {'key': 'vaultUri', 'type': 'str'},
        'enabled_for_deployment': {'key': 'enabledForDeployment', 'type': 'bool'},
        'enabled_for_disk_encryption': {'key': 'enabledForDiskEncryption', 'type': 'bool'},
        'enabled_for_template_deployment': {'key': 'enabledForTemplateDeployment', 'type': 'bool'},
        'enable_soft_delete': {'key': 'enableSoftDelete', 'type': 'bool'},
        'create_mode': {'key': 'createMode', 'type': 'str'},
        'enable_purge_protection': {'key': 'enablePurgeProtection', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        tenant_id: str,
        sku: "Sku",
        access_policies: Optional[List["AccessPolicyEntry"]] = None,
        vault_uri: Optional[str] = None,
        enabled_for_deployment: Optional[bool] = None,
        enabled_for_disk_encryption: Optional[bool] = None,
        enabled_for_template_deployment: Optional[bool] = None,
        enable_soft_delete: Optional[bool] = None,
        create_mode: Optional[Union[str, "CreateMode"]] = None,
        enable_purge_protection: Optional[bool] = None,
        **kwargs
    ):
        super(VaultProperties, self).__init__(**kwargs)
        self.tenant_id = tenant_id
        self.sku = sku
        self.access_policies = access_policies
        self.vault_uri = vault_uri
        self.enabled_for_deployment = enabled_for_deployment
        self.enabled_for_disk_encryption = enabled_for_disk_encryption
        self.enabled_for_template_deployment = enabled_for_template_deployment
        self.enable_soft_delete = enable_soft_delete
        self.create_mode = create_mode
        self.enable_purge_protection = enable_purge_protection
