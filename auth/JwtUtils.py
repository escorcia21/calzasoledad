from jwt import decode, encode, exceptions
from datetime import datetime, timedelta
from flask import jsonify
import os

SECRENT_KEY = os.environ.get('SECRET_KEY')

def expire_day(days: int) -> datetime:
    return datetime.utcnow() + timedelta(days=days)

def write_token(data: dict) -> str:
    token = encode(payload = {**data, "exp": expire_day(364)}, key=SECRENT_KEY, algorithm='HS256')
    return token

def validate_token(token: str, output=False) -> dict:
    try:
        data = decode(token, key=SECRENT_KEY, algorithms=['HS256'])
        if output:
            return data
        return True
    except exceptions.DecodeError:
        raise exceptions.DecodeError("Invalid token")
    except exceptions.ExpiredSignatureError:
        raise exceptions.ExpiredSignatureError("Token expired")