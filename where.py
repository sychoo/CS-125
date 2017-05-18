
s = "banana"
i = 0
where = []
for ch in s:
    if ch == "a":
        where = where + [i]

    i = i + 1

print(where)