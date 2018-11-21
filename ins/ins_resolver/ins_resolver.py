from iconservice import *


class INSRegistryInterface(InterfaceScore):

    @interface
    def holder(self, node: str) -> Address: pass


class INSResolver(IconScoreBase):

    __ADDR_INS_REGISTRY_SCORE = 'addr_ins_registry_score'
    __ADDRESS = 'address'
    __MULTIHASH = 'multihash'
    __TEXT = 'text'
    __NAME = 'name'

    @eventlog(indexed=2)
    def AddressChanged(self, node: str, addr: Address): pass

    @eventlog(indexed=3)
    def MultihashChanged(self, node: str, name: str, multihash: str): pass

    @eventlog(indexed=3)
    def TextChanged(self, node: str, key: str, value: str): pass

    @eventlog(indexed=2)
    def NameChanged(self, node: str, name: str): pass

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

        self.__addr_ins_registry_score = VarDB(self.__ADDR_INS_REGISTRY_SCORE, db, value_type=Address)
        self.__address = DictDB(self.__ADDRESS, db, value_type=Address)
        self.__multihash = DictDB(self.__MULTIHASH, db, value_type=str, depth=2)
        self.__text = DictDB(self.__TEXT, db, value_type=str, depth=2)
        self.__name = DictDB(self.__NAME, db, value_type=str)

        self.__ins_registry_score = self.create_interface_score(
            self.__addr_ins_registry_score.get(), INSRegistryInterface)

    # TODO ins_address should be defined
    def on_install(self, ins_address: str = 'cx1720bef7a1d0552e4609c5a72a71a173ca84b8f7') -> None:
        super().on_install()

        ins_registry_address = Address.from_string(ins_address)
        self.__addr_ins_registry_score.set(ins_registry_address)

        self.__ins_registry_score = self.create_interface_score(self.__addr_ins_registry_score.get(), INSRegistryInterface)

    def on_update(self) -> None:
        super().on_update()

    @external
    def setAddr(self, node: str, addr: Address) -> None:
        if self.__ins_registry_score.holder(node) == self.msg.sender:
            self.AddressChanged(node, addr)
            self.__address[node] = addr

    @external
    def setMultihash(self, node: str, name: str, multihash: str) -> None:
        if self.__ins_registry_score.holder(node) == self.msg.sender:
            self.MultihashChanged(node, name, multihash)
            self.__multihash[node][name] = multihash

    @external
    def setText(self, node: str, key: str, value: str) -> None:
        if self.__ins_registry_score.holder(node) == self.msg.sender:
            self.TextChanged(node, key, value)
            self.__text[node][key] = value

    @external
    def setName(self, node: str, name: str) -> None:
        if self.__ins_registry_score.holder(node) == self.msg.sender:
            self.NameChanged(node, name)
            self.__name[node] = name

    @external(readonly=True)
    def addr(self, node: str) -> Address:
        return self.__address[node]

    @external(readonly=True)
    def multihash(self, node: str, name: str) -> str:
        return self.__multihash[node][name]

    @external(readonly=True)
    def text(self, node: str, key: str) -> str:
        return self.__text[node][key]

    @external(readonly=True)
    def name(self, node: str) -> str:
        return self.__name[node]
    