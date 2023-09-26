# massclude

## Information
This is a simple script that will generate an *exclude.conf* file for [masscan](https://github.com/robertdavidgraham/masscan) that contains a set of IP ranges that are mostly pointless to scan thus making it much faster & raising less suspicion.

###### These ranges include:
- [Bogons](https://en.wikipedia.org/wiki/Bogon_filtering)
- [Department Of Defense DNIC](https://en.wikipedia.org/wiki/List_of_assigned_/8_IPv4_address_blocks#List_of_assigned_/8_blocks_to_the_United_States_Department_of_Defense)
- [Internet Excahnge Points](https://en.wikipedia.org/wiki/Internet_exchange_point)
- [Root DNS Servers](https://en.wikipedia.org/wiki/Root_name_server)
- [Reserved IP Ranges](https://en.wikipedia.org/wiki/Reserved_IP_addresses)


## What kind of numbers?
###### IPv4
**Total IPv4 Addresses** : 4,294,967,296

**Total After Massclude**  : 3,176,439,555

This is a **26%** drop in total IP addresses...

###### IPv6
**Total IP Addresses** : 340,282,366,920,938,463,463,374,607,431,768,211,456

**Total After Massclude**  : 12,551,294,199,370,633,260,152,632,202,625,108,965

While this is still a huge number, total IP addresses dropped **96.31%** here...

## See [avoidr](https://github.com/acidvegas/avoidr) for EXCLUSIVE exclusions

___

<h6 align="center">Mirrors</h1>
<p align="center">
	<a href="https://git.acid.vegas/massclude">acid.vegas</a> • <a href="https://github.com/acidvegas/massclude">Github</a> • <a href="https://gitlab.com/acidvegas/massclude">Gitlab</a> • <a href="https://git.supernets.org/acidvegas/massclude">SuperNETs</a>
	<br><br><a href="https://www.buymeacoffee.com/acidvegas"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a BEER&emoji=🍺&slug=acidvegas&button_colour=FFDD00&font_colour=000000&font_family=Bree&outline_colour=000000&coffee_colour=ffffff" /></a>
</p>
