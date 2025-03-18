# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # flip it
        for i in range(len(image)):
            self.reverse(0, len(image[i]) - 1, image[i])
        # for inverting use XOR
        for row in range(len(image)):
            for col in range(len(image[0])):
                image[row][col] = image[row][col] ^ 1
        return image
    def reverse(self, start, end , row):
        while start <= end:
            row[start], row[end] = row[end], row[start]
            start += 1
            end -= 1