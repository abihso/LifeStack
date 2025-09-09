from fastapi import FastAPI


server = FastAPI()

@server.get("/")
async def index():
  return ""