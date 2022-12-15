import itertools

class sort:

    def __init__(self) -> None:
        pass

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)


    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if self.InRightOrderLists(left[i], right[j]) == 1:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def InRightOrderLists(self, firstList, secondList, result = 0):

        for i,j in itertools.zip_longest(firstList, secondList):
            # print(i,j)

            #base case
            if result == -1 or result == 1:
                pass

            elif isinstance(i, int) == True and isinstance(j, int) == True:
                if j == i:
                    pass
                elif j < i:
                    result = -1
                    return result
                else:
                    result = 1
                    return result

            elif i == None:
                result = 1
                return result
            elif  j == None:
                result = -1
                return result
            
            elif isinstance(i, list) == True and isinstance(j, list) == True:
                result = self.InRightOrderLists(i, j, result)   

            elif isinstance(i, list) == True and isinstance(j, int) == True:
                j = [j]
                result = self.InRightOrderLists(i, j, result) 

            elif isinstance(i, int) == True and isinstance(j, list) == True:
                i = [i]
                result = self.InRightOrderLists(i, j, result) 

        return result