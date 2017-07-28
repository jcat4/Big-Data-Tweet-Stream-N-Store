import abc
from abc import ABC, abstractmethod

# Abstract class outlining DAO class structures
class DAOBase(ABC):
  
  @abstractmethod
  def __init__(self):
    '''Print that object created'''
    return
    
  @abstractmethod
  def updateCollection(self, status):
    '''update table with status' attributes'''
    return
    
  @abstractmethod
  def getNumOfDocs(self):
    '''return DAO count attribute'''
    return