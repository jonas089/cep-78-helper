# Usage Examples
This python-tool makes installing ( and using ) the Casper NFT Standard Cep-78 easier for developers. You can quickly install an instantiation of the contract by just calling a python script with many default modalities.

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
Summarized overview of [this](https://github.com/casper-ecosystem/cep-78-enhanced-nft/blob/dev/README.md):

1. --ownership-mode

| Ownership    | u8        |
|--------------|-----------|
| Minter       | 0         |
| Assigned     | 1         |
| Transferable | 2         |

2. --nft-kind

| NFTKind  | u8            |
|----------|---------------|
| Physical | 0             |
| Digital  | 1             |
| Virtual  | 2             |

3. --nft-holder-mode

| NFTHolderMode | u8       |
|---------------|----------|
| Accounts      | 0        |
| Contracts     | 1        |
| Mixed         | 2        |

4. --minting-mode

| MintingMode | u8         |
|-------------|------------|
| Installer   | 0          |
| Public      | 1          |

5. --metadata-kind

| NFTMetadataKind | u8     |
|-----------------|--------|
| CEP78           | 0      |
| NFT721          | 1      |
| Raw             | 2      |
| CustomValidated | 3      |

6. --nft-identifier
note: this should be changed to __identifier_mode__ for naming to be consistent,

| NFTIdentifierMode | u8   |
|-------------------|------|
| Ordinal           | 0    |
| Hash              | 1    |

7. --metadata-mutability

| MetadataMutability | u8  |
|--------------------|-----|
| Immutable          | 0   |
| Mutable            | 1   |

8. --burn-mode

| BurnMode    | u8         |
|-------------|------------|
| Burnable    | 0          |
| NonBurnable | 1          |

## What next?
You can learn how to query the contract and mint NFTs from [this medium article](https://medium.com/casperblockchain/casper-cep-78-enhanced-nft-standard-d954218626be). Querying and Calling capabilities of this repository that might help you in the process will be added below, once developed:

## Querying capabilities
1. Get deploy / check whether installation of contract was successful
```bash
$ python3 cep78.py --function install-status --deploy DEPLOY_HASH --node_address SOME_IP_ADDRESS:PORT
```
## Calling capabilities
