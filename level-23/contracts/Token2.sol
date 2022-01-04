// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Token2 is ERC20 {
    constructor() public ERC20("Token2", "TK2") {
        _mint(msg.sender, 100_000_000 * (10**uint256(decimals())));
    }
}
