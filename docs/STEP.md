# T-bears deploy step

```
# deploy INS Registry
tbears deploy ins_registry -k keypath

# get INS Registry contract address
tbears txresult <tx>

# deploy INS Registrar, should update the INS Registry address first
tbears deploy ins_registrar -k keypath

# get INS Registrar contract address
tbears txresult <tx>

# deploy INS Resolver
tbears deploy ins_resolver -k keypath

# set holder to INS Registrar
tbears sendtx actions/ins_registry/set_holder.json

# register domain to INS Registrar
tbears sendtx actions/ins_registrar/register.json

# check holder
tbears call actions/ins_registry/get_holder.json
```

### Testnet

Registry: cx1720bef7a1d0552e4609c5a72a71a173ca84b8f7
Registrar: cxb444156d3c905d4b690e1f8cb20e492624cc6e74
Resolver: cx5a6af92d8aeee267aab82ff6535a65f2ffa0b40f

```
# deploy INS Registry
tbears deploy ins_registry -u https://bicon.net.solidwallet.io/api/v3 -k keypath  -m install -s 0x50000000

# get INS Registry contract address // cx1720bef7a1d0552e4609c5a72a71a173ca84b8f7
tbears txresult 0xbabcb7c2a92ff57654d08db662a0db2f1719b2adac2e99b37c3cf16b664afccb -u https://bicon.net.solidwallet.io/api/v3

# deploy INS Registrar, should update the INS Registry address first
tbears deploy ins_registrar -u https://bicon.net.solidwallet.io/api/v3 -k keypath  -m install -s 0x50000000

# get INS Registrar contract address // cxb444156d3c905d4b690e1f8cb20e492624cc6e74
tbears txresult 0x344a38f23e1e17af67519fe645c1cd9c9e67b7e129001edd13cb98030591729b -u https://bicon.net.solidwallet.io/api/v3

# deploy INS Resolver 
tbears deploy ins_resolver -u https://bicon.net.solidwallet.io/api/v3 -k keypath  -m update -s 0x50000000

# get INS Resolver contract address // cx5a6af92d8aeee267aab82ff6535a65f2ffa0b40f
tbears txresult 0x5bd81c81c6bea2a09e406997741905135ca44048c879f861859daea448d6d643 -u https://bicon.net.solidwallet.io/api/v3

# set holder to INS Registrar
tbears sendtx actions/ins_registry/set_holder.json -u https://bicon.net.solidwallet.io/api/v3 -k keypath

```

#### Transaction

- Set node to registrar
https://bicon.tracker.solidwallet.io/transaction/0x28bffab2d9c725811ca438d9f065a9c60c01d8dd469c4d4d0b628c54659fe6c0

- Register `phyrex.icon`
https://bicon.tracker.solidwallet.io/transaction/0x2bc5e8591c41875e3de1aa4333caf4f5fe862af57d4a2370799f44ed13d6da80

- Set resolver to registry
https://bicon.tracker.solidwallet.io/transaction/0xa4674ea03df96a8739d44b88433f483a4e4821b2403305bec59f09e7e779d05a

- Set address to resolver
https://bicon.tracker.solidwallet.io/transaction/0x460bc13b491a7d3f0043d7eea34413a9d13fa66bcc1253c56da70537cd7b7936
