# Workflow
This is a temporary solution that will be deprecated once casper contracts 
produce json artifacts. 

Last updated: 20.02.2023

# Intro
Install an NFT contract with a single command!

<img width="600" alt="Screenshot 2023-02-19 at 01 36 56" src="https://user-images.githubusercontent.com/49498646/219905720-f789c010-a3ef-4fd7-9b4b-86660d319eff.png">


This python-tool makes installing ( and using ) the Casper NFT Standard Cep-78 easier for developers. You can quickly install an instantiation of the contract by just calling a python script with many default modalities. This repository includes a bunch of bash scripts and a python argparser to call them. When using casper-client directly, there are many mandatory arguments that one has to type out for every instance of the Cep-78 standard. This tool works with a default configuration where all changes are optional and can be supplied to the python argparser as described below:

# Usage Examples
## 1. with [NCTL](https://github.com/casper-network/casper-node/blob/dev/utils/nctl/README.md)

To install the example, custom cep-78 contract, run this command:
```bash
$ python3 cep78.py --function install --secret-key PATH_TO_SECRET_KEY
```
This will install a cep-78 contract with these modalities:
```bash
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
```
Read more on modalities [here](https://github.com/casper-ecosystem/cep-78-enhanced-nft/blob/dev/README.md), or see the smaller overview below if you kind of know what modalities do in this context.

As you can see, the **json_schema** has to be an escaped string. Because of this we need to generate a temp bash file, that's then executed to install an instantiation of the custom-template.sh. Don't worry, you can easily escape your json schema using [this](https://jsontostring.com/) tool.

When using standard metadata (e.g. meta:0 or meta:1) (cep78 and NFT721 respectively), the json_schema defaults to an empty string ''.

Feel free to experiment with modalities as per the documentation. They are useful for configuring the conditions of the NFT contract such as blacklists, mutability, burning and many more. I categorized the modalites by how advanced they are in cep78.py:

```python
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
```
Note that not all of them are supported. Others will be added over time as this is a very recent project.


## 2. with [Testnet](https://testnet.cspr.live/)

If you want to install the contract on Testnet, you need to supply a different chain-name and node-address. Retrieve an active Testnet node from [this list](https://testnet.cspr.live/tools/peers)

An example could look like this:

```bash
$ python3 cep78.py --function install --secret-key PATH_TO_SECRET_KEY --node-address SOME_IP_FROM_LIST:7777 --chain-name casper-test
```


# Modalities
[Overview](https://github.com/jonas089/cep-78-helper/blob/master/modalities.md) for experienced users

[Details](https://github.com/casper-ecosystem/cep-78-enhanced-nft/blob/dev/README.md) for beginners

## What next?
You can learn how to query the contract and mint NFTs from [this medium article](https://medium.com/casperblockchain/casper-cep-78-enhanced-nft-standard-d954218626be). Querying and Calling capabilities of this repository that might help you in the process will be added below, once developed:

## Querying capabilities

1. Get deploy / check whether installation of contract was successful
```bash
$ python3 cep78.py --function deploy-status --deploy DEPLOY_HASH --node-address SOME_IP_ADDRESS:PORT
```

2. Query account / get contract hashes from named_keys
```bash
$ python3 cep78.py --function query-account-named-keys --account-key SOME_PUBLIC_KEY --node-address SOME_IP_ADDRESS:PORT
```
Returns and prints a list of account's named_keys. Use the account hashs of the installed contracts in the list to call functions on the contracts such as **mint**, **burn**, ...

3. Query _contract-hash_ by name
```bash
$ python3 cep78.py --function query-contract-by-name --contract-name SOME_CONTRACT_NAME --account-key SOME_PUBLIC_KEY --node-address SOME_IP_ADDRESS:PORT
```
Contract name can be the name of any named key. The default Contract's hash is stored under this name: _cep78_contract_hash_casper_collection_

## Calling capabilities
1. Mint an NFT by calling a contract via _contract-hash_

In this scenario, we mint a custom NFT using the default metadata schema from the example above:
```bash
r'''{\"properties\":{\"nft_name\":{\"name\":\"nft_name\",\"description\":\"name_of_nft\",\"required\":true},\"nft_description\":{\"name\":\"nft_description\",\"description\":\"description_of_nft\",\"required\":true},\"nft_name\":{\"name\":\"nft_url\",\"description\":\"url_of_nft\",\"required\":true}}}'''
```
With this schema, every NFT has a name, description and url. If you want to use a standard schema, like CEP-78 or NFT-721, consider changing the __--nft-kind__ to 0 or 1 respectively. If you do so, you don't need to supply a json-schema when installing the contract and the value will default to ''.

In our case the __--nft-kind__ is set to 3 => custom validated Metadata.

```bash
$ python3 cep78.py --function mint --chain-name CHAIN_NAME \
  --secret-key PATH_TO_SECRET_KEY \
  --payment-amount PAYMENT_AMOUNT --session-hash CONTRACT_HASH \
  --token-owner ACCOUNT_HASH --token-metadata META_DATA \
  --node-address SOME_IP_ADDRESS:PORT
```

Example _account-hash_:
```
account-hash-5a54f173e71d3c219940dcb9dfec222b024cd81aa7e0672de59ba5fab296448b
```
Example _token-metadata_:
```
'{\"nft_name\":\"DUMMY_NAME\",\"nft_description\":\"DUMMY_DESCRIPTION\",\"nft_url\":\"http://DUMMY_URL\"}'
```
