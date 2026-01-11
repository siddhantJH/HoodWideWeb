from pydantic import BaseModel



class clildNodeData(BaseModel):
    node_ip:str
    node_port:str
    node_host:str
    is_node_active:bool



