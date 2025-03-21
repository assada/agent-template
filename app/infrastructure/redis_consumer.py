import redis
import json
import requests
from app.config import Config
from app.domain.models.request import Request
from app.services.agent_service import AgentService
from app.domain.interfaces.consumer_interface import MessageConsumerInterface

class RedisConsumer(MessageConsumerInterface):
    def __init__(self):
        self.client = None
        
    def connect(self) -> None:
        self.client = redis.Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
        
    def disconnect(self) -> None:
        if self.client:
            self.client.close()
            
    def consume(self):
        if not self.client:
            self.connect()
            
        while True:
            item = self.client.blpop("task_queue", timeout=0)
            if item:
                try:
                    payload = json.loads(item[1].decode())
                    req = Request(payload["query"], payload.get("data"), payload.get("params"))
                    res = AgentService().handle(req)
                    if res.success:
                        requests.post(Config.CALLBACK_URL_SUCCESS, json={"result": res.result})
                    else:
                        requests.post(Config.CALLBACK_URL_ERROR, json={"error": res.error})
                except:
                    requests.post(Config.CALLBACK_URL_ERROR, json={"error": "processing failed"})
