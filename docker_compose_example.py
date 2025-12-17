from redis import Redis

cashe = Redis(host='redis', port=6379)
cashe.set("example", 5)
print(int(cashe.get("example")) ** 2)