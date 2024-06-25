import math
from abc import ABC, abstractmethod


class AbstractChessPiece(ABC):
    def __init__(self,colour:str,position:str,active_status:bool):
        self._colour = colour
        self._position = position
        self._active_status = active_status
    
    @abstractmethod
    def move(self,position:str):
        pass
    
    @property
    def colour(self):
        return self._colour
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self,new_pos):
        self._position = new_pos
        
     
        

