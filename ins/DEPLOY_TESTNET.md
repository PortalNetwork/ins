# Deploy Testnet

Claim testnet token from [http://52.88.70.222/](http://52.88.70.222/)

### Testnet

Title            | Description
-----------------|-------------------------------------------------------
Name             | Yeouido (여의도)
Node             | https://bicon.net.solidwallet.io
API endpoint     | https://bicon.net.solidwallet.io/api/v3
Network ID (nid) | 3
Tracker          | https://bicon.tracker.solidwallet.io
Transaction fee	 | on
SCORE audit      | off

### Update tbears

- tbears.json
- tbears_server_config.json
- tbears_cli_config.json

###

We should use tbears version 1.0.6.1 for the `step-limit`

```
tbears deploy ins_registry -u https://bicon.net.solidwallet.io/api/v3 -k keypath  -m install -s 0x50000000
```

```
tbears txresult 0xbabcb7c2a92ff57654d08db662a0db2f1719b2adac2e99b37c3cf16b664afccb -u https://bicon.net.solidwallet.io/api/v3
```

```
tbears deploy ins_registrar -u https://bicon.net.solidwallet.io/api/v3 -k keypath  -m install -s 0x50000000
```

### Reference
- [https://icon-project.github.io/docs/icon_network.html#testnet-for-dapps](https://icon-project.github.io/docs/icon_network.html#testnet-for-dapps)
