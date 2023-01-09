// get parameters

function get_send_parameters(accounts,send_to,send_value) {

    para = {
        // Set the 'from' address to the first account in the list
        from: accounts[0],
        // Set the 'to' address
        to: send_to,
        // Set the value to send in wei
        value: send_value,
        // Set the gas price in wei
        gasPrice: '0x09184e72a000',
        // Set the gas limit
        gas: '0x2710',

    };

    return para

}




function SendEth(accounts) {

    send_to = document.getElementsByName("to_address")[0].value;

    $.ajax({
        type: "POST",
        url: actionUrl,
        async: false,
        data: form.serialize(), // serializes the form's elements.
        success: function(data)
        {
          console.log(data);
            //alert(data); // show response from the php script.
        }
    });


    send_value = document.getElementsByName("cvalue")[0].value;
    send_value =  "0x" + Web3.utils.toBN(Web3.utils.toWei(send_value, "ether")).toString(16);
    para = get_send_parameters(accounts,send_to = send_to,send_value = send_value);
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

