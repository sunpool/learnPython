target = "afbcacb"
pat = "a*acb"

target = "xxy"
pat = "xxz"

# Dynamic programming
sol = [False] * (len(target) + 1)
sol[0] = True
for ip, pStr in enumerate(pat):
    if pStr == "*":
        for it in xrange(1, len(target)+1):         # was missing "+ 1" in the range
            sol[it] = sol[it - 1] or sol[it]
        sol[0] = True                               # missing condition on sol[0]
    else:
        for it in xrange(len(target), 0, -1):
            # if target[it - 1] == pStr or pStr == "?":
            #     sol[it] = sol[it - 1]
            # else:
            #     sol[it] = False
            sol[it] = sol[it - 1] and (target[it - 1] == pStr or pStr == "?")
        sol[0] = False

print sol
print sol[len(target)]


# extreme way of expression
sol = [False] * (len(target) + 1)
sol[0] = True
for pStr in pat:
    for it in xrange(len(target), 0, -1):
        sol[it] = ((pStr == "*") and sol[it - 1] or sol[it]) or ((target[it - 1] == pStr or pStr == "?") and sol[it-1])
    sol[0] = pStr == "*"

print sol
print sol[len(target)]


# quick switches
def wildcardMatching(target, pat):
    # match = True
    match_target_id, match_pattern_id = -1, -1

    it = ip = 0
    # for it, t in enumerate(target):
    while it < len(target):
        t = target[it]

        if ip < len(pat) and (t == pat[ip] or pat[ip] == "?"):
            it += 1  # python does not have operator ++ -- ?
            ip += 1
        elif ip < len(pat) and pat[ip] == "*":
            match_target_id, match_pattern_id = it, ip
            ip += 1
        elif match_target_id != -1:
            match_target_id += 1  # forward by only 1 step
            ip = match_pattern_id + 1  # reset to last * position + 1
            it = match_target_id
        else:
            return False

    while ip < len(pat) and pat[ip] == "*":
        ip += 1

    return ip == len(pat)


print wildcardMatching(target, pat)
