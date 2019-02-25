_x = 'global'
_arr = [1, 2, 3, 4]
def fun1():
    print(_x)
    print(_arr)

def fun2():
    _arr[1] = 0
    _x = 'new'
    print(_x)

class Class1:

    def fun1(self, arr):
        self.fun2(arr)
        print(arr)

    def fun2(self, nums):
        nums[1] = 0
        print(nums)


# fun2()
# print(_x)
Class1().fun1([6,1,5,2])