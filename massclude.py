#!/usr/bin/env python3
# Massclude - developed by acidvegas in python (https://git.acid.vegas/massclude)

import argparse
import ipaddress
import json
import time
import urllib.request

def get_bogons(version):
    '''Returns a list of bogon IP addresses from Team Cymru.'''
    url = f'https://team-cymru.org/Services/Bogons/fullbogons-ipv{version}.txt'
    return urllib.request.urlopen(url).read().decode().split('\n')[2:]

def get_ixps(version):
	'''Returns a list of IXP IP addresses from CAIDA.'''
	latest = time.strftime('%Y%m')
	try:
		data = urllib.request.urlopen(f'https://publicdata.caida.org/datasets/ixps/ixs_{latest}.jsonl').read().decode()
	except:
		latest = str(int(time.strftime('%Y%m'))-1)
		data = urllib.request.urlopen(f'https://publicdata.caida.org/datasets/ixps/ixs_{latest}.jsonl').read().decode()
	decoder = json.JSONDecoder()
	objects = []
	for line in data.split('\n'):
		if len(line) > 0 and line[0][0] != "#":
			objects.append(decoder.decode(line))
	json_data = json.loads(json.dumps(objects))
	return [ip for item in json_data if item['prefixes']['ipv'+version] for ip in item['prefixes']['ipv'+version]]

def generate_list():
	return {
		'bogons' : {
			'4': sorted(get_bogons('4')),
			'6': sorted(get_bogons('6'))
		},
		'dns_root_servers' : {
			'4': [
				'198.41.0.4',     # a.root-servers.net Verisign, Inc.
				'199.9.14.201',   # b.root-servers.net University of Southern California, Information Sciences Institute
				'192.33.4.12',    # c.root-servers.net Cogent Communications
				'199.7.91.13',    # d.root-servers.net University of Maryland
				'192.203.230.10', # e.root-servers.net NASA (Ames Research Center)
				'192.5.5.241',    # f.root-servers.net Internet Systems Consortium, Inc.
				'192.112.36.4',   # g.root-servers.net US Department of Defense (NIC)
				'198.97.190.53',  # h.root-servers.net US Army (Research Lab)
				'192.36.148.17',  # i.root-servers.net Netnod
				'192.58.128.30',  # j.root-servers.net Verisign, Inc.
				'193.0.14.129',   # k.root-servers.net RIPE NCC
				'199.7.83.42',    # l.root-servers.net ICANN
				'202.12.27.33'    # m.root-servers.net WIDE Project
			],
			'6': [
				'2001:503:ba3e::2:30', # a.root-servers.net Verisign, Inc.
				'2001:500:200::b',     # b.root-servers.net University of Southern California, Information Sciences Institute
				'2001:500:2::c',       # c.root-servers.net Cogent Communications
				'2001:500:2d::d',      # d.root-servers.net University of Maryland
				'2001:500:a8::e',      # e.root-servers.net NASA (Ames Research Center)
				'2001:500:2f::f',      # f.root-servers.net Internet Systems Consortium, Inc.
				'2001:500:12::d0d',    # g.root-servers.net US Department of Defense (NIC)
				'2001:500:1::53',      # h.root-servers.net US Army (Research Lab)
				'2001:7fe::53',        # i.root-servers.net Netnod
				'2001:503:c27::2:30',  # j.root-servers.net Verisign, Inc.
				'2001:7fd::1',         # k.root-servers.net RIPE NCC
				'2001:500:9f::42',     # l.root-servers.net ICANN
				'2001:dc3::35'         # m.root-servers.net WIDE Project

			]
		},
		'government': {
			'4': [
				'6.0.0.0/8',   # Army Information Systems Center
				'7.0.0.0/8',   # DoD Network Information Center
				'11.0.0.0/8',  # DoD Intel Information Systems
				'21.0.0.0/8',  # DDN-RVN
				'22.0.0.0/8',  # Defense Information Systems Agency
				'26.0.0.0/8',  # Defense Information Systems Agency
				'28.0.0.0/8',  # DSI-North
				'29.0.0.0/8',  # Defense Information Systems Agency
				'30.0.0.0/8',  # Defense Information Systems Agency
				'33.0.0.0/8',  # DLA Systems Automation Center
				'55.0.0.0/8',  # DoD Network Information Center
				'205.0.0.0/8', # US-DOD
				'214.0.0.0/8', # US-DOD
				'215.0.0.0/8'  # US-DOD
			]
		},
		'ixps' : {
			'4': sorted(get_ixps('4')),
			'6': sorted(get_ixps('6'))
		}
	}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate an exclude.conf file based on IP version.')
    parser.add_argument('ip_version', choices=['4', '6'], help='IP version (either 4 or 6)')
    args = parser.parse_args()

    o_total = ipaddress.ip_network('0.0.0.0/0' if args.ip_version == '4' else '::/0').num_addresses
    total = o_total

    donotscan = generate_list()

    with open(f'exclude{args.ip_version}.conf', 'w') as file:
        for option in donotscan:
            if args.ip_version in donotscan[option]:
                file.write(f'\n# Excludes from {option}\n')
                for ip in donotscan[option][args.ip_version]:
                    try:
                        r_total = ipaddress.ip_network(ip).num_addresses
                        file.write(ip+'\n')
                        total -= r_total
                    except:
                        file.write(f"# Invalid IP/range from {option}\n{ip}\n")

    print(f'Total IP Addresses : {o_total:,}')
    print(f'Total After Clean  : {total:,}')