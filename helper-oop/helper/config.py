contract_config = {
    'collection_name':'casper_collection',
    'collection_symbol': 'cspr',
    'total_token_supply': str(1000000),
    'ownership_mode': str(2),
    'nft_kind': str(1),
    'nft_identifier': str(1),
    'nft_holder_mode': str(2),
    'minting_mode': str(1),
    'metadata_mutability': str(0),
    'burn_mode': str(1),
    'metadata_kind':str(3), # Custom, validated = 3, CEP-78 = 0, NFT-721 = 1, RAW = 2
    'json_schema': r'''{\"properties\":{\"nft_name\":{\"name\":\"nft_name\",\"description\":\"thenameofthenft\",\"required\":true},\"nft_description\":{\"name\":\"nft_description\",\"description\":\"thedescriptionofthenft\",\"required\":true},\"nft_url\":{\"name\":\"nft_url\",\"description\":\"theurlofthenft\",\"required\":true}}}''',

    'chain_name': 'casper-net-1', # NCTL contract_config
    'node_address': 'http://127.0.0.1:11101', # NCTL contract_config
    'secret_key': './secret_key.pem',
    'payment_amount': str(300000000000) # 300 CSPR Tokens
}
