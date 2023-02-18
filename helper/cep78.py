import os, argparse
parser = argparse.ArgumentParser(
            prog = 'ProgramName',
            description = 'What the program does',
            epilog = 'Text at the bottom of help')
parser.add_argument('-f', '--function')
def install():
    # Mandatory Arguments

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
    parser.add_argument('-hold', '--nft-holder-mode')
    parser.add_argument('-mint', '--minting-mode')
    parser.add_argument('-mutable', '--metadata-mutability')
    parser.add_argument('-burn', '--burn-mode')
    ## Advanced
    parser.add_argument('-json', '--json-schema')

    default = {
        'name':'casper_collection',
        'sym': 'cspr',
        'supply': str(1000000),
        'chain': 'casper-net-1', # NCTL DEFAULT
        'host': 'http:127.0.0.1:11101', # NCTL DEFAULT
        'key': './secret_key.pem',
        'gas': str(300000000000), # 300 CSPR Tokens
        'ownership': str(2),
        'kind': str(1),
        'hold': str(2),
        'mint': str(1),
        'mutable': str(0),
        'burn': str(1),
        'json': '{\"properties\":{\"nft_name\":{\"name\":\"nft_name\",\"description\":\"name_of_nft\",\"required\":true},\"nft_description\":{\"name\":\"nft_description\",\"description\":\"description_of_nft\",\"required\":true},\"nft_name\":{\"name\":\"nft_url\",\"description\":\"url_of_nft\",\"required\":true}}}'
    }

    args = parser.parse_args()

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
    if args.nft_holder_mode:
        default['hold'] = args.nft_holder_mode
    if args.minting_mode:
        default['mint'] = args.minting_mode
    if args.metadata_mutability:
        default['mutable'] = args.metadata_mutability
    if args.burn_mode:
        default['burn'] = args.burn_mode
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

    # Construct session arguments
    collection_name_arg = '''"collection_name:string='{name}'"'''.format(name=default['name'])
    collection_symbol_arg = '''"collection_symbol:string='{sym}'"'''.format(sym=default['sym'])
    total_token_supply_arg = '''"total_token_supply:u64='{supply}'"'''.format(supply=default['supply'])
    ownership_mode_arg = '''"ownership_mode:u8='{ownership}'"'''.format(ownership=default['ownership'])
    nft_kind_arg = '''"nft_kind:u8='{kind}'"'''.format(kind=default['kind'])
    nft_holder_mode_arg = '''"nft_holder_mode:u8='{hold}'"'''.format(hold=default['hold'])
    minting_mode_arg = '''"minting_mode:u8='{mint}'"'''.format(mint=default['mint'])
    metadata_mutability_arg = '''"metadata_mutability:u8='{mutable}'"'''.format(mutable=default['mutable'])
    burn_mode_arg = '''"burn_mode:u8='{burn}'"'''.format(burn=default['burn'])
    json_schema_arg = '''"json_schema:string='{json}'"'''.format(json=default['json'])

    # Assign other arguments
    chain_name = default['chain']
    node_address = default['host']
    secret_key = default['key']
    payment_amount = default['gas']

    return os.system("../bash-scripts/template.sh {chain_name} {node_address} {secret_key} {payment_amount} {collection_name} {collection_symbol} {total_token_supply} {ownership_mode} {nft_kind} {nft_holder_mode} {minting_mode} {metadata_mutability} {burn_mode} {json_schema}".format(chain_name=chain_name,
        node_address=node_address,
        secret_key=secret_key,
        payment_amount=payment_amount,
        collection_name=collection_name_arg,
        collection_symbol=collection_symbol_arg,
        total_token_supply=total_token_supply_arg,
        ownership_mode=ownership_mode_arg,
        nft_kind=nft_kind_arg,
        nft_holder_mode=nft_holder_mode_arg,
        minting_mode=minting_mode_arg,
        metadata_mutability=metadata_mutability_arg,
        burn_mode=burn_mode_arg,
        json_schema=json_schema_arg))

def get_deploy():
    parser.add_argument('-deploy', '--deploy-hash')
    parser.add_argument('-host', '--node-address')
    args = parser.parse_args()
    return os.system("../bash-scripts/get-deploy.sh {deploy} {host}".format(deploy=args.deploy_hash, host=args.node_address))


args = parser.parse_args()

if args.function == 'install':
    install()

if args.function == 'install-status':
    query_deploy()
