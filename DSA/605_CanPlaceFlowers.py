'''

Initial thoughts

    given n 

    looks at each index, 
    peek to its left, i - 1, if exists
    peek at it
    peek to its right, i + 1

    if everything is free, decrease n by 1

    at the end, if n != 0, return false else return true


'''

def canPlaceFlowers(flowerbed, n):

    for i in range(len(flowerbed)):
        
        if flowerbed[i] == 0:
            if i - 1 < 0:
                left = 0
            else:
                left = flowerbed[i - 1]
            
            if i + 1 > len(flowerbed) - 1:
                right = 0
            else:
                right = flowerbed[i + 1]
            
            if left == 0 and right == 0:
                n -= 1
                flowerbed[i] = 1
        print(f"i = {flowerbed[i]} left = {left}, right = {right}, {flowerbed}")


    return True if n <= 0 else False

print(canPlaceFlowers([0,0,1,0,0], 1))


