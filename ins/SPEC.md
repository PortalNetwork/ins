# SPEC

## INS Registry
Implementation of a simple registrar, which issues (sub)domains to the first account to request them.

#### holder
Returns the holder of the specified domain.
```
def holder(self, node: str) -> Address
```

#### resolver
Returns the resolver of the specified domain.
```
def resolver(self, node: str) -> Address
```

#### ttl
Returns the ttl of the specified domain.
```
def ttl(self, node: str) -> int
```

#### setHolder
Update the holder to the sepcified domain.
```
def setHolder(self, node: str, addr: Address) -> None
```

#### setSubnodeHolder
Set the holder to the specified subdomain.
```
def setSubnodeHolder(self, node: str, label: str, addr: Address) -> None
```

#### setResolver
Set the resolver to the specified domain. 
```
def setResolver(self, node: str, resolver: Address) -> None
```

#### setTTL
Set the time to leave to the specified domain.
```
def setTTL(self, node: str, ttl: int) -> None
```

## INS Registrar

#### register
Use to register domain with specified address.
```
def register(self, subnode: str, holder: Address) -> None
```

## INS Resolver

#### setAddr
Map address with the specified domain.
```
def setAddr(self, node: str, addr: Address) -> None
```

#### setMultihash
Map multihash with the specified domain and type.
```
def setMultihash(self, node: str, name: str, multihash: str) -> None
```

#### setText
Map text with the specified domain.
```
def setText(self, node: str, key: str, value: str) -> None
```

#### setName
Map name with the specified domain.
```
def setName(self, node: str, name: str) -> None
```

#### addr
Returns the address of the specified domain.
```
def addr(self, node: str) -> Address
```

#### multihash
Returns the multihash of the specified domain and type.
```
def multihash(self, node: str, name: str) -> str
```

#### text
Returns the text of the specified domain.
```
def text(self, node: str, key: str) -> str
```

#### name
Returns the name of the specified domain.
```
def name(self, node: str) -> str
```
