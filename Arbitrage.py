

liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}
def find_best_exchange_rate(liquidity, token_amount=5, start_token="tokenB", fee=0.003):
  """
  Finds the best exchange rate for converting to tokenB given the current liquidity,
  considering Uniswap V2 fees.

  Args:
      liquidity: A dictionary representing liquidity between tokens. Key is a tuple
          of (tokenA, tokenB) and value is a tuple of (buy price, sell price).
      token_amount: The amount of the starting token (default: 5).
      start_token: The starting token (default: "tokenB").
      fee: The Uniswap V2 fee (default: 0.003).

  Returns:
      A tuple representing the best exchange rate: (token, exchange_rate).
      None if no profitable exchange is found.
  """
  best_exchange_rate = None
  best_token = None

  for neighbor, (buy_price, sell_price) in liquidity.items():
    if neighbor[1] == start_token:  # Skip converting back to start_token
      continue

    # Calculate the amount of tokenB received after conversion, considering fee
    tokenB_amount_before_fee = token_amount * sell_price / buy_price
    tokenB_amount_after_fee = tokenB_amount_before_fee * (1 - fee)

    # Update best exchange rate if found a better one
    if tokenB_amount_after_fee > token_amount and (best_exchange_rate is None or tokenB_amount_after_fee > best_exchange_rate):
      best_exchange_rate = tokenB_amount_after_fee
      best_token = neighbor[1]

  return best_token, best_exchange_rate
