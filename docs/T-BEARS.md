# T-bears

## T-bears deploy 

```
(ins) Yungde-MacBook-Pro-2:ins phyrex$ tbears deploy abc
Send deploy request successfully.
If you want to check SCORE deployed successfully, execute txresult command
transaction hash: 0x830401d9a59f158d408ff8501f03819425f0a150e531f96ef25c8c0531dc524f
```

### INS Registry

#### Deploy
```
(ins) Yungde-MacBook-Pro-2:ins phyrex$ tbears deploy ins_registry
Send deploy request successfully.
If you want to check SCORE deployed successfully, execute txresult command
transaction hash: 0xe5c09265718ac58f0e45d794ed224d29a94bb6f03941680f366bae15880ae428
```

#### Check transaction result
```
(ins) Yungde-MacBook-Pro-2:ins phyrex$ tbears txresult 0xe5c09265718ac58f0e45d794ed224d29a94bb6f03941680f366bae15880ae428
Transaction result: {
    "jsonrpc": "2.0",
    "result": {
        "txHash": "0xe5c09265718ac58f0e45d794ed224d29a94bb6f03941680f366bae15880ae428",
        "blockHeight": "0xc5",
        "blockHash": "0x02e89a19767375d3b16ba2c845e70332f74f2601874248cc865d113b0644ddbd",
        "txIndex": "0x0",
        "to": "cx0000000000000000000000000000000000000000",
        "scoreAddress": "cxfc9f58943b43e02e20dfeb62530d9ee8573aa242",
        "stepUsed": "0x24f9c58",
        "stepPrice": "0x0",
        "cumulativeStepUsed": "0x24f9c58",
        "eventLogs": [],
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "status": "0x1"
    },
    "id": 1
}
```

#### Check SCORE API
```
(ins) Yungde-MacBook-Pro-2:ins phyrex$ tbears scoreapi cxfc9f58943b43e02e20dfeb62530d9ee8573aa242
SCORE API: [
    {
        "type": "fallback",
        "name": "fallback",
        "inputs": []
    },
    {
        "type": "function",
        "name": "owner",
        "inputs": [
            {
                "name": "node",
                "type": "bytes"
            }
        ],
        "outputs": [
            {
                "type": "Address"
            }
        ],
        "readonly": "0x1"
    },
    {
        "type": "function",
        "name": "resolver",
        "inputs": [
            {
                "name": "node",
                "type": "bytes"
            }
        ],
        "outputs": [
            {
                "type": "Address"
            }
        ],
        "readonly": "0x1"
    },
    {
        "type": "function",
        "name": "setOwner",
        "inputs": [
            {
                "name": "node",
                "type": "bytes"
            },
            {
                "name": "addr",
                "type": "Address"
            }
        ],
        "outputs": []
    },
    {
        "type": "function",
        "name": "setResolver",
        "inputs": [
            {
                "name": "node",
                "type": "bytes"
            },
            {
                "name": "resolver",
                "type": "Address"
            }
        ],
        "outputs": []
    },
    {
        "type": "function",
        "name": "setSubnodeOwner",
        "inputs": [
            {
                "name": "node",
                "type": "bytes"
            },
            {
                "name": "label",
                "type": "bytes"
            },
            {
                "name": "addr",
                "type": "Address"
            }
        ],
        "outputs": []
    },
    {
        "type": "function",
        "name": "setTTL",
        "inputs": [
            {
                "name": "node",
                "type": "bytes"
            },
            {
                "name": "ttl",
                "type": "int"
            }
        ],
        "outputs": []
    },
    {
        "type": "function",
        "name": "ttl",
        "inputs": [
            {
                "name": "node",
                "type": "bytes"
            }
        ],
        "outputs": [
            {
                "type": "int"
            }
        ],
        "readonly": "0x1"
    },
    {
        "type": "eventlog",
        "name": "NewOwner",
        "inputs": [
            {
                "name": "node",
                "type": "bytes",
                "indexed": "0x1"
            },
            {
                "name": "label",
                "type": "bytes",
                "indexed": "0x1"
            },
            {
                "name": "owner",
                "type": "Address",
                "indexed": "0x1"
            }
        ]
    },
    {
        "type": "eventlog",
        "name": "NewResolver",
        "inputs": [
            {
                "name": "node",
                "type": "bytes",
                "indexed": "0x1"
            },
            {
                "name": "resolver",
                "type": "Address",
                "indexed": "0x1"
            }
        ]
    },
    {
        "type": "eventlog",
        "name": "NewTTL",
        "inputs": [
            {
                "name": "node",
                "type": "bytes",
                "indexed": "0x1"
            },
            {
                "name": "ttl",
                "type": "int",
                "indexed": "0x1"
            }
        ]
    },
    {
        "type": "eventlog",
        "name": "Transfer",
        "inputs": [
            {
                "name": "node",
                "type": "bytes",
                "indexed": "0x1"
            },
            {
                "name": "owner",
                "type": "Address",
                "indexed": "0x1"
            }
        ]
    }
]
```

#### Create keypath
```
(ins) Yungde-MacBook-Pro-2:ins phyrex$ tbears keystore keypath
Input your keystore password:
Retype your keystore password:
Made keystore file successfully
```

#### Send Transaction
```
(ins) Yungde-MacBook-Pro-2:ins_registry phyrex$ tbears sendtx set_owner.json -k ../keypath
Input your keystore password:
Send transaction request successfully.
transaction hash: 0x6e40b37ad46429f9022b2301636dd99a1f5bb7ef9a58a1abdc8228f9d3d387f4
(ins) Yungde-MacBook-Pro-2:ins_registry phyrex$ tbears txresult 0x6e40b37ad46429f9022b2301636dd99a1f5bb7ef9a58a1abdc8228f9d3d387f4
Transaction result: {
    "jsonrpc": "2.0",
    "result": {
        "txHash": "0x6e40b37ad46429f9022b2301636dd99a1f5bb7ef9a58a1abdc8228f9d3d387f4",
        "blockHeight": "0xbf6",
        "blockHash": "0xb9f9233007b1e292d7ca3aae121dcb7410137750610b542e7db8c3ad7fa9f8c4",
        "txIndex": "0x0",
        "to": "cxfc9f58943b43e02e20dfeb62530d9ee8573aa242",
        "stepUsed": "0xfbce8",
        "stepPrice": "0x0",
        "cumulativeStepUsed": "0xfbce8",
        "eventLogs": [],
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "status": "0x1"
    },
    "id": 1
}
```

#### Call method
```
(ins) Yungde-MacBook-Pro-2:ins_registry phyrex$ tbears call get_owner.json
response : {
    "jsonrpc": "2.0",
    "result": null,
    "id": 1
}
```

