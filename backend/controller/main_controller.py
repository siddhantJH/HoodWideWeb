from storage.postgress_connector import PostgresConnector
from connector.check_client_status import check_host_and_port


class CollectClients:
    
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self,client_credentials,log_obj=None):
        print("================Registor possible clients===============")
        self.registor_client(client_credentials)

    def registor_client(self,client_credentials):
        status=True
        # status=check_host_and_port(client_credentials)
        if status:
            self.save_client_details(client_credentials)

    def ping_client(client_credentials):
        pass

    def save_client_details(self,client_credentials):
        obj=PostgresConnector()
        obj.store_node_details(client_credentials)
        




