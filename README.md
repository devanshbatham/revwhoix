<h1 align="center">
    RevWhoix
  <br>
</h1>

<h4 align="center">A simple utility to perform reverse WHOIS lookups using whoisxml API</h4>


<p align="center">
  <a href="#installation">🏗️ Install</a>  
  <a href="#post-installation-instructions">📝 API Key Setup</a>  
  <a href="#example-usage">⛏️ Usage</a> 
  <br>
</p>


# Install
```sh
git clone https://github.com/Sybil-Scan/revwhoix
cd revwhoix
pip install .
```

# API Key Setup

- Create an account at [main.whoisxmlapi.com](https://main.whoisxmlapi.com/).
- Navigate to [user.whoisxmlapi.com/products](https://user.whoisxmlapi.com/products) and obtain API Key.
- Paste the API key in `~/.config/whoisxml.conf` file.
- And, we are all set. 


# Usage

```console
(~) >>> revwhoix -k "Airbnb, Inc"

                            __          _
   ________ _   ___      __/ /_  ____  (_)  __
  / ___/ _ \ | / / | /| / / __ \/ __ \/ / |/_/
 / /  /  __/ |/ /| |/ |/ / / / / /_/ / />  <
/_/   \___/|___/ |__/|__/_/ /_/\____/_/_/|_|


                             - by Sybil Scan Research <research@sybilscan.com>

🚀 Performing reverse whois lookup on "Airbnb, Inc"
🔍 Checking if domains exist
✅ Domains exist
⛏️ Fetching domains

hoteltonight.us
hotelstonight.info
hoteltonight.at
hotelstonight.us
hoteltonight.in
cybersource.com.do
byairbnb.com
airbnb-aws.com
..............
..............
..............
airbnb.com.pe
airbnb.ae
```