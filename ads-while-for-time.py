from os import system
from time import sleep
ads=[
"suck my dick",
"please",
"i need you to suck my dick",
]
ads_duration=[
3.0,
4.0,
5.0
]


while True:
    ad=ads.pop(0)
    ad1=ads_duration.pop(0)
    print(">>",ad,"<<")
    ad1=sleep
    ads_duration.append(ad1)
    ads.append(ad)
    