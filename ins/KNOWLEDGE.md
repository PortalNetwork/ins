# Knowledge

Variable  
`get`, `set`, `remove`
```python
self.__total_supply = VarDB(self.__TOTAL_SUPPLY, db, value_type=int)
```

Object
```python
self.__balances = DictDB(self.__BALANCES, db, value_type=int)
```

Array
`put`, `pop`, `get`
```python
self.__joiner_list = ArrayDB(self.__JOINER_LIST, db, value_type=Address)
```
