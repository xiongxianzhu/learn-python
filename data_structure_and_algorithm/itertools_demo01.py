# coding: utf-8

import itertools


def permutation(arr, n):
    """ 排列算法 """
    return list(itertools.permutations(arr, n))


def combination(arr, n):
    """ 组合算法 """
    return list(itertools.combinations(arr, n))


def go():
    """ 
        请将4, 5, 6, 7, 9, 19六个数分别填入A-F空白框中， 每个数在每条算式中只能填一次。
        满足： A + B - C = D - E - F

    """
    arr = [4, 5, 6, 7, 9, 19]
    all_list = permutation(arr, 6)
    count = 0
    for one_list in all_list:
        if one_list[0] + one_list[1] - one_list[2] == \
            one_list[3] - one_list[4] - one_list[5]:
            # print "%s + %s - %s = %s - %s - %s" % tuple(i for i in one_list)
            # print('{0[0]} + {0[1]} - {0[2]} = {0[3]} - {0[4]} - {0[5]}'.format(one_list))
            print('{0[0]:>2} + {0[1]:>2} - {0[2]:>2} = {0[3]:>2} - {0[4]:>2} - {0[5]:>2}'.format(one_list))
            count += 1
    print "共有%s种排列的写法。" % count

if __name__ == "__main__":
    go()