# INS

## Registry

在 Registry 上面儲存的 owner 會是 deed 的合約 address 而不是擁有者本人，這樣才能確保 Registry 不會被亂改


## Deploy step

1. Deploy INSRegistry
2. Deploy INSRegistrar
3. Invoke INSRegistry.setSubnodeOwner('0x0', 'ins', INSRegistrar.address)
4. Deploy INSResolver