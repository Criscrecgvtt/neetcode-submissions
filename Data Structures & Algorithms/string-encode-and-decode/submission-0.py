class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            delimiter = s.find('#', i)
            length = int(s[i:delimiter])
            res.append(s[delimiter + 1 : delimiter + 1 + length])
            i = delimiter + 1 + length
        return res