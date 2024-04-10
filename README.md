# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution:滑點是預期價格跟實際價格之間的落差，他提供很多個池給予更有效率的交換方式，提供流動性來減少滑點。假設原本是20/10000的A幣和B幣，價格應該是1:500，假設要投入250的B換出A那麼只會換到0.487的A，根據20*10000=(20-x)(10250)，這樣算出來250/0.487=513，這樣就產生滑點。

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

