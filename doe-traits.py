import json

with open('json/ipfs_doe_nft_metadata.json') as metadata_f:
    data = json.loads(metadata_f.read())
    traits = {}

    # Generate traits list
    for asset in data['assets']:
        for trait in asset['attributes']:
            if trait['trait_type'] not in traits:
                traits[trait['trait_type']] = {'total_count': 1}
                traits[trait['trait_type']]['values_count'] = 0
                traits[trait['trait_type']]['values'] = {}
            else:
                traits[trait['trait_type']]['total_count'] = traits[trait['trait_type']]['total_count'] + 1

            if trait['value'] not in traits[trait['trait_type']]['values']:
                traits[trait['trait_type']]['values'][trait['value']] = 1
                traits[trait['trait_type']]['values_count'] = traits[trait['trait_type']]['values_count'] + 1
            else:
                traits[trait['trait_type']]['values'][trait['value']] = traits[trait['trait_type']]['values'][trait['value']] + 1

    # Sort traits' values by rarity
    for trait in traits:
        traits[trait]['values'] = dict(sorted(traits[trait]['values'].items(), key=lambda item: item[1]))

    with open('json/doe_nft_traits.json', 'w') as traits_f:
        json.dump(traits, traits_f)
