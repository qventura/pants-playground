import logging
from dataclasses import dataclass

from google_cloud_run.fields import (GoogleCloudRunDockerImageNameField,
                                     GoogleCloudRunDockerRegistryField,
                                     GoogleCloudRunDockerTag)
from google_cloud_run.util_rules.gcloud_binary import GCloudBinary
from pants.core.goals.publish import (Publish, PublishFieldSet,
                                      PublishOutputData, PublishProcesses,
                                      PublishRequest)
from pants.engine.environment import Environment, EnvironmentRequest
from pants.engine.process import InteractiveProcess, InteractiveProcessRequest
from pants.engine.rules import collect_rules, rule
from pants.engine.unions import UnionRule
from pants.util.logging import LogLevel

logger = logging.getLogger(__name__)


class PublishGoogleCloudRunServiceRequest(PublishRequest):
    pass


@dataclass(frozen=True)
class PublishGoogleCloudRunServiceFieldSet(PublishFieldSet):
    publish_request_type = PublishGoogleCloudRunServiceRequest

    required_fields = (
        GoogleCloudRunDockerRegistryField,
        GoogleCloudRunDockerImageNameField,
        GoogleCloudRunDockerTag,
    )

    def get_output_data(self) -> PublishOutputData:
        return PublishOutputData(
            {
                "publisher": "google_cloud_run",
                **super().get_output_data(),
            }
        )


@rule(level=LogLevel.DEBUG)
async def google_cloud_run_publish(
    request: PublishGoogleCloudRunServiceRequest, gcloud: GCloudBinary
) -> PublishProcesses:
    logger.info("request", request)

    env = await Get(Environment, EnvironmentRequest(options.env_vars))
    jobs: list[PublishPackages] = []

    # DO SOMETHING

    return PublishProcesses(jobs)


def rules():
    return [
        *collect_rules(),
        *PublishGoogleCloudRunServiceFieldSet.rules(),
    ]
