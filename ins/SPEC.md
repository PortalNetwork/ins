# SPEC

## INS Registry
Implementation of a simple registrar, which issues (sub)domains to the first account to request them.

#### def holder(self, node: str) -> Address
Returns the holder of the specified domain.

#### def resolver(self, node: str) -> Address
Returns the resolver of the specified domain.

#### def ttl(self, node: str) -> int
Returns the ttl of the specified domain.

#### def setHolder(self, node: str, addr: Address) -> None
Update the holder to the sepcified domain.

#### def setSubnodeHolder(self, node: str, label: str, addr: Address) -> None
Set the holder to the specified subdomain.

#### def setResolver(self, node: str, resolver: Address) -> None
Set the resolver to the specified domain. 

#### def setTTL(self, node: str, ttl: int) -> None
Set the time to leave to the specified domain.

## INS Registrar

#### def register(self, subnode: str, holder: Address) -> None
Use to register domain with specified address.

## INS Resolver

#### def setAddr(self, node: str, addr: Address) -> None
Map address with the specified domain.

#### def setMultihash(self, node: str, name: str, multihash: str) -> None
Map multihash with the specified domain and type.

#### def setText(self, node: str, key: str, value: str) -> None
Map text with the specified domain.

#### def setName(self, node: str, name: str) -> None
Map name with the specified domain.

#### def addr(self, node: str) -> Address
Returns the address of the specified domain.

#### def multihash(self, node: str, name: str) -> str
Returns the multihash of the specified domain and type.

#### def text(self, node: str, key: str) -> str
Returns the text of the specified domain.

#### def name(self, node: str) -> str
Returns the name of the specified domain.
