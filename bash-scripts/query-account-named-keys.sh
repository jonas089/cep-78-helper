#!/bin/bash
function acc(){
  casper-client query-global-state --node-address $1 -s $2 --key $3
}
result=$(acc $1 $2 $3)
echo $result
