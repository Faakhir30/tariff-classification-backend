import os
import time

from fastapi import Depends, Header
import jwt
from sqlalchemy.ext.asyncio import AsyncSession

from app.session.db import get_db
from app.models import User
from app.utils.responses import response


SECREY_KEY = os.getenv("SECRET_KEY")


async def auth_dep(auth_token: str = Header(None), db: AsyncSession = Depends(get_db)):
    print("Authorization: ", auth_token)
    token = None
    if auth_token and auth_token.startswith("Bearer "):
        try:
            token = auth_token.split(" ")[1]
        except Exception as e:
            return response(401, "Invalid Token!", data=None)
    if not token:
        return response(401, "Authentication Token is missing!", data=None)
    try:
        decoded_token = jwt.decode(token, SECREY_KEY, algorithms=["HS256"])
        current_user = await db.get(User, decoded_token["id"])
        return (
            current_user
            if decoded_token["exp"] >= time.time() and current_user
            else response(401, "Invalid Token!")
        )

    except jwt.ExpiredSignatureError:
        return response(401, "Token has expired!", data=None)

    except Exception as e:
        print("Exception at auth middleware: ", e)
        return response(401, "Invalid Token!")
