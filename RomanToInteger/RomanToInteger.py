class Solution:
    def romanToInt(self, s: str) -> int:
        # Map each Roman numeral to its integer value
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        
        for i in range(len(s)):
            # If the current numeral is smaller than the next one, subtract it
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
                total -= roman_map[s[i]]
            # Otherwise, add it
            else:
                total += roman_map[s[i]]
                
        return total

# Defining your input string
s = "MCMXCIV"

# Running your code and printing the output
sol = Solution()
output = sol.romanToInt(s)
print(output)  # This will print: 1994