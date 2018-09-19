from iconservice import *
from Crypto.Hash import keccak
import re

class INSRegistry(IconScoreBase):

    __HOLDER = 'holder'
    __RESOLVER = 'resolver'
    __TTL = 'ttl'

    @eventlog(indexed=2)
    def Transfer(self, node: str, holder: Address): pass

    @eventlog(indexed=3)
    def NewHolder(self, node: str, label: str, holder: Address): pass

    @eventlog(indexed=2)
    def NewResolver(self, node: str, resolver: Address): pass

    @eventlog(indexed=2)
    def NewTTL(self, node: str, ttl: int) : pass

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        # Use DictDB to store value as map
        self.__holder = DictDB(self.__HOLDER, db, value_type=Address)
        self.__resolver = DictDB(self.__RESOLVER, db, value_type=Address)
        self.__ttl = DictDB(self.__TTL, db, value_type=int)

    def on_install(self) -> None:
        super().on_install()
        # initial all the node holder is the contract holder
        # top-level domain: icon
        self.__holder["icon"] = self.msg.sender

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def holder(self, node: str) -> Address:
        return self.__holder[node]

    @external(readonly=True)
    def resolver(self, node: str) -> Address:
        return self.__resolver[node]

    @external(readonly=True)
    def ttl(self, node: str) -> int:
        return self.__ttl[node]

    @external
    def setHolder(self, node: str, addr: Address) -> None:
        if self.__holder[node] == self.msg.sender:
            self.Transfer(node, addr)
            self.__holder[node] = addr

    @external
    def setSubnodeHolder(self, node: str, label: str, addr: Address) -> None:
        if self.__holder[node] == self.msg.sender and re.match("[a-z0-9]+", label):
            subnode = label + "." + node
            self.NewHolder(node, label, addr)
            self.__holder[subnode] = addr

    @external
    def setResolver(self, node: str, resolver: Address) -> None:
        if self.__holder[node] == self.msg.sender:
            self.NewResolver(node, resolver)
            self.__resolver[node] = resolver

    @external
    def setTTL(self, node: str, ttl: int) -> None:
        if self.__holder[node] == self.msg.sender:
            self.NewTTL(node, ttl)
            self.__ttl[node] = ttl
