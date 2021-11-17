from brownie import accounts, network, config, Contract
#LinkToken, VRFCoordinatorMock, Contract
from web3 import Web3
import os, json, glob

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache", "mainnet-fork"]
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


# imagepath = "../images/outputdata/*.png"
# imageNumberMapping = {}

# def get_imagenumber(number,imagepath):
#     imagelist = glob.glob(imagepath)
#     counter = 0
#     for item in imagelist:
#         imageNumberMapping[counter]=item
#         counter = counter + 1
#     return imageNumberMapping[number]

def get_imagenumber(number):
    imageNumberMapping = {0:"train-0.png",1:"train-1.png",2:"train-2.png",3:"train-3.png",4:"train-4.png"}
    # imagelist = glob.glob(imagepath)
    # counter = 0
    # for item in imagelist:
    #     imageNumberMapping[counter]=item
    #     counter = counter + 1
    return imageNumberMapping[number]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])
    





