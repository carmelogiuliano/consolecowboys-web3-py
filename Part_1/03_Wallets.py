from web3 import Web3

INFURA = 'https://mainnet.infura.io/v3/1a7def275e74445fb433aacbdf9fa3d7'

# Connect to blockchain
w3 = Web3(Web3.HTTPProvider(INFURA))
print(f'Connected: {w3.is_connected()}')

# Connect to contract/wallet
target_address = w3.to_checksum_address("0x514910771AF9Ca656af840dff83E8264EcF986CA")

print(w3.from_wei(w3.eth.get_balance(target_address), 'ether'))
print(w3.to_hex(w3.eth.get_code(target_address)))