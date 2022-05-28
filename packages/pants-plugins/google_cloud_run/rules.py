from pants.engine.rules import collect_rules
from google_cloud_run.goals import rules as google_cloud_run_goal_rules
from google_cloud_run.util_rules.gcloud_binary import rules as gcloud_binary_rules

def rules():
    return [
        *collect_rules(),
        *gcloud_binary_rules(),
        *google_cloud_run_goal_rules()
    ]
