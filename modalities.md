# Modalities
Summarized overview of [this](https://github.com/casper-ecosystem/cep-78-enhanced-nft/blob/dev/README.md):

1. __--ownership-mode__

| Ownership    | u8        |
|--------------|-----------|
| Minter       | 0         |
| Assigned     | 1         |
| Transferable | 2         |

2. __--nft-kind__

| NFTKind  | u8            |
|----------|---------------|
| Physical | 0             |
| Digital  | 1             |
| Virtual  | 2             |

3. __--nft-holder-mode__

| NFTHolderMode | u8       |
|---------------|----------|
| Accounts      | 0        |
| Contracts     | 1        |
| Mixed         | 2        |

4. __--minting-mode__

| MintingMode | u8         |
|-------------|------------|
| Installer   | 0          |
| Public      | 1          |

5. __--metadata-kind__

| NFTMetadataKind | u8     |
|-----------------|--------|
| CEP78           | 0      |
| NFT721          | 1      |
| Raw             | 2      |
| CustomValidated | 3      |

6. __--nft-identifier__
note: this should be changed to __identifier_mode__ for naming to be consistent,

| NFTIdentifierMode | u8   |
|-------------------|------|
| Ordinal           | 0    |
| Hash              | 1    |

7. __--metadata-mutability__

| MetadataMutability | u8  |
|--------------------|-----|
| Immutable          | 0   |
| Mutable            | 1   |

8. __--burn-mode__

| BurnMode    | u8         |
|-------------|------------|
| Burnable    | 0          |
| NonBurnable | 1          |
