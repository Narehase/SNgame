import numpy as np
# import keyboard
import time
import msvcrt
# import pygame
import os
import json
os.system("cls")
os.system("printf \"\\e[100;0;0t\"")
# os.system("printf '\\033]50;0;0\\007\\033]1337;SetProfile=Square\\a'")
os.system("title Snake Game")

sn = []
length = 5
head = [0,0]

pain = 2
poin = 1
low = 0.5
point = 0

#   3 
# 0 # 2
#   1
def gos(x = 0,y = 0):
    print("\033[H\033[J")
    # print(f"\033[{x};{y}H",end="")
    # os.system("cls")
    # print()


def display(maps, point = 0):
    gos()
    pizz = ("#" * (maps.shape[0]+2 ))+ "\n#"
    for y in maps:
        for x in y:
            a = " "
            # a = "□"
            if x == 0:
                a = " "
            elif x > 0 and x < 1:
                a = "■"
            elif x == 1:
                a = "▤"
            else:
                a = "$"
            pizz+= a
        pizz+= "#\n#"
    pizz += ("#" * (maps.shape[0]+1 ))+ f"\n {point}"
    
    print(pizz)
def ful_up(na, pix = 10):
    xf =[]
    yf =[]
    for y in na:
        for i in range(pix):
            for x in y:
                for i in range(pix):
                    xf.append(x)
            yf.append(xf)
            xf =[]
    return yf

def len_sp(sn, lens:int):
    sn = sn[::-1][:lens][::-1]
    return sn

def Nuton(maps):
    # print(maps[1]+1)
    y=np.random.randint(0, maps.shape[0])
    x=np.random.randint(0, maps.shape[1])
    return [y,x]

def wig(poin = [0,0], poins = 0, maps = [], sn = [], nus = [], lens = 5 , point = 0):
    if poins == 1:
        a = [poin[0]+1,poin[1]]
    elif poins == 2:
        a = [poin[0],poin[1]+1]
    elif poins == 3:
        a = [poin[0]-1,poin[1]]
    elif poins == 0:
        a = [poin[0],poin[1]-1]
    # print(a)        
    try:
        for i in sn:
            if i == a:
                print("tail_Touch")
                raise
        if maps[a[0],a[1]] == 1:
            return False, a, lens, point
        if a[0] < 0 or a[1] < 0:
            raise
        if a[0] > maps.shape[0] or a[1] > maps.shape[1]:
            raise
        # print(nus[0])
        if nus[0] == a[0] and nus[1] == a[1]: 
            # print("apple")
            nus = Nuton(maps)
            lens += 1
            point += 1
            # print("apple")
    except:
        return False, a, nus, lens, point
    return True, a, nus, lens, point
_ = True
mapi = np.zeros([20,20])
nu = Nuton(mapi)

# f = open("desktop.json", encoding="utf-8")
# while True:
#     head = [0,0]
#     while _:
#         maps = mapi.copy()
#         for i in sn:
#             maps[i[0],i[1]] = low
#         maps[head[0],head[1]] = 1
        
#         maps[nu[0],nu[1]] = 2
#         display(maps, point)
#         hg = {}
#         hg["head"] = {"x" : head[1], "y": head[0]}
#         hg["p"] = poin
#         hg["apple"] = pain
#         hg["point"] = point
#         hg["len"] = length

#         with open('desktop.json', 'w', encoding='utf-8') as make_file:
#             json.dump(hg, make_file, indent="\t")
#         # if keyboard.read_event():
#         #     key = keyboard.read_key()
#         _ = False
#         time.sleep(0.2)

#         if msvcrt.kbhit():
#             _ = True
#             byte_arr = msvcrt.getche()
#             try:
#                 key = byte_arr.decode("utf-8")
#                 print(key)
#             except UnicodeDecodeError:
#                 print("WASD로만 플레이가 가능해요!")
#                 raise KeyError
#         #   3 
#         # 0 # 2
#         #   1
#         sn.append(head)
#         sn = len_sp(sn, length)
#         r_maps = np.array(ful_up(maps))
#         # print(f"{sn=}")
#         if _:
#             if key == "d":
#                 poin = 2
#             if key == "w":
#                 poin = 3
#             if key == "s":
#                 poin = 1
#             if key == "a":
#                 poin = 0
#         # print(nu)
#         _,head,nu, length, point = wig(head, poin, maps, sn, nus = nu, lens = length,point= point)
#     print("Game Over")
#     _ = True
#     point = 0
#     length = 5
#     sn = []
#     poin = 1
head = [0,0]
while _:
    maps = mapi.copy()
    for i in sn:
        maps[i[0],i[1]] = low
    maps[head[0],head[1]] = 1
    
    maps[nu[0],nu[1]] = 2
    display(maps, point)
    hg = {}
    hg["head"] = {"x" : head[1], "y": head[0]}
    hg["p"] = pain
    hg["apple"] = pain
    hg["point"] = point
    hg["len"] = length

    with open('desktop.json', 'w', encoding='utf-8') as make_file:
        json.dump(hg, make_file, indent="\t")
    # if keyboard.read_event():
    #     key = keyboard.read_key()
    _ = False
    time.sleep(0.2)

    if msvcrt.kbhit():
        _ = True
        byte_arr = msvcrt.getche()
        try:
            key = byte_arr.decode("utf-8")
            print(key)
        except UnicodeDecodeError:
            print("WASD로만 플레이가 가능해요!")
            raise KeyError
    #   3 
    # 0 # 2
    #   1
    sn.append(head)
    sn = len_sp(sn, length)
    r_maps = np.array(ful_up(maps))
    # print(f"{sn=}")
    if _:
        if key == "d":
            poin = 2
        if key == "w":
            poin = 3
        if key == "s":
            poin = 1
        if key == "a":
            poin = 0
    # print(nu)
    _,head,nu, length, point = wig(head, poin, maps, sn, nus = nu, lens = length,point= point)
print("Game Over")
