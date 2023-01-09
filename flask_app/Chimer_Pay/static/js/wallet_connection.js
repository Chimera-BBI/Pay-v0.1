

if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask is installed!');
}
else{
    console.log("no wallet available")
}

// Initialize the list of accounts
let accounts = [];


// Asynchronously get the accounts from the Ethereum network
async function getAccounts(accounts) {
    // Send a request to the Ethereum network to get the accounts
    accounts = await ethereum.request({ method: 'eth_requestAccounts' });
    const account = accounts[0];
    showAccount.innerHTML = account;
}


// Select the Ethereum enable button and send Ethereum button elements
const ethereumButton = document.querySelector('.enableEthereumButton');
const showAccount = document.querySelector('.showAccount');


// Add click event listener to the Ethereum enable button
ethereumButton.addEventListener('click', () => { getAccounts(); });

