S = input()
weather = ["Sunny", "Cloudy", "Rainy"]
print(weather[(weather.index(S)+1) % 3])
