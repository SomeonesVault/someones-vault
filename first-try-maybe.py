import requests
import webbrowser
import json

TOKEN_URL = 'https://www.bungie.net/platform/app/oauth/token/'
API_KEY = '35df7ca970834f178dd261d181eedaea'
CLIENT_ID = '48220'
REDIRECT_URI = 'https://ttv-emumanhonk.github.io/'
AUTH_URL = f'https://www.bungie.net/en/OAuth/Authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}'
CLIENT_SECRET = 'VCMsXHZ0TmTHj-Vb1IoF4mMMCzqwjfgwUolpubYR5rA'
# Open the authorization URL in the user's browser
webbrowser.open(AUTH_URL)

TOKEN_URL = 'https://www.bungie.net/platform/app/oauth/token/'

def get_destiny_manifest(api_key):
    # Function to get and save Destiny manifest
    url = "https://www.bungie.net/Platform/Destiny2/Manifest/"
    headers = {
        "X-API-Key": API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()


def get_item_data(manifest, api_key, item_type):
    item_data = []
    for key, value in manifest['Response']['jsonWorldComponentContentPaths']['en'].items():
        if 'DestinyInventoryItemDefinition' in key:
            url = f"https://www.bungie.net{value}"
            headers = {
                "X-API-Key": api_key
            }
            response = requests.get(url, headers=headers)
            items = response.json()
            for item in items.values():
                if item.get('itemType') == item_type:
                    item_data.append((item['hash'], item['displayProperties']['name']))
    return item_data

def save_item_data(item_data, filename):
    with open(filename, 'w') as f:
        for item_number, name in item_data:
            f.write(f"{item_number}: {name}\n")

# Fetch the manifest
manifest = get_destiny_manifest(API_KEY)

# Extract weapon data
weapon_data = get_item_data(manifest, API_KEY, 3)
save_item_data(weapon_data, 'destiny2_weapons.txt')

#Extract armor data
armor_data = get_item_data(manifest, API_KEY, 2)
save_item_data(armor_data, 'destiny2_armor.txt')

TestVar = get_destiny_manifest(API_KEY)

# Save the manifest to a JSON file
with open('test.json', 'w') as f:
    json.dump(TestVar, f, indent=4)


def get_access_token(auth_code):
    payload = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI
    }
    
    response = requests.post(TOKEN_URL, data= payload)

    if response.status_code == 200:
        token_data = response.json()
        if 'access_token' in token_data:
            return token_data['access_token']
        else:
            print("Error: 'access_token' not found in the response.")
            print(token_data)
            return None
    else:
        print(f"Error: Received status code {response.status_code}")
        print(response.json())
        return None

auth_code = input("Enter the URL Code: ")
access_token = get_access_token(auth_code)


if access_token:
    def get_user_info(access_token):
        url = 'https://www.bungie.net/Platform/User/GetMembershipsForCurrentUser/'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-API-Key': API_KEY
        }
        response = requests.get(url, headers=headers)
        return response.json()

   
    user_info = get_user_info(access_token)
    membership_id = user_info['Response']['destinyMemberships'][0]['membershipId']
    print(membership_id)
else:
    print("Failed to obtain access token.")

