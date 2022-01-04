// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./MagicNum.sol";

contract Attack {
    MagicNum magicnum;
    address public owner;
    address public solver;
    bytes public answer;

    constructor(address payable _magicnum) public {
        magicnum = MagicNum(_magicnum);
        owner = msg.sender;
    }

    function attack() public {
        bytes
            memory bytecode = hex"600a600c600039600a6000f3602a60005260206000f3";
        bytes32 salt = 0;
        address _solver;

        assembly {
            _solver := create2(0, add(bytecode, 0x20), mload(bytecode), salt)
        }

        solver = _solver;
    }

    function whatIsTheMeaningOfLife() public {
        (, bytes memory data) = solver.call("whatIsTheMeaningOfLife()");
        answer = data;
    }
}
