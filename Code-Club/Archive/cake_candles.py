candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))

tallest = max(candles)

answer = candles.count(tallest)

print(answer)



















