#!/bin/bash
function srh(){
    casper-client get-state-root-hash --node-address $1
}
result=$(srh $1)
echo $result
