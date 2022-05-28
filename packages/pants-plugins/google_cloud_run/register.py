from google_cloud_run.target_types import GoogleCloudRunTarget
from google_cloud_run.rules import rules as google_cloud_run_rules

def target_types():
    return [GoogleCloudRunTarget]

def rules():
    return [*google_cloud_run_rules()]