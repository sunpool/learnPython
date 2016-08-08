
target = "afbcacb"
pat = "a*acb"
print len(pat)
# Dynamic programming
# sol = list[]

# quick switches
def wildcardMatching( target, pat ):
    match = True
    match_target_id, match_pattern_id = -1, -1

    it = ip = 0
    # for it, t in enumerate(target):
    while it < len(target) and match:
        t = target[it]

        if ip < len(pat) and (t == pat[ip] or pat[ip] == "?"):
            it += 1     # python does not have operator ++ -- ?
            ip += 1
        elif ip < len(pat) and pat[ip] == "*":
            match_target_id, match_pattern_id = it, ip
            ip += 1
        elif match_target_id != -1:
            match_target_id += 1        # forward by only 1 step
            ip = match_pattern_id + 1   # reset to last * position + 1
            it = match_target_id
        else:
            match = False

    print match, ip
    while ip < len(pat) and match:
        if pat[ip] != "*":
            match = False
        ip += 1

    print match
    return match

target = "afbcacb"
pat = "a*bcb"
print len(pat)

wildcardMatching( target, pat )
