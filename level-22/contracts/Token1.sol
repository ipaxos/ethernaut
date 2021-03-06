// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Token1 is ERC20 {
    constructor() public ERC20("Token1", "TK1") {
        _mint(msg.sender, 100_000_000 * (10**uint256(decimals())));
    }
}
