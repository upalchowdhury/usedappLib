from scripts.helpful_scripts import (
    get_account
)
from brownie import Count, network, config


def deploy_and_create():
    account = get_account()

    counter = Count.deploy(
        # get_contract("vrf_coordinator"),
        # get_contract("link_token"),
        # config["networks"][network.show_active()]["keyhash"],
        # config["networks"][network.show_active()]["fee"],
        {"from": account},
    )
    #fund_with_link(counter.address)
    # creating_tx = counter.createCollectible({"from": account})
    # creating_tx.wait(1)
    #print("token  created!")
    return counter


def main():
    deploy_and_create()