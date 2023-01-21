"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Logging Bucket
logging_bucket = s3.BucketV2('loggingBucket')
logging_bucket_acl = s3.BucketAclV2(
    'loggingBucketACL',
    bucket=logging_bucket.id,
    acl='log-delivery-write')
logging_bucket_bucket_versioning = s3.BucketVersioningV2(
    'loggingBucketVersioning',
    bucket=logging_bucket.id,
    versioning_configuration=s3.BucketVersioningV2VersioningConfigurationArgs(
        status="Enabled"
    ))
logging_bucket_encryption = s3.BucketServerSideEncryptionConfigurationV2(
    'loggingBucketEncryption',
    bucket=logging_bucket.id,
    rules=[s3.BucketServerSideEncryptionConfigurationRuleArgs(
        apply_server_side_encryption_by_default=s3.BucketServerSideEncryptionConfigurationV2RuleApplyServerSideEncryptionByDefaultArgs(
            sse_algorithm='AES256'
        )
    )]
)
logging_bucket_public_access_block = s3.BucketPublicAccessBlock(
    'loggingBucketPublicAccessBlock',
    bucket=logging_bucket.id,
    block_public_acls=True,
    block_public_policy=True,
    ignore_public_acls=True,
    restrict_public_buckets=True)

# Pipeline Artifacts Bucket
pipeline_artifacts_bucket = s3.BucketV2('pipelineArtifactsBucket')
pipeline_artifacts_bucket_acl = s3.BucketAclV2(
    'pipelineArtifactsBucketAcl',
    bucket=pipeline_artifacts_bucket.id,
    acl='log-delivery-write')
pipeline_artifacts_bucket_bucket_versioning = s3.BucketVersioningV2(
    'pipelineArtifactsBucketVersioning',
    bucket=pipeline_artifacts_bucket.id,
    versioning_configuration=s3.BucketVersioningV2VersioningConfigurationArgs(
        status="Enabled"
    ))
pipeline_artifacts_bucket_encryption = s3.BucketServerSideEncryptionConfigurationV2(
    'pipelineArtifactsBucketEncryption',
    bucket=pipeline_artifacts_bucket.id,
    rules=[s3.BucketServerSideEncryptionConfigurationRuleArgs(
        apply_server_side_encryption_by_default=s3.BucketServerSideEncryptionConfigurationV2RuleApplyServerSideEncryptionByDefaultArgs(
            sse_algorithm='AES256'
        )
    )]
)
pipeline_artifacts_bucket_public_access_block = s3.BucketPublicAccessBlock(
    'pipelineArtifactsBucketPublicAccessBlock',
    bucket=pipeline_artifacts_bucket.id,
    block_public_acls=True,
    block_public_policy=True,
    ignore_public_acls=True,
    restrict_public_buckets=True)
pipeline_artifacts_bucket_logging = s3.BucketLoggingV2(
    'pipelineArtifactsBucketLogging',
    bucket=pipeline_artifacts_bucket.id,
    target_bucket=logging_bucket.id,
    target_prefix='log/'
)

# Export the name of the bucket
pulumi.export('pipeline_artifacts_bucket', pipeline_artifacts_bucket.id)
pulumi.export('logging_bucket', logging_bucket.id)
