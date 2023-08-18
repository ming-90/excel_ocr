import os
import cv2
from typing import Any, List
from fastapi import FastAPI, HTTPException, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from src.backend.util import convert_image
from src.backend.infer import image_ocr

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
class dataframe(BaseModel):
    data: List

###################
# APIs
###################
@app.get("/healthcheck")
def healthcheck() -> bool:
    """Ping and pong for healthcheck."""
    return True

templates = Jinja2Templates(directory="src/frontend")
app.mount("/frontend", StaticFiles(directory="src/frontend"), name="static")
@app.get("/", response_model=dataframe)
async def index(request: Request) -> Request:
    context = {}
    context["request"] = request

    return templates.TemplateResponse("index.html", context)

@app.post("/infer", response_model=None)
async def infer(
    image: UploadFile = File(...)
) -> dataframe:
    image = await convert_image(image)
    df = image_ocr(image)
    return df