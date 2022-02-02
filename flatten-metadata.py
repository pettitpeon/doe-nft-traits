import json

# Generate traits JSON from IPFS metadata
json_data = {'assets': []}
dir = 'ipfs\doe_metadata_QmcxJeVYRhyevvwQgsBfSWiY7QVmyNx1rQinzXbc1ZYut5'

for i in range(1, 10001):
    with open(f'{dir}/{i}', 'r') as f:
        tmp_data = json.loads(f.read())
        json_data['assets'].append(tmp_data)    

with open('json/ipfs_doe_nft_metadata.json', 'w') as f:
    json.dump(json_data, f)       
