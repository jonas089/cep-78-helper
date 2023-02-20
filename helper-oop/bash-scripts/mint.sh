#!/bin/bash
echo $7
function mint(){
  casper-client put-deploy --session-entry-point mint --node-address $1 --chain-name $2 --secret-key $3 --payment-amount $4 --session-hash $5 --session-arg "token_owner:key='$6'" "token_meta_data:string='[JSON_METADATA]'"
}
result=$(mint $1 $2 $3 $4 $5 $6 $7)
echo $result
