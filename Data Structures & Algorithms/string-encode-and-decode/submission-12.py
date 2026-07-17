class Solution:

    # Schematic: num1_string1num2_string2 etc...
    def encode(self, strs: List[str]) -> str:

        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + "_" + s
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # Decoded output
        decoded_list = []

        # i = index of the string
        i = 0

        # Iterate through the string
        while i < len(s):

            # Extract the length
            len_str = []
            while s[i] != "_":
                len_str.append(s[i])
                i+=1;

            # Increment i for esc character
            i+=1;

            length = int("".join(len_str))

            decoded_list.append(s[i : i + length])

            i += length

        return decoded_list
            

