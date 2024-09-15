import requests
import webbrowser

API_KEY = '35df7ca970834f178dd261d181eedaea'
CLIENT_ID = '48220'
REDIRECT_URI = 'https://www.ttv-emumanhonk.github.io'
AUTH_URL = f'https://www.bungie.net/en/OAuth/Authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}'
CLIENT_SECRET = 'VCMsXHZ0TmTHj-Vb1IoF4mMMCzqwjfgwUolpubYR5rA'
# Open the authorization URL in the user's browser
webbrowser.open(AUTH_URL)

TOKEN_URL = 'https://www.bungie.net/platform/app/oauth/token/'

def get_access_token(auth_code):
    payload = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI
    }
    
    response = requests.post(TOKEN_URL, data=payload)
    return response.json()

auth_code = input("Enter the URL Code: ")
token_data = get_access_token(auth_code)
print(token_data)
access_token = token_data['access_token']

def get_user_info(access_token):
    url = 'https://www.bungie.net/Platform/User/GetMembershipsForCurrentUser/'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-API-Key': API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Example usage
user_info = get_user_info(access_token)
membership_id = user_info['Response']['destinyMemberships'][0]['membershipId']
print(membership_id)