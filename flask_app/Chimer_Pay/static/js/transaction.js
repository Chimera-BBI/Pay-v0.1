

// get parameters

function get_send_parameters() {

    para = {
        // Set the 'from' address to the first account in the list
        from: accounts[0],
        // Set the 'to' address
        to: '0x2f318C334780961FB129D2a6c30D0763d9a5C970',
        // Set the value to send in wei
        value: '0x29a2241af62c0000',
        // Set the gas price in wei
        gasPrice: '0x09184e72a000',
        // Set the gas limit
        gas: '0x2710',
    };

    return para

}




function SendEth(accounts) {


    para = get_send_parameters(accounts);
    // Send a request to the Ethereum network to send a transaction

    ethereum.request({ method: 'eth_sendTransaction', params: [para], })
        // Log the transaction hash if the request is successful
        .then((txHash) => console.log(txHash))
        // Log the error if the request fails
        .catch((error) => console.error);

}





const sendEthButton = document.querySelector('.sendEthButton');



// Add click event listener to the send Ethereum button
sendEthButton.addEventListener('click', () => { SendEth(accounts); });

