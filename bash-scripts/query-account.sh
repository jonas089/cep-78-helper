#!/bin/bash
function acc(){
    casper-client query-global-state --node-address $1 -s $2 --key $3
}
result=$(acc)
echo $result
