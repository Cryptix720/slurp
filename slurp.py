#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------------------
	SLURP experimental model for XSS attacks
------------------------------------------------------------------------------
"""

## # LIBRARIES # ##
import re
import json
import requests
import os
import bleach


## # CONTEXT VARIABLES # ##
version = 1.0

## # MAIN FUNCTIONS # ##

def parse_args():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--domain', type=str, required=True, help="Target domain.")
	parser.add_argument('-o', '--output', type=str, help="Output file.")
	parser.add_argument('-m', '--malicious URLs', type=str, help="Malicious files.")
	parser.add_argument('-x', '--xsseser', type=str, help="Trace xss files.")
	return parser.parse_args()

def banner():
	global version
	b = '''
 Model for detection and classification of code injection attacks
	
     Version {v} 
      Made by Chris Pro
	'''.format(v=version)
	print(b)
	
def clear_url(target):
	return re.sub('.*www\.','',target,1).split('/')[0].strip()
	

#def mal_url():
    

def check_protocol(attrs):

 if not attrs.get((None, u'href'), u'').startswith(('http:', 'https:')):

        return attrs


#def class_model():

#def test_injection():


 

 
 
def save_subdomains(subdomain,output_file):
	with open(output_file,"a") as f:
		f.write(subdomain + '\n')
		f.close()

		
		
		
def main():
	banner()
	args = parse_args()

	subdomains = []
	target = clear_url(args.domain)
	output = args.output
	#malicious =  
	#xsseser = 

	req = requests.get("https://crt.sh/?q=%.{d}&output=json".format(d=target))
	
	#rex = requests.get("https://csrc.nist.gov/?q=%.{d}&output=json".format(d=target))

	if req.status_code != 200:
		print("[X] Information not available!") 
		exit(1)
		
		
	json_data = json.loads('[{}]'.format(req.text.replace('}{', '},{')))

	for (key,value) in enumerate(json_data):
		subdomains.append(value['name_value'])

	
	print("\n[!] ---- TARGET: {d} ---- [!] \n".format(d=target))

	subdomains = sorted(set(subdomains))

	for subdomain in subdomains:
		print("[-]  {s}".format(s=subdomain))
		if output is not None:
			save_subdomains(subdomain,output)

	print("\n\n[!]  DONE! enjoy your SLURP.. ;).")


main()
	
