// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Attack is ERC20 {
    constructor() public ERC20("Attack", "ATK") {
        _mint(msg.sender, 400 * (10**uint256(decimals())));
    }
}
