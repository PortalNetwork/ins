# Reverse Registrar

In addition to mapping names to resources (forward resolution), INS also supports mapping from addresses to names and other metadata (reverse resolution).

Reverse records are named <ICON address>.addr.reverse.

Reverse resolution follows the same three-step process as forward resolution; the only change is that the name you are resolving has the special format defined above. To find the canonical name for an address, then, you would first query the NNS registry for the resolver responsible for (address).addr.reverse, then call name(bytes32) on that resolver in order to obtain its canonical name.
