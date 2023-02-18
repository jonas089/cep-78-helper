# Arguments
## Calling install
1. --ownership-mode
| Ownership    | u8  |
|--------------|-----|
| Minter       | 0   |
| Assigned     | 1   |
| Transferable | 2   |
2. --nft-kind
| NFTKind  | u8  |
|----------|-----|
| Physical | 0   |
| Digital  | 1   |
| Virtual  | 2   |
3. --nft-holder-mode
| NFTHolderMode | u8  |
|---------------|-----|
| Accounts      | 0   |
| Contracts     | 1   |
| Mixed         | 2   |
4. --minting-mode
| MintingMode | u8  |
|-------------|-----|
| Installer   | 0   |
| Public      | 1   |
5. --nft-kind
| NFTMetadataKind | u8  |
|-----------------|-----|
| CEP78           | 0   |
| NFT721          | 1   |
| Raw             | 2   |
| CustomValidated | 3   |
