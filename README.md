## Ethernaut using Brownie/Python3

![Ethernaut](ethernaut.png)

First, create a Infura Rinkeby project https://infura.io/dashboard and add the https endpoint to the .env file.

* Change directory to a specific level AND update `brownie-config.yaml` with the Ethernaut instance address:

```
cd level-25
```

* To run locally using mock contracts:

```
brownie run scripts/attack.py
```

* To run via the Rinkeby Testnet:

```
brownie run scripts/attack.py --network rinkeby
```



