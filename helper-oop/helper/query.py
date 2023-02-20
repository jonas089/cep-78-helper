import os, json, subprocess
from termcolor import colored

def get_deploy(deploy_hash, node_address):
    res = subprocess.check_output(['../bash-scripts/get-deploy.sh', deploy_hash, node_address]).decode('utf-8')
    print('Result: ', res)
    return json.loads(res)

def query_account_named_keys(node_address, account_key):
    # Get state root hash
    s = subprocess.check_output(['../bash-scripts/get-state-root-hash.sh', node_address])
    s = res.decode('utf-8')
    srh = json.loads(s)['result']['state_root_hash']
    # Use state root hash to query account
    acc = subprocess.check_output(['../bash-scripts/query-account-named-keys.sh', node_address, srh, account_key]).decode('utf-8')
    # Get account's named keys
    res = json.loads(acc)['result']['stored_value']['Account']['named_keys']
    print(colored('Account named keys: ', 'yellow'), res)
    return res

def query_contract_by_name(node_address, account_key, contract_name):
    # default name: cep78_contract_hash_casper_collection
    named_keys = query_account_named_keys(node_address, account_key)
    for contract in named_keys:
        if contract['name'] == contract_name:
            contract_hash = contract['key']
            print(colored('Contract Hash found: ', 'green') + contract_hash)
            return contract_hash
    print(colored('Contract does not exist!', 'red'))
    return False
