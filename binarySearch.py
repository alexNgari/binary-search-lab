#from random import randint
import math

class Array:    # the Array class
    def __init__(self, length, resolution):
        self.length = length
        self.resolution = resolution


    def makeArray(self):
        return [i for i in range(self.resolution, (self.resolution * self.length)+1, self.resolution)]

    # the following methods don't need any of the defined class attributes:
    @staticmethod
    def toTwenty():
        return Array(20, 1)


    @staticmethod
    def toForty():
        return Array(20, 2)


    @staticmethod
    def toOneThousand():
        return Array(100, 20)



class binarySearch:
    def __init__(self, length, resolution):
        self.binarySearch = Array(length, resolution)
        self.length = self.binarySearch.length
        self.resolution = self.binarySearch.resolution
        self.array = self.binarySearch.makeArray()
        self.count = 0

    
    def __getitem__(self, index):   # make binarySearch objects indexable
        return self.array[index]

    
    def search(self, item):
        self.array.sort()       # just to be sure
        minIndex = 0
        maxIndex = self.length - 1
        minItem = self.array[minIndex]
        maxItem = self.array[maxIndex]
        self.count = 0

        if item < minItem:  
            return {"count": self.count, "index": -1}
        if item > maxItem:
            return {"count": self.count, "index": -1}

        while 1:
            
            
            if (item == minItem) or (item == maxItem):  # check if item equals either of the boundary items
                if item == minItem:
                    return {"count": self.count, "index": minIndex}
                else:
                    return {"count": self.count, "index": maxIndex}
            
            if not (((item - minItem)% self.resolution == 0) and ((maxItem - item) % self.resolution == 0)):
                return {"count": self.count, "index": -1}

            if (item - minItem) > (maxItem - item):     # if item is in second half:
                minIndex = math.ceil((maxIndex + minIndex) / 2) # 'discard' first half
            elif (item - minItem) < (maxItem - item):   # if item is in first half
                maxIndex = math.ceil((maxIndex + minIndex) / 2)   # 'discard' second half
            else:
                return {"count": self.count, "index": int((minIndex + maxIndex)/2)} # item is in middle of remaining array space
                
            minItem = self.array[minIndex]
            maxItem = self.array[maxIndex]
            self.count += 1
    
    
'''
        # not binary search algorithm...emotionally attached; can't discard
    def search(self, item):     # modelled after the successive approximation register ADC :)
        randomIndex = randint(0, self.length - 1)   # first 'guess'
        randomItem = self.array[randomIndex]
        self.count = 0      # reset count for every time search() is called

        while 1:    # infinite loop
            error = randomItem - item  # calculate error
            if (error % self.resolution == 0): # checks if item is in array
                if error == 0: # if guess equals item
                    return {"count": self.count, "index": randomIndex}
                else:
                    randomIndex = randomIndex - int(error / self.resolution)  # adjust guess by error, then try again
                    if (randomIndex < self.length - 1): # check if calculated item index is out of range
                        randomItem = self.array[randomIndex]
                    else:
                        return {"count": self.count, "index": -1}

            else:
                return {"count": self.count, "index": -1}
            
            self.count += 1
    '''
    