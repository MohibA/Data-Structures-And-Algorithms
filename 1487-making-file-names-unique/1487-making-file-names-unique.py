class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        hashmap = {}
        
        for name in names:
            new_name = name
            
            if name in hashmap:
                k = hashmap[name]
            
                while new_name in hashmap:
                    k+= 1
                    new_name = f'{name}({k})'
                hashmap[name] = k
            hashmap[new_name] = 0
        return hashmap.keys()
        