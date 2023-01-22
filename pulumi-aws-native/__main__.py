"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws_native import s3

# Logging bucket
logging_bucket = s3.Bucket(
    "logging-bucket",
    access_control=s3.BucketAccessControl.PRIVATE,
    versioning_configuration=s3.BucketVersioningConfigurationArgs(
        status=s3.BucketVersioningConfigurationStatus.ENABLED
    ),
    bucket_encryption=s3.BucketEncryptionArgs(
        server_side_encryption_configuration=[
            s3.BucketServerSideEncryptionRuleArgs(
                server_side_encryption_by_default=s3.BucketServerSideEncryptionByDefaultArgs(
                    s_se_algorithm=s3.BucketServerSideEncryptionByDefaultSSEAlgorithm.AES256
                )
            )
        ]
    ),
    public_access_block_configuration=s3.BucketPublicAccessBlockConfigurationArgs(
        block_public_acls=True,
        block_public_policy=True,
        ignore_public_acls=True,
        restrict_public_buckets=True
    )
)

pipeline_artifacts_bucket = s3.Bucket(
    "pipeline-artifacts-bucket",
    access_control=s3.BucketAccessControl.PRIVATE,
    versioning_configuration=s3.BucketVersioningConfigurationArgs(
        status=s3.BucketVersioningConfigurationStatus.ENABLED
    ),
    bucket_encryption=s3.BucketEncryptionArgs(
        server_side_encryption_configuration=[
            s3.BucketServerSideEncryptionRuleArgs(
                server_side_encryption_by_default=s3.BucketServerSideEncryptionByDefaultArgs(
                    s_se_algorithm=s3.BucketServerSideEncryptionByDefaultSSEAlgorithm.AES256
                )
            )
        ]
    ),
    public_access_block_configuration=s3.BucketPublicAccessBlockConfigurationArgs(
        block_public_acls=True,
        block_public_policy=True,
        ignore_public_acls=True,
        restrict_public_buckets=True
    ),
    logging_configuration=s3.BucketLoggingConfigurationArgs(
        destination_bucket_name=logging_bucket.id,
        log_file_prefix='log/'
    ),
    tags=[
        s3.BucketTagArgs(key='foo', value='bar')
    ]
)

# Export the name of the bucket
pulumi.export("logging_bucket", logging_bucket.id)
pulumi.export("pipeline_artifacts_bucket", pipeline_artifacts_bucket.id)
