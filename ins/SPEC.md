# SPEC

## INS Registry
Implementation of a simple registrar, which issues (sub)domains to the first account to request them.

#### holder
Returns the holder of the specified domain.
```python
def holder(self, node: str) -> Address
```

#### resolver
Returns the resolver of the specified domain.
```python
def resolver(self, node: str) -> Address
```

#### ttl
Returns the ttl of the specified domain.
```python
def ttl(self, node: str) -> int
```

#### setHolder
Update the holder to the sepcified domain.
```python
def setHolder(self, node: str, addr: Address) -> None
```

#### setSubnodeHolder
Set the holder to the specified subdomain.
```python
def setSubnodeHolder(self, node: str, label: str, addr: Address) -> None
```

#### setResolver
Set the resolver to the specified domain. 
```python
def setResolver(self, node: str, resolver: Address) -> None
```

#### setTTL
Set the time to leave to the specified domain.
```python
def setTTL(self, node: str, ttl: int) -> None
```

## INS Registrar

#### register
Use to register domain with specified address.
```python
def register(self, subnode: str, holder: Address) -> None
```

## INS Resolver

#### setAddr
Map address with the specified domain.
```python
def setAddr(self, node: str, addr: Address) -> None
```

#### setMultihash
Map multihash with the specified domain and type.
```python
def setMultihash(self, node: str, name: str, multihash: str) -> None
```

#### setText
Map text with the specified domain.
```python
def setText(self, node: str, key: str, value: str) -> None
```

#### setName
Map name with the specified domain.
```python
def setName(self, node: str, name: str) -> None
```

#### addr
Returns the address of the specified domain.
```python
def addr(self, node: str) -> Address
```

#### multihash
Returns the multihash of the specified domain and type.
```python
def multihash(self, node: str, name: str) -> str
```

#### text
Returns the text of the specified domain.
```python
def text(self, node: str, key: str) -> str
```

#### name
Returns the name of the specified domain.
```python
def name(self, node: str) -> str
```
