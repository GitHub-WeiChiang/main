import json
import random

from fastapi import APIRouter
from fastapi import Query
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/employee/present", deprecated=True)
def employee_present(employee_name=Query(...)):
    print(f"🤖 [FakeAPI][/employee/present] 收到請求 {employee_name}")

    return JSONResponse(
        content=random.choice([True, False]),
        status_code=200
    )
