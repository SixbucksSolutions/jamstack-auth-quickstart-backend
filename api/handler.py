import json
import logging
import os

import kinde_sdk.auth.async_oauth


logger = logging.getLogger()
logger.setLevel("INFO")


def ping(event, context):

    body = {
        "message": "Pong!",
    }

    response = {
        "statusCode"    : 200, 
        "headers": {
            "Access-Control-Allow-Origin": "https://jamstack-auth.publicntp.net",
            "Content-Type": "application/json",
        },
        "body"          : json.dumps(body, indent=4, sort_keys=True), 
    }

    return response


def user_get(event, context):
    env_var_names: list[str] = [
        "KINDE_CLIENT_ID",
        "KINDE_CLIENT_SECRET",
        "MGMT_API_CLIENT_ID",
        "MGMT_API_CLIENT_SECRET",
    ]

    env_vars: dict[str, str] = {}
    for curr_name in env_var_names:
        env_vars[curr_name] = os.environ.get(curr_name)

    # Initialize Kinde AsyncOAuth client
    oauth_client = kinde_sdk.auth.async_oauth.AsyncOAuth()
 
    body = {
        "env_vars": env_vars,
    }

    response = {
        "statusCode"    : 200,
        "headers": {
            "Access-Control-Allow-Origin": "https://jamstack-auth.publicntp.net",
            "Access-Control-Allow-Credentials": True,
            "Content-Type": "application/json",
        },
        "body"          : json.dumps(body, indent=4, sort_keys=True) + "\n",
    }

    return response

