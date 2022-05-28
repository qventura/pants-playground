from google_cloud_run.fields import (GoogleCloudRunDependenciesField,
                                     GoogleCloudRunDockerImageNameField,
                                     GoogleCloudRunDockerRegistryField,
                                     GoogleCloudRunDockerTag)
from pants.engine.target import COMMON_TARGET_FIELDS, Target


class GoogleCloudRunTarget(Target):
    alias = "google_cloud_run"
    core_fields = (
        *COMMON_TARGET_FIELDS,
        GoogleCloudRunDependenciesField,
        GoogleCloudRunDockerRegistryField,
        GoogleCloudRunDockerImageNameField,
        GoogleCloudRunDockerTag,
    )

    help = "A target to deploy a Docker image into a Google Cloud Run service."
