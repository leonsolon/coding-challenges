from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransomNote = Counter(ransomNote)
        count_magazine = Counter(magazine)
        for key, value in count_ransomNote.items():
            if key not in count_magazine:
                return False
            else:
                if value> count_magazine[key]:
                    return False
        return True