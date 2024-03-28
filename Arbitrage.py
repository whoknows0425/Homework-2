def find_arbitrage(liquidity, start_token="tokenB", start_balance=10.930035):
  """
  This function finds a profitable arbitrage path in a given liquidity dictionary.

  Args:
      liquidity: A dictionary representing liquidity between tokens. Key is a tuple
          of (tokenA, tokenB) and value is a tuple of (buy price, sell price).
      start_token: The token to start the arbitrage path from (default: "tokenB").
      start_balance: The starting balance in the start_token (default: 10.930035).

  Returns:
      A string representing the arbitrage path and remaining balance 
      (e.g., "path: tokenB->tokenA->tokenD->tokenB, tokenB balance=11.0").
      None if no profitable arbitrage path is found.
  """
  visited = set()  # Track visited tokens to avoid cycles
  current_token = start_token
  current_balance = start_balance
  path = [current_token]

  while True:
    if current_token in visited:
      return None  # Loop detected, no arbitrage

    visited.add(current_token)

    # Find the most profitable trade from current token
    best_sell_price = 0
    next_token = None
    for neighbor, (buy_price, sell_price) in liquidity.items():
      if neighbor[0] == current_token and sell_price > best_sell_price:
        best_sell_price = sell_price
        next_token = neighbor[1]

    # If no profitable trade found, return None
    if not next_token:
      return None

    # Update path and balance for the profitable trade
    path.append(next_token)
    current_balance = current_balance * best_sell_price

    # Check if arbitrage loop is complete (back to starting token)
    if next_token == start_token:
      return f"path: {'->'.join(path)}, {start_token} balance={current_balance:.4f}"

    # Move to the next token for the next iteration
    current_token = next_token

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

result = find_arbitrage(liquidity)
if result:
  print(result)
else:
  print("No profitable arbitrage path found.")
