import requests

HEADERS = {"X-API-Key":'35df7ca970834f178dd261d181eedaea'}

r = requests.get("https://www.bungie.net/platform/Destiny/Manifest/InventoryItem/1274330687", headers=HEADERS)

inventoryItem = r.json()
print(inventoryItem['Response']['data']['inventoryItem']['itemName'])