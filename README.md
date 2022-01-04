## Ethernaut using Brownie/Python3

![Ethernaut](ethernaut.png)

First, create an Infura Rinkeby project at https://infura.io and add the project id and https endpoint to the .env file, along with your private key. 

* Change directory to a specific level AND update `brownie-config.yaml` with your Ethernaut instance address:

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



