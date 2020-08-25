#coding: utf
from itertools import permutations

def solve(pb):
    nums = []
    res = []
    for one in pb:
        nums.append(str(one))
    for one1 in permutations(nums):
        for i in range(4):
            if i == 3 and eval(one1[1]) == 0:
                break
            first_part = fun(one1[0], one1[1], i)
            new1 = []
            new1.append(first_part)
            new1 += one1[2:]
            
            for one2 in permutations(new1):
                for j in range(4):
                    if j == 3 and eval(one2[1]) == 0:
                        break
                    second_part = fun(one2[0], one2[1], j)
                    new2 = []
                    new2.append(second_part)
                    new2 += one2[2:]
                    
                    for one3 in permutations(new2):
                        for k in range(3):
                            if k == 3 and eval(one3[1]) == 0:
                                break
                            last_value = fun(one3[0], one3[1], k)
                            if eval(last_value) < 24.01 and eval(last_value) > 23.99:
                                res.append(last_value)
    return list(set(res))

def fun(a, b, way):
    if way == 0:
        return '(' + a + '+' + b + ')'
    if way == 1:
        return '(' + a + '-' + b + ')'
    if way == 2:
        return '(' + a + '*' + b + ')'
    if way == 3:
        return '(float(' + a + ')/' + b + ')'

if __name__ == '__main__':
    res = solve([1,1,1,1])
    if len(res) != 0:
        ans = res[0].replace('float(', '')
        ans = ans.replace(')/', '/')
        print("Possible solution:")
        print(ans)
    else:
        print("No 24 solution for these numbers...")
