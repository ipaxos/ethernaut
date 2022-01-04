// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./SimpleToken.sol";

contract Recovery {
    //generate tokens

    address public newestSimpleToken; // Added for easy mocking

    function generateToken(string memory _name, uint256 _initialSupply) public {
        newestSimpleToken = address(
            new SimpleToken(_name, msg.sender, _initialSupply)
        );
    }
}
