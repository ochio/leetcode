class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        t = set()

        for i in range(len(words)):
            s = ""

            for j in range(len(words[i])):
                idx = ord(words[i][j]) - 97
                s += m[idx]

            t.add(s)

        return len(t)
