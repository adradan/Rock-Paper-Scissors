import re


usr = input().strip()
reRock = re.compile(r'\brock\b|\br\b', re.IGNORECASE)
rePaper = re.compile(r'\bpaper\b|\bp\b', re.IGNORECASE)
reScissors = re.compile(r'\bscissors\b|\bs\b', re.IGNORECASE)

reItems = [
    reRock,
    rePaper,
    reScissors
]

for search in reItems:
    reSearch = re.search(search, usr)
    if reSearch is not None:
        print(reSearch.group()[0])
        break