# Encode and Decode Strings

Problem can be found in [here](https://leetcode.com/problems/encode-and-decode-strings/)!

### [Solution](/Array%20%26%20Hashing/271-EncodeandDecodeStrings/solution.py)

```python
class Codec:
    def encode(self, strs: List[str]) -> str:
        """ Encodes a list of strings to a single string """
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}#{s}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """ Decodes a single string to a list of strings """
        index = 0
        decoded_string = []

        while index < len(s):
            j = index
            while s[j] != "#":
                j += 1
            length = int(s[j-1])
            decoded_string.append(str[j+1:j+1+length])
            i = j + 1 + length

        return decoded_string
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)