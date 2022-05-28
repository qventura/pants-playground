from pants.engine.target import (
    COMMON_TARGET_FIELDS,
    Target,
)

from google_cloud_run.fields import (
  GoogleCloudRunDependenciesField, 
  GoogleCloudRunDockerRegistryField, 
  GoogleCloudRunDockerImageNameField, 
  GoogleCloudRunDockerTag,
)

class GoogleCloudRunTarget(Target):
    alias = "google_cloud_run"
    core_fields = (
      *COMMON_TARGET_FIELDS,
      GoogleCloudRunDependenciesField,
      GoogleCloudRunDockerRegistryField,
      GoogleCloudRunDockerImageNameField,
      GoogleCloudRunDockerTag,
    )

    help = (
      "A target to deploy a Docker image into a Google Cloud Run service."
    )

