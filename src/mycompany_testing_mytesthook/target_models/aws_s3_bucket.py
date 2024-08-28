# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass

from cloudformation_cli_python_lib.interface import BaseModel
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

import sys
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class AwsS3Bucket(BaseModel):
    InventoryConfigurations: Optional[Sequence["_InventoryConfiguration"]]
    WebsiteConfiguration: Optional["_WebsiteConfiguration"]
    DualStackDomainName: Optional[str]
    AccessControl: Optional[str]
    AnalyticsConfigurations: Optional[Sequence["_AnalyticsConfiguration"]]
    AccelerateConfiguration: Optional["_AccelerateConfiguration"]
    PublicAccessBlockConfiguration: Optional["_PublicAccessBlockConfiguration"]
    BucketName: Optional[str]
    RegionalDomainName: Optional[str]
    OwnershipControls: Optional["_OwnershipControls"]
    ObjectLockConfiguration: Optional["_ObjectLockConfiguration"]
    ObjectLockEnabled: Optional[bool]
    LoggingConfiguration: Optional["_LoggingConfiguration"]
    ReplicationConfiguration: Optional["_ReplicationConfiguration"]
    Tags: Optional[Any]
    DomainName: Optional[str]
    BucketEncryption: Optional["_BucketEncryption"]
    WebsiteURL: Optional[str]
    NotificationConfiguration: Optional["_NotificationConfiguration"]
    LifecycleConfiguration: Optional["_LifecycleConfiguration"]
    VersioningConfiguration: Optional["_VersioningConfiguration"]
    MetricsConfigurations: Optional[Sequence["_MetricsConfiguration"]]
    IntelligentTieringConfigurations: Optional[
        Sequence["_IntelligentTieringConfiguration"]
    ]
    CorsConfiguration: Optional["_CorsConfiguration"]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsS3Bucket"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsS3Bucket"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            InventoryConfigurations=deserialize_list(
                json_data.get("InventoryConfigurations"), InventoryConfiguration
            ),
            WebsiteConfiguration=WebsiteConfiguration._deserialize(
                json_data.get("WebsiteConfiguration")
            ),
            DualStackDomainName=json_data.get("DualStackDomainName"),
            AccessControl=json_data.get("AccessControl"),
            AnalyticsConfigurations=deserialize_list(
                json_data.get("AnalyticsConfigurations"), AnalyticsConfiguration
            ),
            AccelerateConfiguration=AccelerateConfiguration._deserialize(
                json_data.get("AccelerateConfiguration")
            ),
            PublicAccessBlockConfiguration=PublicAccessBlockConfiguration._deserialize(
                json_data.get("PublicAccessBlockConfiguration")
            ),
            BucketName=json_data.get("BucketName"),
            RegionalDomainName=json_data.get("RegionalDomainName"),
            OwnershipControls=OwnershipControls._deserialize(
                json_data.get("OwnershipControls")
            ),
            ObjectLockConfiguration=ObjectLockConfiguration._deserialize(
                json_data.get("ObjectLockConfiguration")
            ),
            ObjectLockEnabled=json_data.get("ObjectLockEnabled"),
            LoggingConfiguration=LoggingConfiguration._deserialize(
                json_data.get("LoggingConfiguration")
            ),
            ReplicationConfiguration=ReplicationConfiguration._deserialize(
                json_data.get("ReplicationConfiguration")
            ),
            Tags=json_data.get("Tags"),
            DomainName=json_data.get("DomainName"),
            BucketEncryption=BucketEncryption._deserialize(
                json_data.get("BucketEncryption")
            ),
            WebsiteURL=json_data.get("WebsiteURL"),
            NotificationConfiguration=NotificationConfiguration._deserialize(
                json_data.get("NotificationConfiguration")
            ),
            LifecycleConfiguration=LifecycleConfiguration._deserialize(
                json_data.get("LifecycleConfiguration")
            ),
            VersioningConfiguration=VersioningConfiguration._deserialize(
                json_data.get("VersioningConfiguration")
            ),
            MetricsConfigurations=deserialize_list(
                json_data.get("MetricsConfigurations"), MetricsConfiguration
            ),
            IntelligentTieringConfigurations=deserialize_list(
                json_data.get("IntelligentTieringConfigurations"),
                IntelligentTieringConfiguration,
            ),
            CorsConfiguration=CorsConfiguration._deserialize(
                json_data.get("CorsConfiguration")
            ),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsS3Bucket = AwsS3Bucket


@dataclass
class InventoryConfiguration(BaseModel):
    Destination: Optional["_Destination"]
    OptionalFields: Optional[Sequence[str]]
    IncludedObjectVersions: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Prefix: Optional[str]
    ScheduleFrequency: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InventoryConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InventoryConfiguration"]:
        if not json_data:
            return None
        return cls(
            Destination=Destination._deserialize(json_data.get("Destination")),
            OptionalFields=json_data.get("OptionalFields"),
            IncludedObjectVersions=json_data.get("IncludedObjectVersions"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            ScheduleFrequency=json_data.get("ScheduleFrequency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InventoryConfiguration = InventoryConfiguration


@dataclass
class Destination(BaseModel):
    BucketArn: Optional[str]
    Format: Optional[str]
    BucketAccountId: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Destination"]:
        if not json_data:
            return None
        return cls(
            BucketArn=json_data.get("BucketArn"),
            Format=json_data.get("Format"),
            BucketAccountId=json_data.get("BucketAccountId"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Destination = Destination


@dataclass
class WebsiteConfiguration(BaseModel):
    IndexDocument: Optional[str]
    RedirectAllRequestsTo: Optional["_RedirectAllRequestsTo"]
    RoutingRules: Optional[Sequence["_RoutingRule"]]
    ErrorDocument: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebsiteConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebsiteConfiguration"]:
        if not json_data:
            return None
        return cls(
            IndexDocument=json_data.get("IndexDocument"),
            RedirectAllRequestsTo=RedirectAllRequestsTo._deserialize(
                json_data.get("RedirectAllRequestsTo")
            ),
            RoutingRules=deserialize_list(json_data.get("RoutingRules"), RoutingRule),
            ErrorDocument=json_data.get("ErrorDocument"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebsiteConfiguration = WebsiteConfiguration


@dataclass
class RedirectAllRequestsTo(BaseModel):
    Protocol: Optional[str]
    HostName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectAllRequestsTo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectAllRequestsTo"]:
        if not json_data:
            return None
        return cls(
            Protocol=json_data.get("Protocol"),
            HostName=json_data.get("HostName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectAllRequestsTo = RedirectAllRequestsTo


@dataclass
class RoutingRule(BaseModel):
    RedirectRule: Optional["_RedirectRule"]
    RoutingRuleCondition: Optional["_RoutingRuleCondition"]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingRule"]:
        if not json_data:
            return None
        return cls(
            RedirectRule=RedirectRule._deserialize(json_data.get("RedirectRule")),
            RoutingRuleCondition=RoutingRuleCondition._deserialize(
                json_data.get("RoutingRuleCondition")
            ),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingRule = RoutingRule


@dataclass
class RedirectRule(BaseModel):
    ReplaceKeyWith: Optional[str]
    HttpRedirectCode: Optional[str]
    Protocol: Optional[str]
    HostName: Optional[str]
    ReplaceKeyPrefixWith: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectRule"]:
        if not json_data:
            return None
        return cls(
            ReplaceKeyWith=json_data.get("ReplaceKeyWith"),
            HttpRedirectCode=json_data.get("HttpRedirectCode"),
            Protocol=json_data.get("Protocol"),
            HostName=json_data.get("HostName"),
            ReplaceKeyPrefixWith=json_data.get("ReplaceKeyPrefixWith"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectRule = RedirectRule


@dataclass
class RoutingRuleCondition(BaseModel):
    KeyPrefixEquals: Optional[str]
    HttpErrorCodeReturnedEquals: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingRuleCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingRuleCondition"]:
        if not json_data:
            return None
        return cls(
            KeyPrefixEquals=json_data.get("KeyPrefixEquals"),
            HttpErrorCodeReturnedEquals=json_data.get("HttpErrorCodeReturnedEquals"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingRuleCondition = RoutingRuleCondition


@dataclass
class AnalyticsConfiguration(BaseModel):
    StorageClassAnalysis: Optional["_StorageClassAnalysis"]
    TagFilters: Optional[Sequence["_TagFilter"]]
    Id: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnalyticsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalyticsConfiguration"]:
        if not json_data:
            return None
        return cls(
            StorageClassAnalysis=StorageClassAnalysis._deserialize(
                json_data.get("StorageClassAnalysis")
            ),
            TagFilters=deserialize_list(json_data.get("TagFilters"), TagFilter),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalyticsConfiguration = AnalyticsConfiguration


@dataclass
class StorageClassAnalysis(BaseModel):
    DataExport: Optional["_DataExport"]

    @classmethod
    def _deserialize(
        cls: Type["_StorageClassAnalysis"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageClassAnalysis"]:
        if not json_data:
            return None
        return cls(
            DataExport=DataExport._deserialize(json_data.get("DataExport")),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageClassAnalysis = StorageClassAnalysis


@dataclass
class DataExport(BaseModel):
    Destination: Optional["_Destination"]
    OutputSchemaVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataExport"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataExport"]:
        if not json_data:
            return None
        return cls(
            Destination=Destination._deserialize(json_data.get("Destination")),
            OutputSchemaVersion=json_data.get("OutputSchemaVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataExport = DataExport


@dataclass
class TagFilter(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagFilter"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagFilter = TagFilter


@dataclass
class AccelerateConfiguration(BaseModel):
    AccelerationStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccelerateConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccelerateConfiguration"]:
        if not json_data:
            return None
        return cls(
            AccelerationStatus=json_data.get("AccelerationStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccelerateConfiguration = AccelerateConfiguration


@dataclass
class PublicAccessBlockConfiguration(BaseModel):
    RestrictPublicBuckets: Optional[bool]
    BlockPublicPolicy: Optional[bool]
    BlockPublicAcls: Optional[bool]
    IgnorePublicAcls: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PublicAccessBlockConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicAccessBlockConfiguration"]:
        if not json_data:
            return None
        return cls(
            RestrictPublicBuckets=json_data.get("RestrictPublicBuckets"),
            BlockPublicPolicy=json_data.get("BlockPublicPolicy"),
            BlockPublicAcls=json_data.get("BlockPublicAcls"),
            IgnorePublicAcls=json_data.get("IgnorePublicAcls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicAccessBlockConfiguration = PublicAccessBlockConfiguration


@dataclass
class OwnershipControls(BaseModel):
    Rules: Optional[Sequence["_OwnershipControlsRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_OwnershipControls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnershipControls"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), OwnershipControlsRule),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnershipControls = OwnershipControls


@dataclass
class OwnershipControlsRule(BaseModel):
    ObjectOwnership: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnershipControlsRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnershipControlsRule"]:
        if not json_data:
            return None
        return cls(
            ObjectOwnership=json_data.get("ObjectOwnership"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnershipControlsRule = OwnershipControlsRule


@dataclass
class ObjectLockConfiguration(BaseModel):
    ObjectLockEnabled: Optional[str]
    Rule: Optional["_ObjectLockRule"]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectLockConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectLockConfiguration"]:
        if not json_data:
            return None
        return cls(
            ObjectLockEnabled=json_data.get("ObjectLockEnabled"),
            Rule=ObjectLockRule._deserialize(json_data.get("Rule")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectLockConfiguration = ObjectLockConfiguration


@dataclass
class ObjectLockRule(BaseModel):
    DefaultRetention: Optional["_DefaultRetention"]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectLockRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectLockRule"]:
        if not json_data:
            return None
        return cls(
            DefaultRetention=DefaultRetention._deserialize(
                json_data.get("DefaultRetention")
            ),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectLockRule = ObjectLockRule


@dataclass
class DefaultRetention(BaseModel):
    Years: Optional[int]
    Days: Optional[int]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultRetention"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultRetention"]:
        if not json_data:
            return None
        return cls(
            Years=json_data.get("Years"),
            Days=json_data.get("Days"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultRetention = DefaultRetention


@dataclass
class LoggingConfiguration(BaseModel):
    TargetObjectKeyFormat: Optional["_TargetObjectKeyFormat"]
    LogFilePrefix: Optional[str]
    DestinationBucketName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfiguration"]:
        if not json_data:
            return None
        return cls(
            TargetObjectKeyFormat=TargetObjectKeyFormat._deserialize(
                json_data.get("TargetObjectKeyFormat")
            ),
            LogFilePrefix=json_data.get("LogFilePrefix"),
            DestinationBucketName=json_data.get("DestinationBucketName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfiguration = LoggingConfiguration


@dataclass
class TargetObjectKeyFormat(BaseModel):
    SimplePrefix: Optional[MutableMapping[str, Any]]
    PartitionedPrefix: Optional["_PartitionedPrefix"]

    @classmethod
    def _deserialize(
        cls: Type["_TargetObjectKeyFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetObjectKeyFormat"]:
        if not json_data:
            return None
        return cls(
            SimplePrefix=json_data.get("SimplePrefix"),
            PartitionedPrefix=PartitionedPrefix._deserialize(
                json_data.get("PartitionedPrefix")
            ),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetObjectKeyFormat = TargetObjectKeyFormat


@dataclass
class PartitionedPrefix(BaseModel):
    PartitionDateSource: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PartitionedPrefix"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PartitionedPrefix"]:
        if not json_data:
            return None
        return cls(
            PartitionDateSource=json_data.get("PartitionDateSource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PartitionedPrefix = PartitionedPrefix


@dataclass
class ReplicationConfiguration(BaseModel):
    Role: Optional[str]
    Rules: Optional[Sequence["_ReplicationRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationConfiguration"]:
        if not json_data:
            return None
        return cls(
            Role=json_data.get("Role"),
            Rules=deserialize_list(json_data.get("Rules"), ReplicationRule),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationConfiguration = ReplicationConfiguration


@dataclass
class ReplicationRule(BaseModel):
    Status: Optional[str]
    Destination: Optional["_ReplicationDestination"]
    Filter: Optional["_ReplicationRuleFilter"]
    Priority: Optional[int]
    SourceSelectionCriteria: Optional["_SourceSelectionCriteria"]
    Id: Optional[str]
    Prefix: Optional[str]
    DeleteMarkerReplication: Optional["_DeleteMarkerReplication"]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationRule"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            Destination=ReplicationDestination._deserialize(
                json_data.get("Destination")
            ),
            Filter=ReplicationRuleFilter._deserialize(json_data.get("Filter")),
            Priority=json_data.get("Priority"),
            SourceSelectionCriteria=SourceSelectionCriteria._deserialize(
                json_data.get("SourceSelectionCriteria")
            ),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            DeleteMarkerReplication=DeleteMarkerReplication._deserialize(
                json_data.get("DeleteMarkerReplication")
            ),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationRule = ReplicationRule


@dataclass
class ReplicationDestination(BaseModel):
    AccessControlTranslation: Optional["_AccessControlTranslation"]
    Account: Optional[str]
    Metrics: Optional["_Metrics"]
    Bucket: Optional[str]
    EncryptionConfiguration: Optional["_EncryptionConfiguration"]
    StorageClass: Optional[str]
    ReplicationTime: Optional["_ReplicationTime"]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationDestination"]:
        if not json_data:
            return None
        return cls(
            AccessControlTranslation=AccessControlTranslation._deserialize(
                json_data.get("AccessControlTranslation")
            ),
            Account=json_data.get("Account"),
            Metrics=Metrics._deserialize(json_data.get("Metrics")),
            Bucket=json_data.get("Bucket"),
            EncryptionConfiguration=EncryptionConfiguration._deserialize(
                json_data.get("EncryptionConfiguration")
            ),
            StorageClass=json_data.get("StorageClass"),
            ReplicationTime=ReplicationTime._deserialize(
                json_data.get("ReplicationTime")
            ),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationDestination = ReplicationDestination


@dataclass
class AccessControlTranslation(BaseModel):
    Owner: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessControlTranslation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessControlTranslation"]:
        if not json_data:
            return None
        return cls(
            Owner=json_data.get("Owner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessControlTranslation = AccessControlTranslation


@dataclass
class Metrics(BaseModel):
    Status: Optional[str]
    EventThreshold: Optional["_ReplicationTimeValue"]

    @classmethod
    def _deserialize(
        cls: Type["_Metrics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metrics"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            EventThreshold=ReplicationTimeValue._deserialize(
                json_data.get("EventThreshold")
            ),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metrics = Metrics


@dataclass
class ReplicationTimeValue(BaseModel):
    Minutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationTimeValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationTimeValue"]:
        if not json_data:
            return None
        return cls(
            Minutes=json_data.get("Minutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationTimeValue = ReplicationTimeValue


@dataclass
class EncryptionConfiguration(BaseModel):
    ReplicaKmsKeyID: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            ReplicaKmsKeyID=json_data.get("ReplicaKmsKeyID"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfiguration = EncryptionConfiguration


@dataclass
class ReplicationTime(BaseModel):
    Status: Optional[str]
    Time: Optional["_ReplicationTimeValue"]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationTime"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationTime"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            Time=ReplicationTimeValue._deserialize(json_data.get("Time")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationTime = ReplicationTime


@dataclass
class ReplicationRuleFilter(BaseModel):
    And: Optional["_ReplicationRuleAndOperator"]
    TagFilter: Optional["_TagFilter"]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationRuleFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationRuleFilter"]:
        if not json_data:
            return None
        return cls(
            And=ReplicationRuleAndOperator._deserialize(json_data.get("And")),
            TagFilter=TagFilter._deserialize(json_data.get("TagFilter")),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationRuleFilter = ReplicationRuleFilter


@dataclass
class ReplicationRuleAndOperator(BaseModel):
    TagFilters: Optional[Sequence["_TagFilter"]]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationRuleAndOperator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationRuleAndOperator"]:
        if not json_data:
            return None
        return cls(
            TagFilters=deserialize_list(json_data.get("TagFilters"), TagFilter),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationRuleAndOperator = ReplicationRuleAndOperator


@dataclass
class SourceSelectionCriteria(BaseModel):
    ReplicaModifications: Optional["_ReplicaModifications"]
    SseKmsEncryptedObjects: Optional["_SseKmsEncryptedObjects"]

    @classmethod
    def _deserialize(
        cls: Type["_SourceSelectionCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceSelectionCriteria"]:
        if not json_data:
            return None
        return cls(
            ReplicaModifications=ReplicaModifications._deserialize(
                json_data.get("ReplicaModifications")
            ),
            SseKmsEncryptedObjects=SseKmsEncryptedObjects._deserialize(
                json_data.get("SseKmsEncryptedObjects")
            ),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceSelectionCriteria = SourceSelectionCriteria


@dataclass
class ReplicaModifications(BaseModel):
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicaModifications"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicaModifications"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicaModifications = ReplicaModifications


@dataclass
class SseKmsEncryptedObjects(BaseModel):
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SseKmsEncryptedObjects"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SseKmsEncryptedObjects"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SseKmsEncryptedObjects = SseKmsEncryptedObjects


@dataclass
class DeleteMarkerReplication(BaseModel):
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeleteMarkerReplication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeleteMarkerReplication"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeleteMarkerReplication = DeleteMarkerReplication


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


@dataclass
class BucketEncryption(BaseModel):
    ServerSideEncryptionConfiguration: Optional[Sequence["_ServerSideEncryptionRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_BucketEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BucketEncryption"]:
        if not json_data:
            return None
        return cls(
            ServerSideEncryptionConfiguration=deserialize_list(
                json_data.get("ServerSideEncryptionConfiguration"),
                ServerSideEncryptionRule,
            ),
        )


# work around possible type aliasing issues when variable has same name as a model
_BucketEncryption = BucketEncryption


@dataclass
class ServerSideEncryptionRule(BaseModel):
    BucketKeyEnabled: Optional[bool]
    ServerSideEncryptionByDefault: Optional["_ServerSideEncryptionByDefault"]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryptionRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryptionRule"]:
        if not json_data:
            return None
        return cls(
            BucketKeyEnabled=json_data.get("BucketKeyEnabled"),
            ServerSideEncryptionByDefault=ServerSideEncryptionByDefault._deserialize(
                json_data.get("ServerSideEncryptionByDefault")
            ),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryptionRule = ServerSideEncryptionRule


@dataclass
class ServerSideEncryptionByDefault(BaseModel):
    SSEAlgorithm: Optional[str]
    KMSMasterKeyID: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryptionByDefault"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryptionByDefault"]:
        if not json_data:
            return None
        return cls(
            SSEAlgorithm=json_data.get("SSEAlgorithm"),
            KMSMasterKeyID=json_data.get("KMSMasterKeyID"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryptionByDefault = ServerSideEncryptionByDefault


@dataclass
class NotificationConfiguration(BaseModel):
    TopicConfigurations: Optional[Sequence["_TopicConfiguration"]]
    QueueConfigurations: Optional[Sequence["_QueueConfiguration"]]
    LambdaConfigurations: Optional[Sequence["_LambdaConfiguration"]]
    EventBridgeConfiguration: Optional["_EventBridgeConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationConfiguration"]:
        if not json_data:
            return None
        return cls(
            TopicConfigurations=deserialize_list(
                json_data.get("TopicConfigurations"), TopicConfiguration
            ),
            QueueConfigurations=deserialize_list(
                json_data.get("QueueConfigurations"), QueueConfiguration
            ),
            LambdaConfigurations=deserialize_list(
                json_data.get("LambdaConfigurations"), LambdaConfiguration
            ),
            EventBridgeConfiguration=EventBridgeConfiguration._deserialize(
                json_data.get("EventBridgeConfiguration")
            ),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationConfiguration = NotificationConfiguration


@dataclass
class TopicConfiguration(BaseModel):
    Filter: Optional["_NotificationFilter"]
    Event: Optional[str]
    Topic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TopicConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicConfiguration"]:
        if not json_data:
            return None
        return cls(
            Filter=NotificationFilter._deserialize(json_data.get("Filter")),
            Event=json_data.get("Event"),
            Topic=json_data.get("Topic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicConfiguration = TopicConfiguration


@dataclass
class NotificationFilter(BaseModel):
    S3Key: Optional["_S3KeyFilter"]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationFilter"]:
        if not json_data:
            return None
        return cls(
            S3Key=S3KeyFilter._deserialize(json_data.get("S3Key")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationFilter = NotificationFilter


@dataclass
class S3KeyFilter(BaseModel):
    Rules: Optional[AbstractSet["_FilterRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_S3KeyFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3KeyFilter"]:
        if not json_data:
            return None
        return cls(
            Rules=set_or_none(json_data.get("Rules")),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3KeyFilter = S3KeyFilter


@dataclass
class FilterRule(BaseModel):
    Value: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterRule"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterRule = FilterRule


@dataclass
class QueueConfiguration(BaseModel):
    Filter: Optional["_NotificationFilter"]
    Event: Optional[str]
    Queue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueueConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueueConfiguration"]:
        if not json_data:
            return None
        return cls(
            Filter=NotificationFilter._deserialize(json_data.get("Filter")),
            Event=json_data.get("Event"),
            Queue=json_data.get("Queue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueueConfiguration = QueueConfiguration


@dataclass
class LambdaConfiguration(BaseModel):
    Function: Optional[str]
    Filter: Optional["_NotificationFilter"]
    Event: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaConfiguration"]:
        if not json_data:
            return None
        return cls(
            Function=json_data.get("Function"),
            Filter=NotificationFilter._deserialize(json_data.get("Filter")),
            Event=json_data.get("Event"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaConfiguration = LambdaConfiguration


@dataclass
class EventBridgeConfiguration(BaseModel):
    EventBridgeEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EventBridgeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventBridgeConfiguration"]:
        if not json_data:
            return None
        return cls(
            EventBridgeEnabled=json_data.get("EventBridgeEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventBridgeConfiguration = EventBridgeConfiguration


@dataclass
class LifecycleConfiguration(BaseModel):
    Rules: Optional[Sequence["_Rule"]]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleConfiguration"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), Rule),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleConfiguration = LifecycleConfiguration


@dataclass
class Rule(BaseModel):
    Status: Optional[str]
    ExpiredObjectDeleteMarker: Optional[bool]
    NoncurrentVersionExpirationInDays: Optional[int]
    Transitions: Optional[Sequence["_Transition"]]
    ObjectSizeGreaterThan: Optional[str]
    TagFilters: Optional[Sequence["_TagFilter"]]
    NoncurrentVersionTransitions: Optional[Sequence["_NoncurrentVersionTransition"]]
    Prefix: Optional[str]
    ObjectSizeLessThan: Optional[str]
    NoncurrentVersionTransition: Optional["_NoncurrentVersionTransition"]
    ExpirationDate: Optional[str]
    NoncurrentVersionExpiration: Optional["_NoncurrentVersionExpiration"]
    ExpirationInDays: Optional[int]
    Transition: Optional["_Transition"]
    Id: Optional[str]
    AbortIncompleteMultipartUpload: Optional["_AbortIncompleteMultipartUpload"]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            ExpiredObjectDeleteMarker=json_data.get("ExpiredObjectDeleteMarker"),
            NoncurrentVersionExpirationInDays=json_data.get(
                "NoncurrentVersionExpirationInDays"
            ),
            Transitions=deserialize_list(json_data.get("Transitions"), Transition),
            ObjectSizeGreaterThan=json_data.get("ObjectSizeGreaterThan"),
            TagFilters=deserialize_list(json_data.get("TagFilters"), TagFilter),
            NoncurrentVersionTransitions=deserialize_list(
                json_data.get("NoncurrentVersionTransitions"),
                NoncurrentVersionTransition,
            ),
            Prefix=json_data.get("Prefix"),
            ObjectSizeLessThan=json_data.get("ObjectSizeLessThan"),
            NoncurrentVersionTransition=NoncurrentVersionTransition._deserialize(
                json_data.get("NoncurrentVersionTransition")
            ),
            ExpirationDate=json_data.get("ExpirationDate"),
            NoncurrentVersionExpiration=NoncurrentVersionExpiration._deserialize(
                json_data.get("NoncurrentVersionExpiration")
            ),
            ExpirationInDays=json_data.get("ExpirationInDays"),
            Transition=Transition._deserialize(json_data.get("Transition")),
            Id=json_data.get("Id"),
            AbortIncompleteMultipartUpload=AbortIncompleteMultipartUpload._deserialize(
                json_data.get("AbortIncompleteMultipartUpload")
            ),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class Transition(BaseModel):
    TransitionDate: Optional[str]
    StorageClass: Optional[str]
    TransitionInDays: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Transition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Transition"]:
        if not json_data:
            return None
        return cls(
            TransitionDate=json_data.get("TransitionDate"),
            StorageClass=json_data.get("StorageClass"),
            TransitionInDays=json_data.get("TransitionInDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Transition = Transition


@dataclass
class NoncurrentVersionTransition(BaseModel):
    StorageClass: Optional[str]
    TransitionInDays: Optional[int]
    NewerNoncurrentVersions: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_NoncurrentVersionTransition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoncurrentVersionTransition"]:
        if not json_data:
            return None
        return cls(
            StorageClass=json_data.get("StorageClass"),
            TransitionInDays=json_data.get("TransitionInDays"),
            NewerNoncurrentVersions=json_data.get("NewerNoncurrentVersions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoncurrentVersionTransition = NoncurrentVersionTransition


@dataclass
class NoncurrentVersionExpiration(BaseModel):
    NoncurrentDays: Optional[int]
    NewerNoncurrentVersions: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_NoncurrentVersionExpiration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoncurrentVersionExpiration"]:
        if not json_data:
            return None
        return cls(
            NoncurrentDays=json_data.get("NoncurrentDays"),
            NewerNoncurrentVersions=json_data.get("NewerNoncurrentVersions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoncurrentVersionExpiration = NoncurrentVersionExpiration


@dataclass
class AbortIncompleteMultipartUpload(BaseModel):
    DaysAfterInitiation: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AbortIncompleteMultipartUpload"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AbortIncompleteMultipartUpload"]:
        if not json_data:
            return None
        return cls(
            DaysAfterInitiation=json_data.get("DaysAfterInitiation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AbortIncompleteMultipartUpload = AbortIncompleteMultipartUpload


@dataclass
class VersioningConfiguration(BaseModel):
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersioningConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersioningConfiguration"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersioningConfiguration = VersioningConfiguration


@dataclass
class MetricsConfiguration(BaseModel):
    AccessPointArn: Optional[str]
    TagFilters: Optional[Sequence["_TagFilter"]]
    Id: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricsConfiguration"]:
        if not json_data:
            return None
        return cls(
            AccessPointArn=json_data.get("AccessPointArn"),
            TagFilters=deserialize_list(json_data.get("TagFilters"), TagFilter),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricsConfiguration = MetricsConfiguration


@dataclass
class IntelligentTieringConfiguration(BaseModel):
    Status: Optional[str]
    Tierings: Optional[Sequence["_Tiering"]]
    TagFilters: Optional[Sequence["_TagFilter"]]
    Id: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IntelligentTieringConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntelligentTieringConfiguration"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            Tierings=deserialize_list(json_data.get("Tierings"), Tiering),
            TagFilters=deserialize_list(json_data.get("TagFilters"), TagFilter),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntelligentTieringConfiguration = IntelligentTieringConfiguration


@dataclass
class Tiering(BaseModel):
    AccessTier: Optional[str]
    Days: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Tiering"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tiering"]:
        if not json_data:
            return None
        return cls(
            AccessTier=json_data.get("AccessTier"),
            Days=json_data.get("Days"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tiering = Tiering


@dataclass
class CorsConfiguration(BaseModel):
    CorsRules: Optional[Sequence["_CorsRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_CorsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsConfiguration"]:
        if not json_data:
            return None
        return cls(
            CorsRules=deserialize_list(json_data.get("CorsRules"), CorsRule),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsConfiguration = CorsConfiguration


@dataclass
class CorsRule(BaseModel):
    ExposedHeaders: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
    AllowedHeaders: Optional[Sequence[str]]
    MaxAge: Optional[int]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CorsRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsRule"]:
        if not json_data:
            return None
        return cls(
            ExposedHeaders=json_data.get("ExposedHeaders"),
            AllowedMethods=json_data.get("AllowedMethods"),
            AllowedOrigins=json_data.get("AllowedOrigins"),
            AllowedHeaders=json_data.get("AllowedHeaders"),
            MaxAge=json_data.get("MaxAge"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsRule = CorsRule
