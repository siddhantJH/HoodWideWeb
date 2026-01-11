from fastapi import FastAPI
from dataModels.childNode import clildRegistorData
from controller.main_controller import CollectClients

app = FastAPI()


@app.post("/registorToMaster")
async def root(data:clildRegistorData):
    controller=CollectClients(data)