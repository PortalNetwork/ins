![ICON Name Service](./assets/cover.jpg)

[![Join the chat at https://gitter.im/PortalNetwork/ins](https://badges.gitter.im/PortalNetwork/ins.svg)](https://gitter.im/PortalNetwork/ins?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

> 📖🔍 ICON 네임 서비스 문서 및 구현.

| [English](./README.md) | [한국어](./README_KR.md) |  

## 💡 ICON 이란?
ICON은 다양한 블록체인 스마트 컨트랙을 통해 자본시장, 보험, 대학교, 헬스케어 등 다양한 커뮤니티를 ICON Republic의 루프체인 (Loopchain)을 통해 상호 연결하는 플랫폼을 구축하고 있습니다.

## 💡 BNS (블록체인 네임 서비스)?
BNS, 또는 블록체인 네임 시스템은 'website.icon'과 같은 쉬운 도메인 네임을 분산식 네트워크 컴퓨터들이 이해할 수 있는 주소로 바꿔주는 프로토콜입니다.

## 📝 소개
INS (ICON 네임 서비스)는 ICON 블록체인을 기반으로 분산 및 확장 가능한 명명 시스템입니다.

## 📚 문서

#### 목록
- [개요](./docs/INTRODUCTION.md)
- [실행](./docs/IMPLEMENTATION.md)
    - [Registry](./docs/REGISTRY.md)
    - [Registrar](./docs/REGISTRAR.md)
    - [Resolver](./docs/RESOLVER.md)
    - [ReverseRegistrar](./docs/REVERSE_REGISTRAR.md)
- [개발 가이드](./docs/DEVELOPER_GUIDE.md)
- [통합](./docs/INTEGRATION.md)
- [스펙](./ins/SPEC.md)

## 📝 가이드라인
- [Tutorial](./docs/TUTORIAL.md)
- [T-bears](./docs/T-BEARS.md)
- [STEP](./docs/STEP.md)

## Testnet 계약

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


## INS 워크플로우

![INS Workflow](./assets/ICON_web3.png)

## 🗂️ INS Stack

![INS Stack](./assets/ICON_1.png)

### State Layer
State Layer는 사용자의 "상태" 또는 사용자의 정보와 행동이 저장되는 곳입니다. ICON의 경우 루프체인은 이러한 데이터가 저장되는 곳이며 사용자가 자신의 "상태"를 통제 및 제어할 수 있는 기능을 제공합니다.

### Computation Layer
Computation layer는 SCORE가 계산을 실행하는 곳입니다. 이더리움에서 EVM (Ethereum Virtual Machine)이 스마트 컨트랙을 관리하는 방식과 마찬가지로 ICON에서 스마트 컨트랙을 확인하고 관리 할 수 있는 환경입니다. ICON에서 트랜잭션이 발생하면 SCORE에서 설계된 로직으로 계산이 실행되어 결과가 결정됩니다. Portal Network는 INS의 세 가지 주요 구성 요소를 computation layer에 배포합니다.

### Component Layer
State Layer와 Computation Layer의 특징을 결합함으로써 Component Layer에서 많은 것을 구현할 수 있습니다. 예를 들어, INS는 Registry (레지스트리), Registrar (레지스트라) 및 Resolver (리졸버)등 세 가지 주요 요소로 구성됩니다. 이러한 구성 요소는 INS의 원활한 작동을 가능하게하며 사용자들의 요구를 충족시키는 역할을 합니다.

![Component Layer](./assets/ICON_2.png)

### Protocol Layer
Protocol Layer에서는 INS를 보다 효율적으로 적용 할 수 있는 BNS (Blockchain Name Service) 표준을 제시합니다. Protocol Layer는 사용자 및 개발자들이 앞서 말한 INS의 State Layer, Computation Layer, Component Layer와의 상호작용을 지원해주는 게이트웨이 입니다.

### User Control Layer
User Control Layer는 State Layer와 직접적인 소통을 하기위해 필요한 개인 키 (Private Key)를 관리합니다. INS를 통해 사용자는 보다 쉬운 주소로 암호화폐 자산들을 관리 및 설정할 수 있습니다. 따라서, User Control Layer에는 여러가지 INS와 연관된 응용이 가능해집니다. 예를 들어, Web Builder를 사용하면 INS에 설정된 분산식 웹 사이트 (DWebs)를 만들 수 있으며 "yourwebsite.icon"와 같은 도메인 주소를 통해 DWebs에 보다 쉽게 접속할 수 있습니다.

![User Control Layer & Application Layer](./assets/ICON_3.png)

### Application Layer
INS는 ICON 플랫폼에 구축된 여러가지 어플리케이션에 구현될 수 있습니다. 예를 들어, INS resolve (리졸브)가 가능한 암호화폐 지갑, 또는 INS를 사용자 ID로 데체하는 dApp 등 많은 응용이 가능합니다. 이를 통해 비기술적인 사용자와 개발자 모두에게 사용하기 쉬운 환경을 제공하고 있습니다.

## #️⃣ 참조
- [IIP6](https://github.com/icon-project/IIPs/blob/master/IIPS/iip-6.md) - ICON 네임 서비스 (ICON Name Service) 기준.

## 📣 기여하기
[CONTRIBUTING.md](./CONTRIBUTING.md) 참조.

## 🗒 Licence
[LICENSE](./LICENSE) 참조.
