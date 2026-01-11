from fastapi import FastAPI
from controller.main_controller import CollectClients

app = FastAPI()


@app.get("/registorToMaster")
async def root():
    return {"message": "Hello World"}