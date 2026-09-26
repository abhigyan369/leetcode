class Solution:

  def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
    mp = {}
    for item in knowledge:
      mp[item[0]] = item[1]

    res = ""
    i = 0
    n = len(s)

    while i < n:
      if s[i] == '(':
        i += 1  # Skip open bracket '('

        # 1. Extract the complete key inside brackets first
        key = ""
        while i < n and s[i] != ')':
          key += s[i]
          i += 1

        # 2. Look up the key AFTER the loop finishes
        if key in mp:
          res += mp[key]
        else:
          res += '?'

        i += 1  # Skip close bracket ')'
      else:
        res += s[i]
        i += 1

    return res