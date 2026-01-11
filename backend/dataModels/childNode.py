from pydantic import BaseModel


class clildRegistorData(BaseModel):
    node_id:str
    node_port:str
    node_host:str
    is_node_active:bool



