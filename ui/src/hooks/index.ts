import { ethers } from "ethers";
import { Contract } from "@ethersproject/contracts";
import { useContractCall, useContractFunction } from "@usedapp/core";
import Countabi from "../abi/Count.json";
import { countContractAddress } from "../contracts";


const {abi} = Countabi
const contractInterface = new ethers.utils.Interface(abi) 
//const countContractInterface = new ethers.utils.Interface(countabi);
const contract = new Contract(countContractAddress, contractInterface);

export function useCount() {
  const [count]: any =
    useContractCall({
      abi: contractInterface,
      address: countContractAddress,
      method: "count",
      args: [],
    }) ?? [];
  console.log(count);
  return count;
}

export function useIncrement() {
  const { state, send } = useContractFunction(contract, "incrementCount", {});
  return { state, send };
}

export function useSetCount() {
  const { state, send } = useContractFunction(contract, "setCount", {});
  return { state, send };
}

export function useContractMethod(methodName: string) {
  const { state, send } = useContractFunction(contract, methodName, {});
  return { state, send };
}
