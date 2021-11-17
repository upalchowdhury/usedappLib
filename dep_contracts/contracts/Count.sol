// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;


contract Count {
    uint256 public count;

    function incrementCount() public {
        count++;
    }

    function setCount(uint256 _count) public {
        require(_count > 0);
        count = _count;
    }

        function takeTwoVariables(uint _valueA, uint256 _valueB) public payable {
        require(msg.value > 0);
        count = _valueA + _valueB;
    }


}