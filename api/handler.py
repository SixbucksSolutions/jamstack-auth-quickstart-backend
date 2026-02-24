import json
import logging

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

    body = {
        "event": event,
    }

    response = {
        "statusCode"    : 200,
        "headers": {
            "Access-Control-Allow-Origin": "https://jamstack-auth.publicntp.net",
            "Content-Type": "application/json",
        },
        "body"          : json.dumps(body, indent=4, sort_keys=True) + "\n",
    }

    return response

