<h1 align="center">
    revwhoix
  <br>
</h1>

<h4 align="center">A simple utility to perform reverse WHOIS lookups using whoisxml API</h4>


<p align="center">
  <a href="#install">🏗️ Install</a>  
  <a href="#api-key-setup">📝 API Key Setup</a>  
  <a href="#usage">⛏️ Usage</a> 
  <br>
</p>


![revwhoix](https://github.com/devanshbatham/revwhoix/blob/main/static/revwhoix.png?raw=true)

# Install
```sh
git clone https://github.com/devanshbatham/revwhoix
cd revwhoix
pip install .
```

# API Key Setup

- Create an account at [main.whoisxmlapi.com](https://main.whoisxmlapi.com/).
- Navigate to [user.whoisxmlapi.com/products](https://user.whoisxmlapi.com/products) and obtain API Key.
- Paste the API key in `~/.config/whoisxml.conf` file.
- And, we are all set. 


# Usage

```sh
(~) >>> revwhoix -k "Airbnb, Inc"

                            __          _
   ________ _   ___      __/ /_  ____  (_)  __
  / ___/ _ \ | / / | /| / / __ \/ __ \/ / |/_/
 / /  /  __/ |/ /| |/ |/ / / / / /_/ / />  <
/_/   \___/|___/ |__/|__/_/ /_/\____/_/_/|_|


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
