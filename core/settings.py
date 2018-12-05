import os

from core.utils import env_get_required

# Base project dir
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret data used in production secret!

CLIENT_SECRET_FILE = env_get_required('CLIENT_SECRET_FILE')
SCOPE = [env_get_required('SCOPE')]
DISCOVERY_URL = (env_get_required('DISCOVERY_URL'))
SPREAD_SHEET_ID = env_get_required("SPREAD_SHEET_ID")
RANGE_NAME = env_get_required('RANGE_NAME')

# Slack
SLACK_CLIENT_ID = env_get_required("SLACK_CLIENT_ID")
CHANNEL_NAME = env_get_required("CHANNEL_NAME")

# Scheduler
HOURS = env_get_required('HOURS')
MINUTES = env_get_required('MINUTES')


