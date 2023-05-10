from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import httpx

class QwestiveEvent(BaseModel):
  eventName: str
  inviteePublicKey: str
  revenueValue: float | None = None
  conversionValue: float | None = None
  metadata: dict | None = None

class QwestiveRequestBody(BaseModel):
  secretApiKey: str
  projectId: str
  campaignId: str
  events: list[QwestiveEvent]

app = FastAPI()

URL = "https://us-central1-qwestive-referral-prod.cloudfunctions.net/setConversionEvents"

async def setConversionEvents(body):
    print(str(body)) 
    response = httpx.post(URL, json=jsonable_encoder(body))
    return response.text

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/setConversionEvents/")
async def create_item(item: QwestiveRequestBody):
    print("setConversionEvents") 
    res = await setConversionEvents(item)
    return res