casper-client put-deploy --session-path contract.wasm --chain-name casper-net-1 --node-address http://localhost:11101 --secret-key ./NCTL/casper-node/utils/nctl/assets/net-1/users/user-1/secret_key.pem --payment-amount 2500000000000 --session-arg "ownership_mode:u8='2'" "nft_kind:u8='1'" "nft_holder_mode:u8='2'" "minting_mode:u8='1'" "metadata_mutability:u8='0'" "burn_mode:u8='1'" "collection_name:string='test_collection'" "collection_symbol:string='tst'" "total_token_supply:u64='1000000'" "json_schema:string='{\"properties\":{\"nft_name\":{\"name\":\"nft_name\",\"description\":\"name_of_nft\",\"required\":true},\"nft_description\":{\"name\":\"nft_description\",\"description\":\"description_of_nft\",\"required\":true},\"nft_name\":{\"name\":\"nft_url\",\"description\":\"url_of_nft\",\"required\":true}}}'" "nft_metadata_kind:u8='3'" "identifier_mode:u8='1'"
