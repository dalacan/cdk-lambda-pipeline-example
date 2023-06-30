from aws_cdk import (
    Stack,
    aws_codecommit as codecommit,
    pipelines as pipelines
)
from constructs import Construct

from infrastructure.pipeline_stage import PipelineStage
class PipelineStack(Stack):
    

    def __init__(self, scope: Construct, construct_id: str, branch, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        repo = codecommit.Repository(self, "LambdaDemo",
            repository_name="lambda-demo-repo"
        )

        pipeline = pipelines.CodePipeline(self, "Pipeline",
                                        synth=pipelines.ShellStep("Synth",
                                                                    input=pipelines.CodePipelineSource.code_commit(repo, branch),
                                                                    commands=[
                                                                        "npm install -g aws-cdk",
                                                                        "pip install -r requirements.txt",
                                                                        "cdk synth"
                                                                    ],
                                        
                                        ),
                                        docker_enabled_for_synth=True
        )

        deploy = PipelineStage(self, "DeployTest")
        deploy_stage = pipeline.add_stage(deploy)


        deploy = PipelineStage(self, "DeployProd")
        deploy_stage = pipeline.add_stage(deploy,
                                          pre=[
                                                pipelines.ManualApprovalStep("PromoteToProd")
                                            ]
                                          )