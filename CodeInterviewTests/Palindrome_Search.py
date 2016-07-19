a = "bcdabcebc"

# Rabin-Karp hash for string
def RabinKarp_hash(a):
    rk = []

    for i, char in enumerate(a):
        rk.append(ord(char) * 101 ** i)

    sumRK = [0]
    for i, num in enumerate(rk):
        # i += 1
        sumRK.append(rk[i] + sumRK[i])

    print sumRK, rk
    return sumRK

aRK = RabinKarp_hash(a)
s_str = "bc"
sRK = RabinKarp_hash(s_str)

found = []
for i, s in enumerate(aRK):
    i += len(s_str)
    if i <= len(a):
        match_rk = (aRK[i] - aRK[i-len(s_str)])/101**(i-len(s_str))
        print i, i-len(s_str), match_rk
    else:
        break
    if match_rk == sRK[len(s_str)]:
        found.append((i-len(s_str), i))

print
print "Search for", s_str, "in", a
print "Found: "
for r in found:
    print r, a[r[0]:r[1]]
