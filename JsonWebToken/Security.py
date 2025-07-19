from datetime import datetime, timedelta
from typing import Any, Union, Optional
from jose import jwt
from fastapi import Header, HTTPException

ALGORITHM = "HS256"
SECRET_KEY = "albert0425369@gmail.com"


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    """
    生成token

    :param subject: 保存到 token 的值
    :param expires_delta: 过期时间
    :return:
    """

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=60
        )

    to_encode = {"exp": expire, "sub": str(subject)}

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def check_jwt_token(
     token: Optional[str] = Header(...)
) -> Union[str, Any]:
    """
    解析验证 headers 中为 token的值
    当然也可以用 Header(..., alias="Authentication") 或者 alias="X-token"

    :param token:
    :return:
    """

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload
    except (jwt.JWTError, jwt.ExpiredSignatureError, AttributeError):
        # 抛出自定义异常，然后捕获统一响应
        raise HTTPException(status_code=498, detail="access token fail")
