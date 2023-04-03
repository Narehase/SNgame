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
