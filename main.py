from web3 import Web3

INFURA = 'https://arbitrum-mainnet.infura.io/v3/1a7def275e74445fb433aacbdf9fa3d7'

# Connect to blockchain
w3 = Web3(Web3.HTTPProvider(INFURA))
print(f'Connected: {w3.is_connected()}')

# Connect to contract
#target_address = w3.to_checksum_address("")
#target_ABI = ''

print(w3.eth.get_block('latest'))