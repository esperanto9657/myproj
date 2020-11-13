from collections import Counter

def answer(S):
    d = Counter(S)

    if len(S) <= 3:
        rem = int("".join(S)) % 8
        if rem == 0:
            return "Yes"
        else:
            return "No"
    else:
        for i in range(14, 125):
            s = Counter(str(8 * i))
            if not s - d:
                return "Yes"
        return "No"