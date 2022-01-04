// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract Bomb {
    function initialize() external {
        selfdestruct(msg.sender);
    }
}
