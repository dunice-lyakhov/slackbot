# from dotenv import load_dotenv, find_dotenv
from flask import Flask


app = Flask(__name__)

"""" Uncomment if you run app locally """
# Load from env file
# load_dotenv(find_dotenv())
# #
# from deploy_env_variables.env_variables import load_variables_to_env
#
# # load from google sheets creds file
# load_variables_to_env(locally=False)
""" <--------------------> """

import birthday_report.main
