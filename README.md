# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution
滑點是預期價格跟實際價格之間的落差，他提供很多個池給予更有效率的交換方式，提供流動性來減少滑點。假設原本是20/10000的A幣和B幣，價格應該是1:500，假設要投入250的B換出A那麼只會換到0.487的A，根據20*10000=(20-x)(10250)，這樣算出來250/0.487=513，這樣就產生滑點。

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution
如果沒有最低的限制那麼就可以創造一個很小的池子，這樣會使得波動性非常大，限制最小流動性才可以給市場提供穩定性

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution
保持恆定乘積可以最大幅度的減少交易對價格的影響，也相對的會鼓勵按照目前的比例投入資金有助於維持流動性的供應

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
在消費者下單要購買時這筆交易會先被放到mempool，但是被攻擊者發現了因為這個池子是公開的所有鏈上的礦工都看的到，他會抓準時機也就是在mempool時但未被打包成區塊之前以較低的價格收購消費者原本要買的，再以更高的價格賣給消費者從中獲利，消費者會被迫以比原本更高的價格買入

