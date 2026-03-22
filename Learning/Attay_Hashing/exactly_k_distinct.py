a = "abcbbade"
k = 4
l=0
cur = {}
all =[]
max_len = 0

for r in range(len(a)):
    cur[a[r]] = cur.get(a[r],0)+1

    while len(cur) != k:
        if len(cur) > k:
            cur[a[l]] -= 1
            if cur[a[l]] == 0:
                del cur[a[l]] 
        l+=1
    
    if r-l+1 >max_len:
        max_len = r-l+1
        all = [a[l:r+1]]
    elif r-l+1==max_len:
        if not a[l:r+1] in all:all.append(a[l:r+1])

print(all)