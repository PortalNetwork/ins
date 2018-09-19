from iconservice import *


class INSRegistryInterface(InterfaceScore):

    @interface
    def holder(self, node: str) -> Address: pass

    @interface
    def setSubnodeHolder(self, node: str, label: str, holder: Address): pass


class INSRegistrar(IconScoreBase):

    __ADDR_INS_REGISTRY_SCORE = 'addr_ins_registry_score'
    __ROOT_NODE = 'root_node'

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

        self.__addr_ins_registry_score = VarDB(self.__ADDR_INS_REGISTRY_SCORE, db, value_type=Address)
        self.__root_node = VarDB(self.__ROOT_NODE, db, value_type=str)

        self.__ins_registry_score = self.create_interface_score(self.__addr_ins_registry_score.get(), INSRegistryInterface)

    # TODO ins_address should be defined
    def on_install(self, ins_address: str = 'cx391a9a74b552198d90d4c0e11590373b030c6184') -> None:
        super().on_install()

        ins_registry_address = Address.from_string(ins_address)
        self.__addr_ins_registry_score.set(ins_registry_address)
        self.__root_node.set('icon')
        self.__ins_registry_score = self.create_interface_score(self.__addr_ins_registry_score.get(), INSRegistryInterface)

    def on_update(self) -> None:
        super().on_update()

    # TODO This function is only define register an INS, not include @payable algorithm
    @external
    def register(self, subnode: str, holder: Address) -> None:
        node = subnode + "." + self.__root_node.get()
        if self.__ins_registry_score.holder(node) == None or self.__ins_registry_score.holder(node) == self.msg.sender:
            self.__ins_registry_score.setSubnodeHolder(self.__root_node.get(), subnode, holder)
