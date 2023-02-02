# -*- coding: utf-8 -*-

import argparse
import logging
import requests
import random
import sys
import os


#              ,----------------,              ,---------,
#         ,-----------------------,          ,"        ,"|
#       ,"                      ,"|        ,"        ,"  |
#      +-----------------------+  |      ,"        ,"    |
#      |  .-----------------.  |  |     +---------+      |
#      |  |                 |  |  |     | -==----'|      |
#      |  |  Sybil Scan!    |  |  |     |         |      |
#      |  |                 |  |  |/----|`---=    |      |
#      |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
#      |  |                 |  |  |  // |(((( [33]|    ,"
#      |  `-----------------'  |," .;'| |((((     |  ,"
#      +-----------------------+  ;;  | |         |,"    
#         /_)______________(_/  //'   | +---------+
#    ___________________________/___  `,
#   /  oooooooooooooooo  .o.  oooo /,   \,"-----------
#  / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
# /_==__==========__==_ooo__ooo=_/'   /___________,"
# `-----------------------------'

def check_api_key():

    try:
        path = os.path.expanduser('~') + "/.config/whoisxml.conf"
        f = open(path, "r")
        apiKey = f.read()
    except:
        logging.error(f"❌ Error occured while reading {path}")
        logging.error(f"⚠️ Make sure a valid API Key exists at {path}")
        sys.exit(1)
    return apiKey



def check_preview(preview_mode, url, headers):
    logging.info("🔍 Checking if domains exist")
    try:
        r = requests.post(url, json=preview_mode, headers=headers)
        if r.json()['domainsCount'] != 0:
            logging.info("✅ Domains exist")
            logging.info("⛏️ Fetching domains\n")
            return True
    except:
        logging.error("❌ Error occured while fetching domains")
        sys.exit(1)


def execute(data, domains, url, headers, keyword, apiKey):  
    try:
        r = requests.post(url, json=data, headers=headers)
    except:
        logging.error("❌ Error occured while fetching domains")
        sys.exit(1)
    if r.status_code == 200:
        # process
        if r.json()['domainsCount'] < 10000: 
            # domains are less than 10k, no need to iterate
            for domain in r.json()['domainsList']: 
                domains.append(domain)
                print(domain)
        else: 
            for domain in r.json()['domainsList']:
                print(domain)
            nextPageSearchAfter = r.json()['nextPageSearchAfter']
            data = {
            "apiKey": apiKey,
            "searchType": "current",
            "mode": "purchase",
            "searchAfter": nextPageSearchAfter,
            "punycode": True,
            "basicSearchTerms": {
                "include": [
                    keyword
                ]
                }
            }    
            execute(data, domains, url, headers, keyword, apiKey)
                
    else: 
        logging.error("❌ Error occured while fetching domains")
        sys.exit(1)
    

def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    logging.info("""\u001b[33;1m
                            __          _     
   ________ _   ___      __/ /_  ____  (_)  __
  / ___/ _ \ | / / | /| / / __ \/ __ \/ / |/_/
 / /  /  __/ |/ /| |/ |/ / / / / /_/ / />  <  
/_/   \___/|___/ |__/|__/_/ /_/\____/_/_/|_|  
                                              
                    
                            \u001b[36;1m - by Sybil Scan Research <research@sybilscan.com>\u001b[0m 
    """)

    parser = argparse.ArgumentParser(description='RevWhoix : A simple utility to perform reverse WHOIS lookups using whoisxml API')
    parser.add_argument('-k','--keyword' , help = 'Keyword to search related domains i.e. Org name, email address' , required=True)
    args = parser.parse_args()
    apiKey = check_api_key()
    if len(apiKey) < 2:
        logging.error(f"❌ API Key is not present at {os.path.expanduser('~') + '/.config/whoisxml.conf'}")
        sys.exit(1)
    logging.info(f"🚀 Performing reverse whois lookup on \"{args.keyword}\"")
    url = "https://reverse-whois.whoisxmlapi.com/api/v2"
    keyword = args.keyword
    domains = []
    data = {
        "apiKey": apiKey,
        "searchType": "current",
        "mode": "purchase",
        "punycode": True,
        "basicSearchTerms": {
            "include": [
                keyword
            ]
        }
    }

    preview_mode = {
        "apiKey": apiKey,
        "searchType": "current",
        "mode": "preview",
        "punycode": True,
        "basicSearchTerms": {
            "include": [
                keyword
            ]
        }
    }

    user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}

    if check_preview(preview_mode, url, headers):
        execute(data, domains, url, headers, keyword, apiKey)
