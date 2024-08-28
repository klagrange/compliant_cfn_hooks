import pytest
from .handlers import (
    validate_versioning,
    validate_bucket_name,
    validate_block_public_access,
)
from .target_models.aws_s3_bucket import AwsS3Bucket
from cloudformation_cli_python_lib import exceptions


def test_validate_bucket_name():
    bucket = AwsS3Bucket(
        AccelerateConfiguration=None,
        AccessControl="Private",
        AnalyticsConfigurations=None,
        BucketEncryption={"ServerSideEncryptionConfiguration": True},
        BucketName="dino-bucket",
        CorsConfiguration=None,
        IntelligentTieringConfigurations=None,
        InventoryConfigurations=None,
        LifecycleConfiguration=None,
        LoggingConfiguration=None,
        MetricsConfigurations=None,
        NotificationConfiguration=None,
        ObjectLockConfiguration=None,
        ObjectLockEnabled=False,
        OwnershipControls=None,
        PublicAccessBlockConfiguration={"BlockPublicAcls": True},
        ReplicationConfiguration=None,
        Tags=None,
        VersioningConfiguration={"Status": "Enabled"},
        WebsiteConfiguration=None,
        Arn=None,
        DomainName=None,
        DualStackDomainName=None,
        RegionalDomainName=None,
        WebsiteURL=None,
    )
    try:
        validate_bucket_name(bucket)
        assert True  # Validation passed, no exception raised
    except exceptions.NonCompliant:
        assert False  # Validation failed, exception raised


def test_validate_versioning():
    bucket = AwsS3Bucket(
        AccelerateConfiguration=None,
        AccessControl="Private",
        AnalyticsConfigurations=None,
        BucketEncryption={"ServerSideEncryptionConfiguration": True},
        BucketName="dino-bucket",
        CorsConfiguration=None,
        IntelligentTieringConfigurations=None,
        InventoryConfigurations=None,
        LifecycleConfiguration=None,
        LoggingConfiguration=None,
        MetricsConfigurations=None,
        NotificationConfiguration=None,
        ObjectLockConfiguration=None,
        ObjectLockEnabled=False,
        OwnershipControls=None,
        PublicAccessBlockConfiguration={"BlockPublicAcls": True},
        ReplicationConfiguration=None,
        Tags=None,
        VersioningConfiguration=None,  # Set VersioningConfiguration to None to test validation
        WebsiteConfiguration=None,
        Arn=None,
        DomainName=None,
        DualStackDomainName=None,
        RegionalDomainName=None,
        WebsiteURL=None,
    )
    try:
        validate_versioning(bucket)
        assert False  # Validation should fail, exception should be raised
    except exceptions.NonCompliant:
        assert True  # Validation passed, exception raised


def test_validate_block_public_access():
    bucket = AwsS3Bucket(
        AccelerateConfiguration=None,
        AccessControl="Private",
        AnalyticsConfigurations=None,
        BucketEncryption={"ServerSideEncryptionConfiguration": True},
        BucketName="dino-bucket",
        CorsConfiguration=None,
        IntelligentTieringConfigurations=None,
        InventoryConfigurations=None,
        LifecycleConfiguration=None,
        LoggingConfiguration=None,
        MetricsConfigurations=None,
        NotificationConfiguration=None,
        ObjectLockConfiguration=None,
        ObjectLockEnabled=False,
        OwnershipControls=None,
        PublicAccessBlockConfiguration={"BlockPublicAcls": True},
        ReplicationConfiguration=None,
        Tags=None,
        VersioningConfiguration={"Status": "Enabled"},
        WebsiteConfiguration=None,
        Arn=None,
        DomainName=None,
        DualStackDomainName=None,
        RegionalDomainName=None,
        WebsiteURL=None,
    )
    try:
        validate_block_public_access(bucket)
        assert True  # Validation passed, no exception raised
    except exceptions.NonCompliant:
        assert False  # Validation failed, exception raised
