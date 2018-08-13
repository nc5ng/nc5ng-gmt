from .parsers import BaseFileParser
import logging

class FileBackedMetaBase(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kargs):
        """ Prepare the new class, here for completeness
        """
        logging.debug("Preparing Class %s"%name)
        return super().__prepare__(name, bases, **kargs)

    def __new__(metacls, name, bases, namespace, **kargs):
        logging.debug("Creating Class %s"%name)
        return super().__new__(metacls, name, bases, namespace)

    @property
    def parser(self):
        return self._parser
    

    @parser.setter
    def parser(self, parser):
        logging.debug("Setting parser instance %s"%parser)
        if not(issubclass(parser.__class__,BaseFileParser)):
            raise TypeError("parser %s is not a valid BaseFileParser"%str(parser))

        self._parser = parser

    @property
    def instances(self):
        return self._instances

    
    def __init__(cls, name, bases, namespace, Parser=BaseFileParser, **kwargs):
        """ Initialize a new FileBacked Class

        This is a slot method for class creation, __init__ is called when class is defined (load time)

        \param cls - reference to new type, similiar to @classmethod
        \param name - new class name
        \param bases - base classes
        \param namespace - new class attributes
        \param Parser - BaseFileParser underlying this type
        \param **kwargs - keywords passed to Parser initialization
        
        """        
        logging.debug("Creating File Backed Class %s"%name)

        if Parser:
            logging.debug("Creating Parser Instance of %s"%Parser)
            cls.parser = Parser(**kwargs)
            
        cls._Parser = Parser
        cls._instances = dict()
        super().__init__(name, bases, namespace)
            

class SingletonFileBackedMeta(FileBackedMetaBase):
    
    def __init__(cls, name, bases, namespace, Parser=BaseFileParser, **kwargs):
        """
        """        
        cls._instance = None
        super().__init__(name, bases, namespace, Parser, **kwargs)

    def __call__(cls, *args, overwrite=False, **kwargs):
        if cls._instance is None or overwrite:
            logging.debug("Creating new Singleton File Backed Meta Instance %s"%cls.__name__ )
            inst = super().__call__(*args, **kwargs)
            cls._instance = inst
            return inst
        else:
            return cls._instance
        

