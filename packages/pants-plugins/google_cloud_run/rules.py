from google_cloud_run.goals.rules import rules as goal_rules
from google_cloud_run.util_rules.gcloud_binary import \
    rules as gcloud_binary_rules
from pants.engine.rules import collect_rules


def rules():
    return [*collect_rules(), *gcloud_binary_rules(), *goal_rules()]
