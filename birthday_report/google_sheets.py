from __future__ import print_function

import googleapiclient.discovery
from google.oauth2 import service_account

from core.settings import (DISCOVERY_URL, SCOPE,
                           SPREAD_SHEET_ID, RANGE_NAME, env_get_required)


def get_sheet_data():
    """
    Get data from google sheets.
    All variables should be placed in .env file or in virtualenv.
    Data returns in dict format. Example:

    {number_of_line: data}

    :return:
    """

    # Load credentials variables from env
    google_sheet_info = {
        "type":str(env_get_required("type")),
        "project_id": str(env_get_required("project_id")),
        "private_key_id": str(env_get_required("private_key_id")),
        "private_key": str(env_get_required("private_key")),
        "client_email": str(env_get_required("client_email")),
        "client_id": str(env_get_required("client_id")),
        "auth_uri": str(env_get_required("auth_uri")),
        "token_uri": str(env_get_required("token_uri")),
        "auth_provider_x509_cert_url": str(env_get_required(
            "auth_provider_x509_cert_url"
        )),
        "client_x509_cert_url": str(env_get_required("client_x509_cert_url"))
    }

    credentials = service_account.Credentials.from_service_account_info(google_sheet_info, scopes=SCOPE)

    # Create service
    service = googleapiclient.discovery.build('sheets', 'v4',
                                              discoveryServiceUrl=DISCOVERY_URL,
                                              credentials=credentials)

    # Get data from sheet
    result = service.spreadsheets().values().get(
        spreadsheetId=SPREAD_SHEET_ID, range=RANGE_NAME).execute()

    # Get values of columns
    values = result.get('values', [])

    # If not empty
    if not values:
        return 'No data found.'
    else:
        return values
