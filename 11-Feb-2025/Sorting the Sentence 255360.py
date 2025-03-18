# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        # destructure the word and the number and tuple them
        index_place = []
        string_place = []
        s = s.split()
        for string in s:
            string_place.append(string[:-1])
            index_place.append(string[-1])
        
        
        tupled_list = sorted(list(zip(index_place,string_place)))

        return " ".join([s for num, s in tupled_list])


        