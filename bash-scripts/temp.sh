casper-client put-deploy --session-path ../latest_supported_cep78.wasm --chain-name $1 --node-address $2 --secret-key $3 --payment-amount $4 --session-arg "collection_name:string='$5'" "collection_symbol:string='$6'" "total_token_supply:u64='$7'" "ownership_mode:u8='$8'" "nft_kind:u8='$9'" "identifier_mode:u8='${10}'" "nft_holder_mode:u8='${11}'" "minting_mode:u8='${12}'" "metadata_mutability:u8='${13}'" "burn_mode:u8='${14}'" "nft_metadata_kind:u8='${15}'" "json_schema:string='{\"properties\":{\"nft_name\":{\"name\":\"nft_name\",\"description\":\"name_of_nft\",\"required\":true},\"nft_description\":{\"name\":\"nft_description\",\"description\":\"description_of_nft\",\"required\":true},\"nft_name\":{\"name\":\"nft_url\",\"description\":\"url_of_nft\",\"required\":true}}}'"
