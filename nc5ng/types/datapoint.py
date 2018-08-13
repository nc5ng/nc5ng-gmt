"""
`nc5ng` Data Types
-----------------------

DataPoint
~~~~~~~~~

DataPoint is the base DataPointType hierarchy for nc5ng



Other parts of this library may use a different hierarchy, but share a type generator


.. autoclass:: DataPoint
  :members:

.. autoclass:: DataPointContainer


"""
from .meta import DataPointType
import logging
    
class DataPoint(metaclass=DataPointType):
    """ 
    Base Data Point Type for `nadcon5-ng` conversion data
    """
    def __init__(self, *args, **kwargs):
        self._data = {}

        # for copy
        if args:
            if issubclass(args[0].__class__, DataPoint):
                kwargs = args[0]._data
        #initialize
        for k,v in kwargs.items():
            self._data[k] = v

    
    def __getattr__(self, name):
        if name in self._data:
            return self._data[name]
        else:
            raise AttributeError()
    

    @property
    def data(self):
        return self._data


    def __getitem__(self,name):
        if name in self._data:
            return self._data[name]
        else:
            raise KeyError()
    """
    def __eq__(self, other):
        if not issubclass(other.__class__, DataPoint) or self.type_shorthand != other.type_shorthand:
            return False
        else:
            for k in self.data:
                if not k in other.data or self.data[k] != other.data[k]:
                    return False
            for k in other.data:
                if not k in self.data:
                    return False
        return True
    """

    def __ge__(self, other):
        """ Superset """
        if  not issubclass(other.__class__, DataPoint):
            return False
        return other.__le__(self)
        
        
    def __gt__(self, other):
        """ Strict Superset """
        if not issubclass(other.__class__, DataPoint):
            return False
        return other.__lt__(self)
        
    def __le__(self, other):
        """ Subset, each element in our data is contained in the other
        """
        if not issubclass(other.__class__, DataPoint):
            return False

        if len(self.data) > len(other.data):
            return False
        else:
            for k in self.data:
                if not k in other.data or self[k] != other[k]:
                    return False
        return True

    def __lt__(self, other):
        """ Strict Subset 
        """
        if not issubclass(other.__class__, DataPoint):
            return False
        
        if len(self.data) >= len(other.data):
            return False

        ## equality requires same length, already checked equality 
        return self.__le__(other)

    
    def __contains__(self, other):
        if not issubclass(other.__class__, DataPoint):
            try:
                k,v = other
                if not k in self.data:
                    return False                
                return self[k] == v
            except (TypeError, ValueError):
                return other in self.data
        else:
            for k in other.data:
                if not k in self.data:
                    return False
        return True

    def __repr__(self):
        return "DataPoint('" + self.__class__.type_shorthand + "', **"+repr(self._data)+")"

    def __str__(self):
        return "Data Point('" + self.__class__.type_shorthand + "') : " + str(self._data)
    
    def __bool__(self):
        return self.data.__bool__()
    


    
