#!/bin/bash
function install(){
  casper-client put-deploy --session-path ../latest_supported_cep78.wasm --chain-name $1 --node-address $2 --secret-key $3 --payment-amount $4 --session-arg "collection_name:string='$5'" "collection_symbol:string='$6'" "total_token_supply:u64='$7'" "ownership_mode:u8='$8'" "nft_kind:u8='$9'" "identifier_mode:u8='${10}'" "nft_holder_mode:u8='${11}'" "minting_mode:u8='${12}'" "metadata_mutability:u8='${13}'" "burn_mode:u8='${14}'" "nft_metadata_kind:u8='${15}'" "json_schema:string='[JSON_SCHEMA]'"
}
result=$(install $1 $2 $3 $4 $5 $6 $7 $8 $9 ${10} ${11} ${12} ${13} ${14} ${15})
echo $result
