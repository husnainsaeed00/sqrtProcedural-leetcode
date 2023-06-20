import math

class Solution(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x

        left = 1
        right = x

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square > x:
                right = mid - 1
            else:
                left = mid + 1

        return right  # Return the rounded down value


# Example usage:
solution = Solution()
number = 3
square_root = math.floor(solution.mySqrt(number))
print("Square root of", number, "is:", square_root)
