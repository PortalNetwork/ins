![ICON Name Service](./assets/cover.jpg)

[![Join the chat at https://gitter.im/PortalNetwork/ins](https://badges.gitter.im/PortalNetwork/ins.svg)](https://gitter.im/PortalNetwork/ins?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

> 📖🔍 Documents and implementations for the ICON Name Service.

| [English](./README.md) | [한국어](./README_KR.md) |  

## 💡 What is ICON?
ICON is building a massive platform that will allow various blockchains to interact with each other via smart contracts.  Existing within what developers brand the ICON Republic, communities will connect with each other using ICON’s loopchain technology.

## 💡 What is BNS?
BNS – or blockchain name system – is the protocol on the internet that turns human-comprehensible decentralized website names such as ‘website.icx’ or ‘mywebsite.eth’ into addresses understandable by decentralized network machines.

## 📝 Description

INS is the ICON Name Service, a distributed, open, and extensible naming system based on the ICON blockchain.

## 📚 Documents

#### Table of Contents
- [Introduction](./docs/INTRODUCTION.md)
- [Implementation](./docs/IMPLEMENTATION.md)
    - [Registry](./docs/REGISTRY.md)
    - [Registrar](./docs/REGISTRAR.md)
    - [Resolver](./docs/RESOLVER.md)
    - [ReverseRegistrar](./docs/REVERSE_REGISTRAR.md)
- [Developer Guide](./docs/DEVELOPER_GUIDE.md)
- [Integration](./docs/INTEGRATION.md)
- [Spec](./ins/SPEC.md)

## 📝 Guideline
- [Tutorial](./docs/TUTORIAL.md)
- [T-bears](./docs/T-BEARS.md)
- [STEP](./docs/STEP.md)

## Testnet Contracts

Title            | Description
-----------------|-------------------------------------------------------
Name             | Yeouido (여의도)
Node             | https://bicon.net.solidwallet.io
API endpoint     | https://bicon.net.solidwallet.io/api/v3
Network ID (nid) | 3
Tracker          | https://bicon.tracker.solidwallet.io
Transaction fee	 | on
SCORE audit      | off

INS Contract | Network    | Contract Address                           | Transaction Hash
-------------|------------|--------------------------------------------|-----------------------------------------------
Registry     | Yeouido    | cx1720bef7a1d0552e4609c5a72a71a173ca84b8f7 | [0xbabcb7c2a92ff57654d08db662a0db2f1719b2adac2e99b37c3cf16b664afccb](https://bicon.tracker.solidwallet.io/transaction/0xbabcb7c2a92ff57654d08db662a0db2f1719b2adac2e99b37c3cf16b664afccb)
Registrar    | Yeouido    | cxb444156d3c905d4b690e1f8cb20e492624cc6e74 | [0x344a38f23e1e17af67519fe645c1cd9c9e67b7e129001edd13cb98030591729b](https://bicon.tracker.solidwallet.io/transaction/0x344a38f23e1e17af67519fe645c1cd9c9e67b7e129001edd13cb98030591729b)
Resolver     | Yeouido    | cx5a6af92d8aeee267aab82ff6535a65f2ffa0b40f | [0x5bd81c81c6bea2a09e406997741905135ca44048c879f861859daea448d6d643](https://bicon.tracker.solidwallet.io/transaction/0x5bd81c81c6bea2a09e406997741905135ca44048c879f861859daea448d6d643)

## INS Workflow

![INS Workflow](./assets/ICON_web3.png)

## 🗂️ INS Stack

![INS Stack](./assets/ICON_1.png)

### State Layer
State layer is where user’s “state”, or user’s information and behavior, is stored. For ICON, Loopchain is where these data are stored, and gives users the ability to control their own state.

### Computation Layer
Computation layer is where SCORE executes complicated calculations. It is an environment for smart contracts on ICON to be checked and managed, just like how EVM (Ethereum Virtual Machine) manages smart contract on Ethereum. When a transaction occurs on ICON, the logic designed in SCORE will determine its path that cannot be altered. Portal Network will be deploying INS (SCORE) on this layer that consists 3 major components.

### Component Layer
With the combination of state layer and computation layer, many things could be implemented in the component layer. INS for instance, consists 3 major components — registrar, registry and resolver. These components make sure that INS is operable and could meet the specific needs of each individual.

![Component Layer](./assets/ICON_2.png)

### Protocol Layer
On the Protocol Layer, we will be presenting our BNS (Blockchain Name Service) standards that can make the INS more efficient and applicable. With the state, computation and component layers behind the scene, protocol layer serve as a gateway for users and developers to interact with our INS standard.

### User Control Layer
User control layer is in charge of managing private keys to communicate with the state layer. INS empowers users to control, set up and manage their digital asset with an easier and readable text. This enables more use cases around INS at the application layer. For example, our Web Builder let users to create their own decentralized websites (DWebs) binded with an INS, and a further enhancement on our extension could be used to access these DWebs with ease at “yourwebsite.icon”.

![User Control Layer & Application Layer](./assets/ICON_3.png)

### Application Layer
INS can be implemented into many other applications on ICON platform, such as wallet that can resolve INS, dApp that utilize INS for users identity and many more. We believe that it is an essential components to provide a better environment for both technical and non-technical users.


## #️⃣ Reference
- [IIP6](https://github.com/icon-project/IIPs/blob/master/IIPS/iip-6.md) - ICON Name Service Standard

## 📣 Contributing
See [CONTRIBUTING.md](./CONTRIBUTING.md) for how to help out.

## 🗒 Licence
See [LICENSE](./LICENSE) for details.
