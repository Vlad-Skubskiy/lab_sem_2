def kmp_search(text: str, needle: str) -> list[int]:
    def find_sufix_and_prefix(pattern: str) -> list[int]:
        p = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[length] == pattern[i]:
                length += 1
                p[i] = length
                i += 1
            else:
                if length != 0:
                    length = p[length - 1]
                else:
                    p[i] = 0
                    i += 1
        return p

    if not needle or not text:
        return []

    suf_pref = find_sufix_and_prefix(needle)
    result = []

    i = 0
    j = 0

    while i < len(text):
        if text[i] == needle[j]:
            i += 1
            j += 1
            if j == len(needle):
                result.append(i - j)
                j = suf_pref[j - 1]

        elif i < len(text) and text[i] != needle[j]:
            if j > 0:
                j = suf_pref[j - 1]
            else:
                i += 1
    
    return result

text = "abc ab c abca"
needle = "abca"

positions = kmp_search(text, needle)
print(positions)