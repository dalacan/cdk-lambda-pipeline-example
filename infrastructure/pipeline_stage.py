from aws_cdk import (
    Stage
)

from constructs import Construct

from infrastructure.lambda_stack import LambdaStack

class PipelineStage(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_stack = LambdaStack(self, "LambdaStack")