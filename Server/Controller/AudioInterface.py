from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class AudioInterface(ABC):

    @abstractmethod
    def insert():
        pass

    @abstractmethod
    def remove():
        pass

    @abstractmethod
    def edit():
        pass

    @abstractmethod
    def readDB():
        pass
