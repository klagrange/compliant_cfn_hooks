import logging
from typing import Any, MutableMapping, Optional
from cloudformation_cli_python_lib import (
    BaseHookHandlerRequest,
    HandlerErrorCode,
    Hook,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent,
    SessionProxy,
    exceptions,
)

from .models import HookHandlerRequest, TypeConfigurationModel
from .target_models.aws_s3_bucket import AwsS3Bucket

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "MyCompany::Testing::MyTestHook"

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint


LOG.setLevel(logging.INFO)


def validate_bucket_name(bucket: AwsS3Bucket):
    # Ensure bucket name follows naming conventions
    if not bucket.BucketName or not bucket.BucketName.__contains__("dino"):
        raise exceptions.NonCompliant(
            HandlerErrorCode.InvalidRequest, "Must specify a bucket name"
        )


def validate_versioning(bucket: AwsS3Bucket):
    # Ensure versioning is enabled
    if not bucket.VersioningConfiguration or not bucket.VersioningConfiguration.Status:
        raise exceptions.NonCompliant(
            HandlerErrorCode.NonCompliant, "Versioning is not enabled!"
        )


def validate_block_public_access(bucket: AwsS3Bucket):
    # Ensure block public access is enabled
    if (
        not bucket.PublicAccessBlockConfiguration
        or not bucket.PublicAccessBlockConfiguration.get("BlockPublicAcls", "")
    ):
        raise exceptions.NonCompliant(
            HandlerErrorCode.NonCompliant, "Block public access is not enabled!"
        )


def validate_ssl(bucket: AwsS3Bucket):
    # Ensure SSL is on
    if (
        not bucket.BucketEncryption
        or not bucket.BucketEncryption.ServerSideEncryptionConfiguration
    ):
        raise exceptions.NonCompliant(
            HandlerErrorCode.NonCompliant, "SSL is not enabled!"
        )


def validate_bucket_props(bucket: AwsS3Bucket):
    validate_bucket_name(bucket)
    # validate_versioning(bucket)
    # validate_block_public_access(bucket)
    # validate_ssl(bucket)


@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
def pre_create_handler(
    session: Optional[SessionProxy],
    request: HookHandlerRequest,
    callback_context: MutableMapping[str, Any],
    type_configuration: TypeConfigurationModel,
) -> ProgressEvent:
    target_model = request.hookContext.targetModel
    progress: ProgressEvent = ProgressEvent(status=OperationStatus.IN_PROGRESS)
    # TODO: put code here

    LOG.info("I AM HERE!!!")

    # Example:
    try:
        # Reading the Resource Hook's target properties
        resource_properties = target_model.get("resourceProperties")

        # ADDED
        LOG.info(resource_properties)
        LOG.info("xxx")
        bucket = AwsS3Bucket._deserialize(resource_properties)

        validate_bucket_props(bucket)

        if isinstance(session, SessionProxy):
            client = session.client("s3")
        # Setting Status to success will signal to cfn that the hook operation is complete
        progress.status = OperationStatus.SUCCESS
    except TypeError as e:
        # exceptions module lets CloudFormation know the type of failure that occurred
        LOG.info(e)
        # raise exceptions.InternalFailure(f"was not expecting type {e}")
        return ProgressEvent.failed(
            HandlerErrorCode.InternalFailure, f"[ERROR] {0}".format(e)
        )
        # this can also be done by returning a failed progress event
        # return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"was not expecting type {e}")

    return progress


@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_update_handler(
    session: Optional[SessionProxy],
    request: BaseHookHandlerRequest,
    callback_context: MutableMapping[str, Any],
    type_configuration: TypeConfigurationModel,
) -> ProgressEvent:
    target_model = request.hookContext.targetModel
    progress: ProgressEvent = ProgressEvent(status=OperationStatus.IN_PROGRESS)
    # TODO: put code here

    # Example:
    try:
        # A Hook that does not allow a S3 bucket's encryption to be modified

        # Reading the Resource Hook's target current properties and previous properties
        resource_properties = target_model.get("resourceProperties")
        previous_properties = target_model.get("previousResourceProperties")

        if resource_properties.get("BucketEncryption") != previous_properties.get(
            "BucketEncryption"
        ):
            progress.status = OperationStatus.FAILED
            progress.message = "Encryption configuration can not be changed"
        else:
            progress.status = OperationStatus.SUCCESS
    except TypeError as e:
        progress = ProgressEvent.failed(
            HandlerErrorCode.InternalFailure, f"was not expecting type {e}"
        )

    return progress


@hook.handler(HookInvocationPoint.DELETE_PRE_PROVISION)
def pre_delete_handler(
    session: Optional[SessionProxy],
    request: BaseHookHandlerRequest,
    callback_context: MutableMapping[str, Any],
    type_configuration: TypeConfigurationModel,
) -> ProgressEvent:
    # TODO: put code here
    return ProgressEvent(status=OperationStatus.SUCCESS)


# resource_properties: {'PublicAccessBlockConfiguration': {'RestrictPublicBuckets': 'true', 'BlockPublicPolicy': 'true', 'BlockPublicAcls': 'true', 'IgnorePublicAcls': 'true'}, 'BucketName': 'dino-my-bucket', 'BucketEncryption': {'ServerSideEncryptionConfiguration': [{'ServerSideEncryptionByDefault': {'SSEAlgorithm': 'AES256'}}]}, 'VersioningConfiguration': {'Status': 'Enabled'}}
