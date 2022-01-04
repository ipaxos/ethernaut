from brownie import network, accounts, config, Token

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])


def get_token_address():
    account = get_account()
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        token = Token.deploy(21000000, {"from": account})
        return token
    else:
        return config["networks"]["rinkeby"]["token"]


print(get_account())
