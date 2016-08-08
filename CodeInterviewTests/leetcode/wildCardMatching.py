
target = "abcbaacb"
pat = "a*bcb"
print len(pat)
# Dynamic programming
# sol = list[]

match = True
match_target_id, match_pattern_id = -1, -1

it = ip = 0
# quick switches

# for it, t in enumerate(target):
while it < len(target) and match:
    t = target[it]

    if ip < len(pat):
        p = pat[ip]
    else:
        break

    if t == p or p == "?":
        it += 1     # python does not have operator ++ -- ?
        ip += 1
    elif p == "*":
        match_target_id, match_pattern_id = it, ip
        ip += 1
    elif match_target_id != -1:
        match_target_id += 1
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
