from aws_cdk import (
    aws_s3 as _s3,
    aws_iam as _iam,
    aws_s3_deployment as _s3_deploy,
    core
)

class Frontend(core.Stack):
    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        """Deploy the frontend to an S3 bucket
           
           Sets up:
           - An S3 with public access, static website hosting, and a bucket policy 
             that allows anonymous GetObject calls
        """
        super().__init__(app, id, **kwargs)

        bucket = _s3.Bucket(
            self, "guestbook",
            public_read_access=True,
            website_index_document="index.html"
        )

        bucket_policy = _iam.PolicyStatement(
            effect=_iam.Effect.ALLOW,
            actions=["s3:GetObject"],
            principals=[_iam.AnyPrincipal()],
            resources=[bucket.bucket_arn + "/*"] 
        )

        bucket.add_to_resource_policy(bucket_policy)
        
        _s3_deploy.BucketDeployment(
            self, "DeployWebsite",
            sources=[_s3_deploy.Source.asset("./src")],
            destination_bucket=bucket
        )

        core.CfnOutput(
            self, 'BucketDomainName',
            value=bucket.bucket_website_domain_name
        )


app = core.App()
stack = Frontend(app, "FrontendStack")
app.synth()