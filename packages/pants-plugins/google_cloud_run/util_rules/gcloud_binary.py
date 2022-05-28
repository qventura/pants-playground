from __future__ import annotations

from dataclasses import dataclass

from pants.core.util_rules.system_binaries import (
    BinaryPath,
    BinaryPathRequest,
    BinaryPaths,
    BinaryPathTest,
)
from pants.engine.environment import Environment, EnvironmentRequest
from pants.engine.process import Process
from pants.engine.rules import Get, collect_rules, rule

@dataclass
class GCloudBinary(BinaryPath):
    """The `gcloud` binary."""

    def __init__(
        self,
        path: str,
        fingerprint: str | None = None,
    ) -> None:
        super().__init__(path, fingerprint)

        return res

    def run_deploy(self, serviceName: str, tag: str) -> Process:
        return Process(
            argv=(self.path, "run", "deploy", name ," --image", repo, "--region", region),
            description=f"Deploying docker image {tag} to GCloud service {serviceName}",
        )

@dataclass(frozen=True)
class GCloudBinaryRequest:
    pass


@rule(desc="Finding the `gcloud` binary")
async def find_gcloud(request: GCloudBinaryRequest) -> GCloudBinary:
    search_path = await Get(Environment, EnvironmentRequest(["PATH"]))

    request = BinaryPathRequest(
        binary_name="gcloud",
        search_path=search_path,
        test=BinaryPathTest(args=["-v"]),
    )
    
    paths = await Get(BinaryPaths, BinaryPathRequest, request)
    first_path = paths.first_path_or_raise(request, rationale="interact with the GCloud cli")

    return GCloudBinary(
        first_path.path,
        first_path.fingerprint
    )


@rule
async def get_gcloud() -> GCloudBinary:
    return await Get(GCloudBinary, GCloudBinaryRequest())


def rules():
    return collect_rules()
