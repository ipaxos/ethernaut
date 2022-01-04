from brownie import Contract, Attack, GatekeeperTwo, network, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3

# https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/?ref=lbp
def decimalToBinary(n):

    if n > 1:
        # divide with integral result
        # (discard remainder)
        decimalToBinary(n // 2)

    print(n % 2, end="")


def attack():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        gatekeeper = GatekeeperTwo.deploy({"from": get_account(index=1)})

        attack = Attack.deploy(gatekeeper, {"from": account})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                Web3.HTTPProvider(config["networks"][network.show_active()]["infura"])
            )
        )

        gatekeeper = Contract.from_abi(
            GatekeeperTwo._name,
            config["networks"][network.show_active()]["gatekeeper"],
            GatekeeperTwo.abi,
        )

        attack = Attack.deploy(gatekeeper, {"from": account})

    print(f"Entered {attack.entered()}")
    print(f"Entrant {gatekeeper.entrant()}")


def main():
    attack()
