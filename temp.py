import json
from web3 import Web3

# Load the ABI from the JSON file
with open('temp.json', 'r') as abi_file:
    contract_abi = json.load(abi_file)

# Connect to Polygon Mumbai testnet
infura_url = "https://polygon-amoy.infura.io/v3/41a8174eef734e4a9411c2e386bce358"
w3 = Web3(Web3.HTTPProvider(infura_url))

if not w3.is_connected():
    raise ConnectionError("Failed to connect to the Polygon network")

# Contract address
contract_address = "0x2Fb6cb634f55e90c0eb55b977B3A357769b217D8"

# Create contract instance using ABI loaded from the file
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Example: Get the owner of a token ID
token_id = 1  # Replace with actual token ID
owner = contract.functions.ownerOf(token_id).call()
print(f"Owner of token ID {token_id}: {owner}")
