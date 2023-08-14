import os
from typing import Any, List

from fastapi import FastAPI, HTTPException, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

import cv2

from pydantic import BaseModel

import time
# create a fastapi app instance
app = FastAPI()

###################
# Configs
###################
INFERENCE_SERVER_URL = os.getenv("INFERENCE_SERVER_URL", "localhost:4001")
SECOND_PER_FRAME = os.getenv("SECOND_PER_FRAME", 1)


###################
# Models
###################
class ImageReturn(BaseModel):
    image: List[str]

###################
# APIs
###################
@app.get("/healthcheck")
def healthcheck() -> bool:
    """Ping and pong for healthcheck."""
    return True

# templates = Jinja2Templates(directory="src/js")
# app.mount("/frontend", StaticFiles(directory="src/js"), name="static")
@app.get("/", response_model=None)
async def read_users(request: Request) -> Request:
    context = {}
    context["request"] = request

    return templates.TemplateResponse("index.html", context)
