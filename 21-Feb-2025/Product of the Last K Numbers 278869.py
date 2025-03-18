# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]
        self.after_zero = 0

    def add(self, num: int):
        if num == 0:
            # If num is 0, reset the cumulative products since multiplication
            # with 0 invalidates previous products
            self.prefix = [1]
            self.after_zero = 0
        else:
            self.prefix.append(self.prefix[self.after_zero] * num)
            self.after_zero += 1

    def getProduct(self, k: int) -> int:
        # Check if the requested product length exceeds the after_zero of the valid
        # product list
        if k > self.after_zero:
            return 0
        return (self.prefix[self.after_zero] // self.prefix[self.after_zero - k])