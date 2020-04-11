from aws_cdk import (
    aws_apigateway as _apigw,
    aws_dynamodb as _dynamodb,
    aws_lambda as _lambda,
    core
)


class RestApi(core.Stack):
    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        """Deploy the REST API
           
           Sets up:
           - An API Gateway with CORS configured
           - A sign Lambda for posting new guestbook entries
           - A get entries Lambda for getting guestbook entries
           - Lambda integrations to wire the Lambda's up in API
           - A DynamoDB table for entries
           - The table name passed as an environment variable to the Lambdas
        """
        super().__init__(app, id, **kwargs)

        api = _apigw.RestApi(
            self, 'ApiGateway',
            rest_api_name='ApiGateway',
            default_cors_preflight_options={
                "allow_origins": _apigw.Cors.ALL_ORIGINS,
                "allow_methods": ["GET", "POST"],
                "allow_headers": _apigw.Cors.DEFAULT_HEADERS
            }
        )

        entries = api.root.add_resource("entries")
        entry = api.root.add_resource("entry")

        sign_lambda = _lambda.Function(
            self,'SignLambda',
            handler='sign.handler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
        )

        sign_lambda_integration = _apigw.LambdaIntegration(
            sign_lambda
        )

        entry.add_method(
            "POST", 
            sign_lambda_integration
            )


        get_entries_lambda = _lambda.Function(
            self,'GetEntriesLambda',
            handler='get_entries.handler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
        )

        get_entries_lambda_integration = _apigw.LambdaIntegration(
            get_entries_lambda
        )

        entries.add_method(
            "GET", 
            get_entries_lambda_integration
        )

        table = _dynamodb.Table(
            self, "GuestbookTable",
            partition_key=_dynamodb.Attribute(
                name="email", 
                type=_dynamodb.AttributeType.STRING
            ),
            sort_key=_dynamodb.Attribute(
                name="date", 
                type=_dynamodb.AttributeType.STRING
            ),
            read_capacity=1,
            write_capacity=1
        )

        table.grant_read_data(get_entries_lambda)
        table.grant_read_write_data(sign_lambda)

        get_entries_lambda.add_environment("TABLE", table.table_name);
        sign_lambda.add_environment("TABLE", table.table_name);


app = core.App()
stack = RestApi(app, "RestApiStack")
app.synth()