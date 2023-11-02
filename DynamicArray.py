class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [None]*self.capacity # Setting the initial values for the array

    def get(self, i: int) -> int:
        return self.arr[i]

    # set the element at index i to n
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # will push the element n to the end of the array.
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length+=1

    # pop and return the element at the end of the array
    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.arr[self.length]

    # double the capacity of the array
    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [None] * self.capacity

        # Copy elements to new array
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr=new_arr

    # will return the number of elements in the array
    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity