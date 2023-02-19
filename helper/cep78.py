import os, argparse, json, subprocess
from termcolor import colored
parser = argparse.ArgumentParser(
            prog = 'ProgramName',
            description = 'What the program does',
            epilog = 'Text at the bottom of help')
parser.add_argument('-f', '--function')

# install arguments

## Basic
parser.add_argument('-name', '--collection-name')
parser.add_argument('-sym', '--collection-symbol')
parser.add_argument('-supply', '--total-token-supply')
## Medium
parser.add_argument('-chain', '--chain-name')
parser.add_argument('-host', '--node-address')
parser.add_argument('-key', '--secret-key')
parser.add_argument('-gas', '--payment-amount')
parser.add_argument('-ownership', '--ownership-mode')
parser.add_argument('-kind', '--nft-kind')
parser.add_argument('-identifier', '--nft-identifier')
parser.add_argument('-hold', '--nft-holder-mode')
parser.add_argument('-mint', '--minting-mode')
parser.add_argument('-mutable', '--metadata-mutability')
parser.add_argument('-burn', '--burn-mode')
## Advanced
parser.add_argument('-metadata', '--metadata-kind')
parser.add_argument('-json', '--json-schema')

# get-deploy arguments
parser.add_argument('-deploy', '--deploy-hash')

# query arguments
parser.add_argument('-acc', '--account-key')
parser.add_argument('-cname', '--contract-name')

def dump_json_schema(new_content):
    if os.path.exists('../bash-scripts/temp.sh'):
        os.remove('../bash-scripts/temp.sh')
    with open('../bash-scripts/temp.sh', 'x'):
        pass
    os.system('chmod +x ../bash-scripts/temp.sh')

    with open('../bash-scripts/temp.sh', 'w') as template_file:
        template_file.write(new_content)
    template_file.close()

def install(args):
    # Mandatory Arguments
    default = {
        'name':'casper_collection',
        'sym': 'cspr',
        'supply': str(1000000),
        'chain': 'casper-net-1', # NCTL DEFAULT
        'host': 'http://127.0.0.1:11101', # NCTL DEFAULT
        'key': './secret_key.pem',
        'gas': str(300000000000), # 300 CSPR Tokens
        'ownership': str(2),
        'kind': str(1),
        'identifier': str(1),
        'hold': str(2),
        'mint': str(1),
        'mutable': str(0),
        'burn': str(1),
        'meta':str(3), # Custom, validated
        'json': r'''{\"properties\":{\"nft_name\":{\"name\":\"nft_name\",\"description\":\"name_of_nft\",\"required\":true},\"nft_description\":{\"name\":\"nft_description\",\"description\":\"description_of_nft\",\"required\":true},\"nft_name\":{\"name\":\"nft_url\",\"description\":\"url_of_nft\",\"required\":true}}}'''
    }

    # Override default if arguments specified

    ## Session arguments
    if args.collection_name:
        default['name'] = args.collection_name
    if args.collection_symbol:
        default['sym'] = args.collection_symbol
    if args.total_token_supply:
        default['supply'] = args.total_token_supply
    if args.ownership_mode:
        default['ownership'] = args.ownership_mode
    if args.nft_kind:
        default['kind'] = args.nft_kind
    if args.nft_identifier:
        default['identifier'] = args.nft_identifier
    if args.nft_holder_mode:
        default['hold'] = args.nft_holder_mode
    if args.minting_mode:
        default['mint'] = args.minting_mode
    if args.metadata_mutability:
        default['mutable'] = args.metadata_mutability
    if args.burn_mode:
        default['burn'] = args.burn_mode
    if args.metadata_kind:
        default['meta'] = args.metadata_kind
    if args.json_schema:
        default['json'] = args.json_schema

    ## Other arguments
    if args.chain_name:
        default['chain'] = args.chain_name
    if args.node_address:
        default['host'] = args.node_address
    if args.secret_key:
        default['key'] = args.secret_key
    if args.payment_amount:
        default['gas'] = args.payment_amount

    # Assign other arguments
    chain_name = default['chain']
    node_address = default['host']
    secret_key = default['key']
    payment_amount = default['gas']


    # Depending on metadata kind, deploy the contract with or without json schema.
    if default['meta'] == str(2) or default['meta'] == str(3):
        call = '../bash-scripts/temp.sh {chain_name} {node_address} {secret_key} {payment_amount} {collection_name} {collection_symbol} {total_token_supply} {ownership_mode} {nft_kind} {nft_identifier} {nft_holder_mode} {minting_mode} {metadata_mutability} {burn_mode} {nft_metadata_kind}'.format(
            chain_name=chain_name,
            node_address=node_address,
            secret_key=secret_key,
            payment_amount=payment_amount,
            collection_name=default['name'],
            collection_symbol=default['sym'],
            total_token_supply=default['supply'],
            ownership_mode=default['ownership'],
            nft_kind=default['kind'],
            nft_identifier=default['identifier'],
            nft_holder_mode=default['hold'],
            minting_mode=default['mint'],
            metadata_mutability=default['mutable'],
            burn_mode=default['burn'],
            nft_metadata_kind=default['meta']
            )
        # Workaround because of Json escape string
        with open('../bash-scripts/custom-template.sh', 'r') as template_file:
            content = template_file.read()
            new_content = content.replace('[JSON_SCHEMA]', default['json'])
            dump_json_schema(new_content)
        os.system(call)
    else:
        call = '../bash-scripts/temp.sh {chain_name} {node_address} {secret_key} {payment_amount} {collection_name} {collection_symbol} {total_token_supply} {ownership_mode} {nft_kind} {nft_identifier} {nft_holder_mode} {minting_mode} {metadata_mutability} {burn_mode} {nft_metadata_kind}'.format(
            chain_name=chain_name,
            node_address=node_address,
            secret_key=secret_key,
            payment_amount=payment_amount,
            collection_name=default['name'],
            collection_symbol=default['sym'],
            total_token_supply=default['supply'],
            ownership_mode=default['ownership'],
            nft_kind=default['kind'],
            nft_identifier=default['identifier'],
            nft_holder_mode=default['hold'],
            minting_mode=default['mint'],
            metadata_mutability=default['mutable'],
            burn_mode=default['burn'],
            nft_metadata_kind=default['meta']
            )
        with open('../bash-scripts/custom-template.sh', 'r') as template_file:
            content = template_file.read()
            new_content = content.replace('[JSON_SCHEMA]', '')
            dump_json_schema(new_content)
        os.system(call)

def get_deploy(args):
    if not args.deploy_hash or not args.node_address:
        print('Missing Mandatory arguments!')
        return False
    args = parser.parse_args()
    res = subprocess.check_output(['../bash-scripts/get-deploy.sh', args.deploy_hash, args.node_address])
    res = res.decode('utf-8')
    print('Installation Status: ', res)
    return json.loads(res)
def query_account_named_keys(args):
    if not args.node_address or not args.account_key:
        print('Missing Mandatory arguments!')
        return False
    # Get state root hash
    res = subprocess.check_output(['../bash-scripts/get-state-root-hash.sh', args.node_address])
    res = res.decode('utf-8')
    srh = json.loads(res)['result']['state_root_hash']
    # Use state root hash to query account
    acc = subprocess.check_output(['../bash-scripts/query-account-named-keys.sh', args.node_address, srh, args.account_key])
    acc = acc.decode('utf-8')
    # Get account's named keys
    named_keys = json.loads(acc)['result']['stored_value']['Account']['named_keys']
    print(colored('Account named keys: ', 'yellow'), named_keys)
    return named_keys

def get_contract_by_name(args):
    # default name: cep78_contract_hash_casper_collection
    if not args.contract_name:
        print('Missing Mandatory arguments!')
        return False
    named_keys = query_account_named_keys(args)
    if named_keys == False:
        return False
    for contract in named_keys:
        if contract['name'] == args.contract_name:
            contract_hash = contract['key']
            print(colored('Contract Hash found: ', 'green') + contract_hash)
            return contract_hash
    print('Contract does not exist!')
    return False


# Parse and call functions
args = parser.parse_args()

if args.function == 'install':
    install(args)

if args.function == 'install-status':
    get_deploy(args)

if args.function == 'query-account-named-keys':
    query_account_named_keys(args)

if args.function == 'get-contract-by-name':
    get_contract_by_name(args)
