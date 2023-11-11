import starknet from 'starknet-library';

// Initialize Starknet and user
const starknetProvider = new starknet.StarknetProvider();
const userWallet = new starknet.UserWallet();

// NFT smart contract
const nftContractAddress = '0xabcdef1234567890';

// Function to mint a new NFT
async function mintNFT(metadataURI) {
    try {
        const txHash = await starknetProvider.invokeContract(userWallet, nftContractAddress, 'mint', [metadataURI]);
        console.log(`Minting NFT... Transaction: ${txHash}`);
        await starknetProvider.waitForTransactionConfirmation(txHash);
        console.log('NFT minted successfully!');
    } catch (error) {
        console.error(`Error minting NFT: ${error}`);
    }
}

// Function to transfer NFT to another user
async function transferNFT(tokenId, recipient) {
    try {
        const txHash = await starknetProvider.invokeContract(userWallet, nftContractAddress, 'transfer', [tokenId, recipient]);
        console.log(`Transferring NFT... Transaction: ${txHash}`);
        await starknetProvider.waitForTransactionConfirmation(txHash);
        console.log(`NFT transferred to ${recipient}`);
    } catch (error) {
        console.error(`Error transferring NFT: ${error}`);
    }
}

// Function to query NFT owner
async function getNFTOwner(tokenId) {
    try {
        const owner = await starknetProvider.queryContractView(nftContractAddress, 'getOwner', [tokenId]);
        console.log(`Owner of NFT #${tokenId}: ${owner}`);
    } catch (error) {
        console.error(`Error querying NFT owner: ${error}`);
    }
}

// Example usage of functions
mintNFT('https://metadata-url/nft123');
transferNFT(1, '0xrecipientaddress');
getNFTOwner(1);
