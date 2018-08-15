from iconservice import *


class INSRegistryInterface(InterfaceScore):

    @interface
    def owner(node: bytes) -> Address: pass


class INSResolverInterface(InterfaceScore):

    @interface
    def setName(node: bytes, name: str) -> Address: pass


class INSReverseResolver(IconScoreBase):

    # TODO implement 
    @external
    def setName(name: str) -> None: pass
        
        
    