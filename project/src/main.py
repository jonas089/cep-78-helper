import argparse, subprocess, time
from cep78 import CEP78
from query import get_deploy, query_account_named_keys, query_contract_by_name
from config import contract_config
from utils import dump_json_temp
print(
'''
 ██████ ███████ ██████        ███████  █████
██      ██      ██   ██            ██ ██   ██
██      █████   ██████  █████     ██   █████
██      ██      ██               ██   ██   ██
 ██████ ███████ ██               ██    █████


'''
)

def new_instance(config):
    return CEP78(config['collection_name'],
    config['collection_symbol'],
    config['total_token_supply'],
    config['ownership_mode'],
    config['nft_kind'],
    config['nft_identifier'],
    config['nft_holder_mode'],
    config['minting_mode'],
    config['metadata_mutability'],
    config['burn_mode'],
    config['metadata_kind'],
    config['json_schema'])
parser = argparse.ArgumentParser(
            prog = 'ProgramName',
            description = 'What the program does',
            epilog = 'Text at the bottom of help')
parser.add_argument('-f', '--function')

# install arguments

## Basic
parser.add_argument('-Name', '--collection-name')
parser.add_argument('-Symbol', '--collection-symbol')
parser.add_argument('-Supply', '--total-token-supply')
## Medium
parser.add_argument('-chain', '--chain-name')
parser.add_argument('-n', '--node-address')
parser.add_argument('-key', '--secret-key')
parser.add_argument('-g', '--payment-amount')
parser.add_argument('-o', '--ownership-mode')
parser.add_argument('-kind', '--nft-kind')
parser.add_argument('-id', '--nft-identifier')
parser.add_argument('-hld', '--nft-holder-mode')
parser.add_argument('-mnt', '--minting-mode')
parser.add_argument('-mut', '--metadata-mutability')
parser.add_argument('-b', '--burn-mode')
## Advanced
parser.add_argument('-m', '--metadata-kind')
parser.add_argument('-j', '--json-schema')

# get-deploy arguments
parser.add_argument('-deploy', '--deploy-hash')

# query arguments
parser.add_argument('-acc', '--account-key')
parser.add_argument('-cname', '--contract-name')

# call arguments
parser.add_argument('-owner', '--token-owner')
parser.add_argument('-metadata', '--token-metadata')
parser.add_argument('-session', '--session-hash')

args = parser.parse_args()

if args.collection_name:
    contract_config['collection_name'] = args.collection_name
if args.collection_symbol:
    contract_config['collection_symbol'] = args.collection_symbol
if args.total_token_supply:
    contract_config['total_token_supply'] = args.total_token_supply
if args.ownership_mode:
    contract_config['ownership_mode'] = args.ownership_mode
if args.nft_kind:
    contract_config['nft_kind'] = args.nft_kind
if args.nft_identifier:
    contract_config['nft_identifier'] = args.nft_identifier
if args.nft_holder_mode:
    contract_config['nft_holder_mode'] = args.nft_holder_mode
if args.minting_mode:
    contract_config['minting_mode'] = args.minting_mode
if args.metadata_mutability:
    contract_config['metadata_mutability'] = args.metadata_mutability
if args.burn_mode:
    contract_config['burn_mode'] = args.burn_mode
if args.metadata_kind:
    contract_config['metadata_kind'] = args.metadata_kind
if args.json_schema:
    contract_config['json_schema'] = args.json_schema
if args.session_hash:
    contract_config['session_hash'] = args.session_hash

## Other arguments
if args.chain_name:
    contract_config['chain_name'] = args.chain_name
if args.node_address:
    contract_config['node_address'] = args.node_address
if args.secret_key:
    contract_config['secret_key'] = args.secret_key
if args.payment_amount:
    contract_config['payment_amount'] = args.payment_amount


def install(config):
    contract = new_instance(config)
    res = contract.install(config['chain_name'], config['node_address'], config['secret_key'], config['payment_amount'])
    return res

def mint(node_address, chain_name, secret_key, payment_amount, session_hash, token_owner, token_metadata):
    if not node_address or not chain_name or not secret_key or not payment_amount or not session_hash or not token_owner or not token_metadata:
        print('Missing Mandatory arguments!')
        return False
    call = ['../bash-scripts/temp.sh', node_address, chain_name, secret_key, payment_amount, session_hash, token_owner]
    # Replace [JSON_METADATA] and create temp file
    with open('../bash-scripts/mint.sh', 'r') as template_file:
        content = template_file.read()
        new_content = content.replace('[JSON_METADATA]', token_metadata)
        dump_json_temp(new_content)
    res = subprocess.check_output(call).decode('utf-8')
    print("Result: ", res)
    return res
# CEP-78
if args.function == 'install':
    install(contract_config)

if args.function == 'mint':
    mint(args.node_address, args.chain_name, args.secret_key, args.payment_amount, args.session_hash, args.token_owner, args.token_metadata)

# Queries
if args.function == 'deploy-status':
    get_deploy(args.deploy_hash, args.node_address)

if args.function == 'query-account-named-keys':
    query_account_named_keys(args.node_address, args.account_key)

if args.function == 'query-contract-by-name':
    query_contract_by_name(args.node_address, args.account_key, args.contract_name)
