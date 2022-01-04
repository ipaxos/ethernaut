from brownie import Contract, Attack, MagicNum, network, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        magicnum = MagicNum.deploy({"from": get_account(index=1)})

        attack = Attack.deploy(magicnum, {"from": get_account(index=2)})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                Web3.HTTPProvider(config["networks"][network.show_active()]["infura"])
            )
        )

        magicnum = Contract.from_abi(
            MagicNum._name,
            config["networks"][network.show_active()]["magicnum"],
            MagicNum.abi,
        )

        attack = Attack.deploy(magicnum, {"from": account})

    attack.attack({"from": account}).wait(1)

    attack.whatIsTheMeaningOfLife().wait(1)

    print(f"What is the meaning of life? {int(attack.answer().hex(), 16)}")

    magicnum.setSolver(attack.solver(), {"from": account}).wait(1)


def main():
    attack()
