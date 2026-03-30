# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    flask_env = os.getenv("FLASK_ENV")

    if flask_env == "production":
        return "Starting in production mode..."
    elif flask_env == "development":
        return "Starting in development mode..."
    else:
        return "Starting in empty mode..."

if __name__ == "__main__":
    print(start())
