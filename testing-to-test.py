import requests

API_KEY = '35df7ca970834f178dd261d181eedaea'
BASE_URL = 'https://www.bungie.net/Platform/Destiny2/'

HEADERS = {
    'X-API-Key': API_KEY
}

def transfer_item(membership_type, character_id, item_id, item_instance_id, transfer_to_vault):
    url = f'{BASE_URL}Actions/Items/TransferItem/'
    payload = {
        'itemReferenceHash': item_id,
        'stackSize': 1,
        'transferToVault': transfer_to_vault,
        'itemId': item_instance_id,
        'characterId': character_id,
        'membershipType': membership_type
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    return response.json()

# Example usage
membership_type = 1  # Xbox
character_id = 'yourcharacter_id_here'
item_id = 'your_item_id_here'
item_instance_id = 'your_item_instance_id_here'
transfer_to_vault = False  # Set to True to transfer to vault

response = transfer_item(membership_type, character_id, item_id, item_instance_id, transfer_to_vault)
print(response)