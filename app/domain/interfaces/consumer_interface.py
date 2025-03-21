from abc import ABC, abstractmethod

class MessageConsumerInterface(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass
    
    @abstractmethod
    def disconnect(self) -> None:
        pass
    
    @abstractmethod
    def consume(self) -> None:
        pass
