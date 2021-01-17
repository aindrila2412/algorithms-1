# 1233. Remove Sub-Folders from the Filesystem
"""
    Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.
    If a folder[i] is located within another folder[j], it is called a sub-folder of it.
    The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. 
    For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

    Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    Output: ["/a","/c/d","/c/f"]
    Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
"""
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Method 1 using startswith python gives better runtime but same space 
        folder.sort()
        final = [folder[0]]
        prev = folder[0] + "/"
        
        for index in range(1, len(folder), 1):
            if not folder[index].startswith(prev):
                final.append(folder[index])
                prev = folder[index] + "/"
        return final 
                
        # Method 2 -> Takes more runtime but same space 
        check_dict = dict()
        final = list()
        folder.sort() 
        for path in folder:
            temp = ""
            for i in range(len(path)):
                temp += path[i] 
                if temp in check_dict:
                    if len(path) > i:
                        if path[i+1] == "/":
                            temp = ""
                            break
                        else:
                            continue
                    else:
                        temp = ""
                        break         
            if len(temp) != 0:
                check_dict[temp] = 1
                final.append(temp)
        
        return final 