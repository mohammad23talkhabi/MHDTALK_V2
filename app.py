import random
import requests

URL = "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/All_Configs_Sub.txt"

COUNT = 200

print("Downloading...")

text = requests.get(URL, timeout=30).text

configs = []

for line in text.splitlines():

    line = line.strip()

    if line:
        configs.append(line)

configs = list(dict.fromkeys(configs))

print("Total:", len(configs))

if len(configs) > COUNT:
    configs = random.sample(configs, COUNT)

with open("sub.txt", "w", encoding="utf-8") as f:

    for c in configs:
        f.write(c + "\n")

print("Done.")
