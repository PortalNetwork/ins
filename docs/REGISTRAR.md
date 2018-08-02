# Registrar
INS registrar is a smart contract that owns a name, and allocates subdomains of it according to some set of rules defined in the smart contract code. For any available domain name, users will be able to bid and start the auction. There will be several rules for the INS registrar smart contract. 

The bidding process will take 5 days in total. The first 3 days will be open for any bidders to join. The auction will be closed for the last 2 days, and bidders will need to come back and reveal their bids in order to win the domain name. Unrevealed bid will not be entitled for the domain acquisition.

Additional rules will be implemented to prevent monopoly in the INS market. Firstly, 7 characters restriction will prevent users to bid domain names under 7 characters. Secondly, an 8 weeks lock up period will limit the availability of INS once it is deployed. During this period, some of the names will be locked up depending on the hash value of the name. More names will be available as time pass and at 8th week, all names will be available for bidding. The purpose of these restriction is to give time for user adoption and to prevent any single entity to dominate the INS` market.

Lastly, every interact with the INS smart contract, including bidding, selling, and buying will result in transaction fee. Depending on the need of ICON foundation, these fees could be either burned, give out to the contract creator as incentive or contribute back to the ICON community. The smart contract could be designed accordingly to compromise the need. 
