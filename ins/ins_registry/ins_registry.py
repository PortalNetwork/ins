from iconservice import *
from Crypto.Hash import keccak


class INSRegistry(IconScoreBase):

    __OWNER = 'owner'
    __RESOLVER = 'resolver'
    __TTL = 'ttl'

    @eventlog(indexed=2)
    def Transfer(self, node: bytes, owner: Address): pass

    @eventlog(indexed=3)
    def NewOwner(self, node: bytes, label: bytes, owner: Address): pass

    @eventlog(indexed=2)
    def NewResolver(self, node: bytes, resolver: Address): pass

    @eventlog(indexed=2)
    def NewTTL(self, node: bytes, ttl: int) : pass

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        # Use DictDB to store value as map
        self.__owner = DictDB(self.__OWNER, db, value_type=Address)
        self.__resolver = DictDB(self.__RESOLVER, db, value_type=Address)
        self.__ttl = DictDB(self.__TTL, db, value_type=int)

    def on_install(self) -> None:
        super().on_install()
        # initial all the node owner is the contract owner
        # after deploy need to change 0x0 to INSRegistrar contract address
        self.__owner['0x0'] = self.msg.sender

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def owner(self, node: bytes) -> Address:
        return self.__owner[node]

    @external(readonly=True)
    def resolver(self, node: bytes) -> Address:
        return self.__resolver[node]

    @external(readonly=True)
    def ttl(self, node: bytes) -> int:
        return self.__ttl[node]

    @external
    def setOwner(self, node: bytes, addr: Address) -> None:
        if self.__owner[node] == self.msg.sender:
            self.Transfer(node, addr)
            self.__owner[node] = addr

    @external
    def setSubnodeOwner(self, node: bytes, label: bytes, addr: Address) -> None:
        if self.__owner[node] == self.msg.sender:
            # TODO check keccak hash
            subnode = self.namehash(node, label)
            self.NewOwner(node, label, addr)
            self.__owner[subnode] = addr

    @external
    def setResolver(self, node: bytes, resolver: Address) -> None:
        if self.__owner[node] == self.msg.sender:
            self.NewResolver(node, resolver)
            self.__resolver[node] = resolver

    @external
    def setTTL(self, node: bytes, ttl: int) -> None:
        if self.__owner[node] == self.msg.sender:
            self.NewTTL(node, ttl)
            self.__ttl[node] = ttl

    # Concate node and label
    def namehash(self, node: bytes, label: bytes) -> bytes:
        keccak256 = keccak.new(digest_bits=256)
        keccak256.update(node + label)
        hexdigest = keccak256.hexdigest()
        return hexdigest
