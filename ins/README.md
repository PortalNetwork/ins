# INS Implementation
The INS system has thsee main smart contracts:

## Registry Smart Contract
INS registry is a single contract that provides a mapping from any registered name to the resolver responsible for it, and permits the owner of a name to set the resolver address, and to create subdomains, potentially with different owners to the parent domain.

The Registry implementation is at [ins_registry](./ins/ins_registry)

## Registrar Smart Contract
INS registrar is a smart contract that owns a Top-level domain, and allocates subdomains of it according to some set of rules defined in the smart contract code. For any available domain name, users will be able to purchase. The rules for the INS registrar smart contract will be interatly updated according to meet the benefit of whole ICON community.

The Registrar implementation is at [ins_registrar](./ins/ins_registrar)

## Resolver Smart Contract
INS resolvers are responsible for performing resources from a domain name, a resources can be a contract address, wallet address and IPFS hash. Utilizing the resolver smart contract enables users and developers using the decentralized resources easily bring more ideas and values to the ecosystem.

The Registrar implementation is at [ins_resolver](./ins/ins_resolver)

## Deploy step

1. Deploy [INS Registry](./ins/ins_registry/ins_registry.py)
2. Deploy [INS Registrar](./ins/ins_registrar/ins_registrar.py)
3. Invoke INSRegistry.setSubnodeOwner('0x0', 'ins', INSRegistrar.address)
4. Deploy [INS Resolver](./ins/ins_resolver/ins_resolver.py)
