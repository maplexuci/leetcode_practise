from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destination = paths[0][1]
        temp = {}
        if len(paths) == 1:
            return destination
        for i in range(1, len(paths)):
            if destination in temp:
                destination = temp[destination]
            elif paths[i][0] == destination:
                destination = paths[i][1]
                while destination in temp:
                    destination = temp[destination]
            else:
                temp[paths[i][0]] = paths[i][1]

        return destination
