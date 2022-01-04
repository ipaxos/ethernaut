from brownie import Instance, network
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        instance = Instance.deploy("ethernaut0", {"from": account})

    else:

        web3 = Web3(
            config["networks"][network.show_active()]["infura"]
        )

        instance = Contract.from_abi(
            Instance._name,
            config["networks"][network.show_active()]["instance"],
            Instance.abi,
        )

    print(instance.info())
    print(instance.info1())
    print(instance.info2("hello"))
    print(instance.infoNum())
    print(instance.info42())
    print(instance.theMethodName())
    print(instance.method7123949())
    print(instance.password())
    instance.authenticate(instance.password()).wait(1)


def main():
    attack()
