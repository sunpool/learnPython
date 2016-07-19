
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


def query_RK(aRK, sRK, str_len):
    found = []
    for i, s in enumerate(aRK):
        i += str_len
        if i <= len(a):
            match_rk = (aRK[i] - aRK[i-str_len])/101**(i-str_len)
            print i, i-str_len, match_rk
        else:
            break
        if match_rk == sRK:
            found.append((i-str_len, i))
    return found

a = "bcdabcebc"
s_str = "bc"

aRK = RabinKarp_hash(a)
sRK = RabinKarp_hash(s_str)[len(s_str)]

found = query_RK(aRK, sRK, len(s_str))

print
print "Search for", s_str, "in", a
print "Found: "
for r in found:
    print r, a[r[0]:r[1]]
