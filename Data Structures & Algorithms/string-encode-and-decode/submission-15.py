class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for s in strs:
            result += str(len(s)) + "_" + s
        
        return result

    def decode(self, s: str) -> List[str]:

        decoded_list = []

        i = 0

        while i < len(s):

            len_list = []
            while s[i] != "_":
                len_list.append(s[i])
                i+=1;
            i+=1;

            length = int("".join(len_list))

            decoded_list.append(s[i : i + length])

            i += length

        return decoded_list

        

        
