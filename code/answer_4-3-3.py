weather = ["Sunny", "Cloudy", "Rainy"]
S = input()
print(weather[(weather.index(S)+1) % 3])
