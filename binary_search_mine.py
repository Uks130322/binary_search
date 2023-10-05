list = [3, 5, 7, 9, 11, 13, 14, 16, 19]


def find_value(nums, value):
    if nums:
        first = 0
        last = len(nums) - 1
        return slicing(nums, value, first, last)
    else:
        return False


def slicing(nums, value, first, last):
    middle = first + (last - first) // 2
    print (first, middle, last)
    if nums[middle] == value:
        return True
    elif first <= last:
        if nums[middle] > value:
            return slicing(nums, value, first, middle - 1)
        else:
            return slicing(nums, value, middle + 1, last)
    else:
        return False


def find_value6(nums, value):   #0.18s

    import math

    first = 0
    last = len(nums) - 1
    if nums:
        for index in range(math.ceil(math.log2(len(nums))) + 1):
            middle = first + (last - first) // 2
            if nums[middle] == value:
                return True
            elif nums[middle] > value:
                last = middle - 1
            else:
                first = middle + 1
    return False


def find_value5(nums, value):   #0.15s

    first = 0
    last = len(nums) - 1
    middle = (last - first) // 2
    if nums and nums[middle] == value:
        return True
    while first <= last:
        middle = first + (last - first) // 2
        if nums[middle] == value:
            return True
        elif nums[middle] > value:
            last = middle - 1
        else:
            first = middle + 1
    return False


def find_value4(nums, value):   #0.15s

    import math

    first = 0
    last = len(nums) - 1
    if nums:
        for index in range(math.ceil(math.log2(len(nums))) + 1):
            middle = first + (last - first) // 2 + last % 2
            if middle > len(nums) - 1:
                return False
            else:
                if nums[middle] == value:
                    return True
                elif nums[middle] > value:
                    last = middle - middle % 2
                else:
                    first = middle + middle % 2 - last % 2
        return False
    return False


def find_value3(nums, value):   #0.16s

    first = 0
    middle = 1
    last = len(nums) - 1
    while nums and not (first == middle == last):
        middle = first + (last - first) // 2 + last % 2
        if nums[middle] == value:
            return True
        elif nums[middle] > value:
            last = middle - middle % 2
        else:
            first = middle + middle % 2 - last % 2
    return False


def find_value2(nums, value):   #0.18s

    new_list = nums
    middle = len(new_list)
    while middle and new_list:
        middle = middle // 2
        if new_list[middle] == value:
            return True
        elif new_list[middle] > value:
            new_list = new_list[0:middle]
        else:
            new_list = new_list[(middle + middle % 2):len(new_list)]
    return False
