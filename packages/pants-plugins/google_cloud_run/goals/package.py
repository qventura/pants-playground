import logging
from dataclasses import dataclass

from google_cloud_run.fields import (GoogleCloudRunDockerImageNameField,
                                     GoogleCloudRunDockerRegistryField,
                                     GoogleCloudRunDockerTag)

from pants.core.goals.package import (BuiltPackage, PackageFieldSet)
from pants.engine.internals.native_engine import EMPTY_DIGEST as EMPTY_DIGEST
from pants.engine.rules import collect_rules, rule
from pants.engine.unions import UnionRule
from pants.util.logging import LogLevel

logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class PackageGoogleCloudRunServiceFieldSet(PackageFieldSet):
    required_fields = (
        GoogleCloudRunDockerRegistryField,
        GoogleCloudRunDockerImageNameField,
        GoogleCloudRunDockerTag,
    )

@rule(level=LogLevel.DEBUG)
async def package(field_set: PackageGoogleCloudRunServiceFieldSet) -> BuiltPackage:
    logger.info("Dummy Packaging for GoogleCloudRunService...")

    return BuiltPackage(EMPTY_DIGEST, ())

def rules():
    return [
        *collect_rules(),
        UnionRule(PackageFieldSet, PackageGoogleCloudRunServiceFieldSet),
    ]
