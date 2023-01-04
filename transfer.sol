pragma solidity ^0.6.0;

// This is the contract for a simple token
// It has a name, symbol, and total supply
// Users can transfer tokens to each other

contract SimpleToken {
    // Token name
    string public name;

    // Token symbol
    string public symbol;

    // Total number of tokens
    uint256 public totalSupply;

    // Mapping from addresses to balances
    mapping(address => uint256) public balanceOf;

    // Event for when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Constructor function
    constructor(string memory _name, string memory _symbol, uint256 _totalSupply) public {
        name = _name;
        symbol = _symbol;
        totalSupply = _totalSupply;
        balanceOf[msg.sender] = totalSupply;
    }

    // Function to transfer tokens
    function transfer(address _to, uint256 _value) public {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
    }
}
