# Implementation

## INS Smart Contracts

The link of INS smart contract as below:
- [Regsitry](../ins/ins_resigry)
- [Registrar](../ins/ins_registrar)
- [Resolver](../ins/ins_resolver)

More information about INS implementation as [HERE](../ins/)

## INS Spec

The internet HTTP protocol is using the URL below:

```
<protocol>://<subdomain>.<domain>.<top-level domain>/<path>
```

Example:
```
https://www.portal.icon/path
```

#### Spec
- http: The INS and protocol will be passed separately when the service requests.
- www.portal.icon: The content of the INS is used when user requests to the browser.
- path: The path is not processed at the DNS level, the same as INS, if there is a path, it is handled by other way or method.

## Resolving Names
Resolving names in INS is a three step process:
1. Normalise and hash the name you want to resolve (see [Namehash](#namehash)).
2. Query the INS registry for the address of the resolver responsible for the name.
3. Query the resolver for the resource you want to look up.

## Updating INS Records
Your application may wish to provide users with a means of updating names they own to point to resources your application provides or manages. Doing so follows a similar process to [Resolving Names](#resolving-names):

- Normalise and hash the name you want to resolve (see [Namehash](#namehash)).
- Query the INS registry for the address of the resolver responsible for the name.
- Call the appropriate update method on the resolver.

## Namehash
Names in INS are represented as 32 byte hashes, rather than as plain text. This simplifies processing and storage, while permitting arbitrary length domain names, and preserves the privacy of names onchain. The algorithm used to translate domain names into hashes is called namehash. The Namehash algorithm is defined in [EIP137](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-137.md).

In order to preserve the hierarchal nature of names, namehash is defined recursively, making it possible to derive the hash of a subdomain from the namehash of the parent domain and the name or hash of the subdomain label.

### Terminology
- domain - the complete, human-readable form of a name; eg, `wallet.portal.icon`.
- label - a single component of a domain; eg, `portal`, `wallet`, or `icon`. A label may not contain a period ('.').
- label hash - the output of the keccak-256 function applied to a label.
- node - the output of the namehash function, used to uniquely identify a name in INS.
