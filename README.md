# massclude

## Information
This is a simple script that will generate an exclude.conf file for masscan that contains a set of IP ranges that are pointless to scan.

These include a private & reserved IP ranges, bogon IP ranges, and IP ranges that belong to root DNS servers, internet exchange points, & government agencies.

This removes over 1.5 billion ip addresses from the scan, thus making it much faster and raising less suspicion.

This repository is hosted on a VPS that updates every 6 hours with the latest IP ranges to exclude. (soon)

___

<h6 align="center">Mirrors</h1>
<p align="center">
	<a href="https://git.acid.vegas/massclude">acid.vegas</a> • <a href="https://github.com/acidvegas/massclude">Github</a> • <a href="https://gitlab.com/acidvegas/massclude">Gitlab</a> • <a href="https://git.supernets.org/acidvegas/massclude">SuperNETs</a>
	<br><br><a href="https://www.buymeacoffee.com/acidvegas"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a BEER&emoji=🍺&slug=acidvegas&button_colour=FFDD00&font_colour=000000&font_family=Bree&outline_colour=000000&coffee_colour=ffffff" /></a>
</p>
