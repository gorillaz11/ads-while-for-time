from os import system
from time import sleep
ads=[
"shave me",
"please",
"show me",
]
ads_duration=[
1.0,
8.0,
3.0
]

while True:
        
        ad=ads.pop(0)
        ad1=ads_duration.pop(0)
        print(">>",ad,"<<")
        
        sleep(ad1)
        ads_duration.append(ad1)
        ads.append(ad)
    