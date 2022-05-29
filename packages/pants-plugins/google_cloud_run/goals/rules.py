from google_cloud_run.goals.package import rules as package_rules
from google_cloud_run.goals.publish import rules as publish_rules
from google_cloud_run.util_rules.gcloud_binary import \
    rules as gcloud_binary_rules
from pants.engine.rules import collect_rules


def rules():
    return [
        *collect_rules(), 
        *gcloud_binary_rules(), 
        *package_rules(),
        *publish_rules(),
    ]
