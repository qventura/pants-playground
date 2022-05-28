from pants.engine.target import (
    Dependencies,
    StringField,
)

class GoogleCloudRunDependenciesField(Dependencies):
    pass

class GoogleCloudRunDockerRegistryField(StringField):
    alias = 'registry'
    default = 'gcr.io'
    help = 'Registry to get the Docker image from.'

class GoogleCloudRunDockerImageNameField(StringField):
    alias = 'image'
    required = True
    help = 'Name of the docker image'

class GoogleCloudRunDockerTag(StringField):
    alias = 'tag'
    default = 'latest'
    help = 'Tag of the docker image'
