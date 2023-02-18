#!/bin/bash
function srh(){
    casper-client get-state-root-hash --node-address http://127.0.0.1:11101
}
result=$(srh)
echo $result
