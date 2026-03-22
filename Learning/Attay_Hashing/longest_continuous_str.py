strr = "abcab"
max_len = 0
max_str = ""
all_max_sub_str = []
sett = set()
l = 0

for r in range(len(strr)):
    while strr[r] in sett:
        sett.remove(strr[l])
        l+=1
    
    sett.add(strr[r])

    if r - l+1 > max_len:
        max_len = r-l+1
        max_str = strr[l:r+1]
        all_max_sub_str = [max_str]
    elif r-l+1 == max_len:
        max_str = strr[l:r+1]
        if not all_max_sub_str in max_str:
            2008
            2
            all_max_sub_str.append(max_str)

print(max_len,max_str,all_max_sub_str)