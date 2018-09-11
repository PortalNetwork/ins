from iconservice import *


class INSRegistryInterface(InterfaceScore):

    @interface
    def owner(self, node: bytes) -> Address: pass


class INSResolver(IconScoreBase):

    __ADDR_INS_REGISTRY_SCORE = 'addr_ins_registry_score'
    __ADDRESS = 'address'
    __MULTIHASH = 'multihash'
    __TEXT = 'text'
    __NAME = 'name'

    @eventlog(indexed=2)
    def AddressChanged(self, node: bytes, addr: Address): pass

    @eventlog(indexed=3)
    def MultihashChanged(self, node: bytes, name: str, multihash: bytes): pass

    @eventlog(indexed=3)
    def TextChanged(self, node: bytes, key: str, value: str): pass

    @eventlog(indexed=2)
    def NameChanged(self, node: bytes, name: str): pass

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

        self.__addr_ins_registry_score = VarDB(self.__ADDR_INS_REGISTRY_SCORE, db, value_type=Address)
        self.__address = DictDB(self.__ADDRESS, db, value_type=Address)
        self.__multihash = DictDB(self.__MULTIHASH, db, value_type=bytes, depth=2)
        self.__text = DictDB(self.__TEXT, db, value_type=str, depth=2)
        self.__name = DictDB(self.__NAME, db, value_type=str)

        self.__ins_registry_score = self.create_interface_score(
            self.__addr_ins_registry_score.get(), INSRegistryInterface)

    # TODO ins_address should be defined
    def on_install(self, ins_address: str = 'cx1390e811b2e0a9f2e5559ea26d8a39bc4b747a7a') -> None:
        super().on_install()

        ins_registry_address = Address.from_string(ins_address)
        self.__addr_ins_registry_score.set(ins_registry_address)

        self.__ins_registry_score = self.create_interface_score(self.__addr_ins_registry_score.get(), INSRegistryInterface)

    def on_update(self) -> None:
        super().on_update()

    @external
    def setAddr(self, node: bytes, addr: Address) -> None:
        if self.__ins_registry_score.owner(node) == self.msg.sender:
            self.AddressChanged(node, addr)
            self.__address[node] = addr

    @external
    def setMultihash(self, node: bytes, name: str, multihash: bytes) -> None:
        if self.__ins_registry_score.owner(node) == self.msg.sender:
            self.MultihashChanged(node, multihash)
            self.__multihash[node][name] = multihash

    @external
    def setText(self, node: bytes, key: str, value: str) -> None:
        if self.__ins_registry_score.owner(node) == self.msg.sender:
            self.TextChanged(node, key, value)
            self.__text[node][key] = value

    @external
    def setName(self, node: bytes, name: str) -> None:
        if self.__ins_registry_score.owner(node) == self.msg.sender:
            self.NameChanged(node, name)
            self.__name[node] = name

    @external(readonly=True)
    def addr(self, node: bytes) -> Address:
        return self.__address[node]

    @external(readonly=True)
    def multihash(self, node: bytes, name: str) -> bytes:
        return self.__multihash[node][name]

    @external(readonly=True)
    def text(self, node: bytes, key: str) -> str:
        return self.__text[node][key]

    @external(readonly=True)
    def name(self, node: bytes) -> str:
        return self.__name[node]
    