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

