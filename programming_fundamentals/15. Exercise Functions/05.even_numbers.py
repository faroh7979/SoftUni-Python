numbers_client = list(map(int, input().split()))
result = list(filter(lambda x: x % 2 == 0, numbers_client))
print(result)
