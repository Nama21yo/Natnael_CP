# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)

        for path in paths:
            directory, *files = path.split()
            for file in files:
                # filename(content)
                file_content = file.split("(")
                fileName = file_content[0]
                content = file_content[1][:-1]
                content_map[content].append(directory + "/" + fileName)
        
        group_file = [value for key,value in content_map.items() if len(value) >= 2]
        
        return group_file