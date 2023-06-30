from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    BundlingOptions
)
from constructs import Construct

class LambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        app1_function = _lambda.Function(self, "app1_function",
                                         code=_lambda.Code.from_asset("code/app1",
                                                                       bundling=BundlingOptions(
                                            image=_lambda.Runtime.PYTHON_3_9.bundling_image,
                                            command=["bash", "-c", "pip install -r requirements.txt -t /asset-output && cp -r . /asset-output"]
                                            ),
                                         ),
                                         runtime=_lambda.Runtime.PYTHON_3_9,
                                         handler="index.handler")
                                            
