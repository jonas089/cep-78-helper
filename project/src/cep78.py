from utils import dump_json_temp
import json, subprocess
class CEP78:
    def __init__(self, collection_name,
    collection_symbol, total_token_supply,
    ownership_mode, nft_kind, nft_identifier,
    nft_holder_mode, minting_mode, metadata_mutability,
    burn_mode, metadata_kind, json_schema):
        self.collection_name = collection_name
        self.collection_symbol = collection_symbol
        self.total_token_supply = total_token_supply
        self.ownership_mode = ownership_mode
        self.nft_kind = nft_kind
        self.nft_identifier = nft_identifier
        self.nft_holder_mode = nft_holder_mode
        self.minting_mode = minting_mode
        self.metadata_mutability = metadata_mutability
        self.burn_mode = burn_mode
        self.metadata_kind = metadata_kind
        self.json_schema = json_schema

    # Install the contract instance
    def install(self, chain_name, node_address, secret_key, payment_amount):
        call = ['../bash-scripts/temp.sh', chain_name, node_address, secret_key, payment_amount, self.collection_name, self.collection_symbol, self.total_token_supply, self.ownership_mode, self.nft_kind, self.nft_identifier, self.nft_holder_mode, self.minting_mode, self.metadata_mutability, self.burn_mode, self.metadata_kind]
        # Workaround because of Json escape string
        with open('../bash-scripts/custom-template.sh', 'r') as template_file:
            content = template_file.read()
            new_content = content.replace('[JSON_SCHEMA]', self.json_schema)
            dump_json_temp(new_content)
        res = subprocess.check_output(call).decode('utf-8')
        print("Result: ", res)
        if not 'Failed' in res:
            return json.loads(res)

    # Infromation about contract object
    def get_collection_name(self):
        return self.collection_name
    def get_total_token_supply(self):
        return self.total_token_supply
    def get_ownership_mode(self):
        return self.ownership_mode
    def get_nft_kind(self):
        return self.get_nft_kind
    def get_nft_identifier(self):
        return self.get_nft_identifier
    def get_nft_holder_mode(self):
        return self.nft_holder_mode
    def get_minting_mode(self):
        return self.minting_mode
    def get_metadata_mutability(self):
        return self.metadata_mutability
    def get_burn_mode(self):
        return self.burn_mode
    def get_metadata_kind(self):
        return self.metadata_kind
    def get_json_schema(self):
        return self.json_schema
