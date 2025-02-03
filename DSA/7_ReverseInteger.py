def reverse( x: int) -> int:
        ans_str = []
        remainder = None
        num = abs(x)
        ans_int = None

        if x == 0:
            return 0

        while num != 0:
            remainder = num % 10
            ans_str.append(str(remainder))
            num = int (num / 10)
        
        print(ans_str)

        trailing = True

        for i in range(len(ans_str)):
             if ans_str[i] != '0':
                  trailing = False
             if ans_str[i] == '0' and trailing == True:
                  ans_str[i] = ''
        print(ans_str)

        ans_int = int(''.join(ans_str))   
        print(ans_int)

        if -2**31 > ans_int or ans_int > 2**31 - 1:
             return 0
        if ans_int < 0:
            return -1 * ans_int
        else:
            return ans_int
        
print(reverse(1534236469))
        
