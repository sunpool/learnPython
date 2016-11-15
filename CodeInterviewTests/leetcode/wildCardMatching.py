target = "afbcacb"
pat = "a*acb"

target = "xxy"
pat = "x?y"

# Dynamic programming
sol = [False] * (len(target) + 1)
sol[0] = True
for ip, pStr in enumerate(pat):
    if pStr == "*":
        for it in xrange(1, len(target)):
            sol[it] = sol[it - 1] or sol[it]
    else:
        # for it, tStr in enumerate(target):
        for it in xrange(len(target), 0, -1):
            # if target[it - 1] == pStr or pStr == "?":
            #     sol[it] = sol[it - 1]
            # else:
            #     sol[it] = False
            sol[it] = sol[it - 1] and (target[it - 1] == pStr or pStr == "?")
        sol[0] = False

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

    print ip == len(pat)
    return ip == len(pat)


wildcardMatching(target, pat)
