#!/bin/bash
function mint(){
  casper-client put-deploy --session-entry-point mint --node-address $1 --chain-name $2 --secret-key $3 --payment-amount $4 --session-hash $5 --session-arg "token_owner:key='$6'" "token_meta_data:string='{\"nft_name\":\"DUMMY_NAME\",\"nft_description\":\"DUMMY_DESCRIPTION\",\"nft_url\":\"http://DUMMY_URL\"}'"
}
result=$(mint $1 $2 $3 $4 $5 $6)
echo $result
