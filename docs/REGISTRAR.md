# Registrar
INS registrar is a smart contract that owns a name, and allocates subdomains of it according to some set of rules defined in the smart contract code. For any available domain name, users will be able to bid and start the auction. There will be several rules for the INS registrar smart contract. 

Additional rules will be implemented to prevent monopoly in the INS market. Firstly, `x` characters restriction will prevent users to bid domain names under `x` characters. Secondly, an `y` weeks lock up period will limit the availability of INS once it is deployed. During this period, some of the names will be locked up depending on the hash value of the name. More names will be available as time pass and at `8` weeks, all names will be available for bidding. The purpose of these restriction is to give time for user adoption and to prevent any single entity to dominate the INS market.

The bidding process will take `z` days in total. The first `n` days will be open for any bidders to join. The auction will be closed for the last `z-n` days, and bidders will need to come back and reveal their bids in order to win the domain name. Unrevealed bid will not be entitled for the domain acquisition.

Lastly, every interact with the INS smart contract, including bidding, selling, and buying will result in transaction fee. Depending on the need of ICON foundation, these fees could be either burned, give out to the contract creator as incentive or contribute back to the ICON community. The smart contract could be designed accordingly to compromise the need. 

#### Settings
`x`: default is 7.
`y`: default is 8.
`z`: default is 5.
`n`: default is 3.
