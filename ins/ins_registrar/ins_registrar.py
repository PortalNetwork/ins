from iconservice import *


class INSRegistryInterface(InterfaceScore):

    @interface
    def owner(self, node: bytes) -> Address: pass

    @interface
    def setSubnodeOwner(self, node: bytes, label: bytes, owner: Address): pass


class INSRegistrar(IconScoreBase):

    __ADDR_INS_REGISTRY_SCORE = 'addr_ins_registry_score'
    __ROOT_NODE = 'root_node'

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

        self.__addr_ins_registry_score = VarDB(self.__ADDR_TOKEN_SCORE, db, value_type=Address)
        self.__root_node = VarDB(self.__ROOT_NODE, db, value_type=bytes)

        self.__ins_registry_score = self.create_interface_score(self.__addr_ins_registry_score.get(), INSRegistryInterface)

    # TODO ins_address should be defined
    def on_install(self, ins_address: str = '') -> None:
        super().on_install()

        one_icx = 1 * 10 ** 18

        ins_registry_address = Address.from_string(ins_address)
        self.__addr_ins_registry_score.set(ins_registry_address)

        self.__ins_registry_score = self.create_interface_score(self.__addr_ins_registry_score.get(), INSRegistryInterface)

    def on_update(self) -> None:
        super().on_update()

    # TODO This function is only define register an INS, not include @payable algorithm
    @external
    def register(self, subnode: bytes, owner: Address) -> None:
        if self.__ins_registry_score.owner(subnode) == "" or self.__ins_registry_score.owner(subnode) == self.msg.sender:
            self.__ins_registry_score.setSubnodeOwner(self.__root_node, subnode, owner)
