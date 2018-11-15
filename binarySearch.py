from random import randint

class Array:    # the Array class
    def __init__(self, length, resolution):
        self.length = length
        self.resolution = resolution


    def makeArray(self):
        return [i for i in range(self.resolution, (self.resolution * self.length)+1, self.resolution)]


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

    
    def search(self, item):     # modelled after the successive approximation register ADC :)
        randomIndex = randint(0, self.length - 1)   # first 'guess'
        randomItem = self.array[randomIndex]
        self.count = 0      # reset count for every time search() is called

        if (item == self.array[0]):     # compare item with first and last elements. For the tests ;)
            return {"count": self.count, "index": 0}
        elif (item == self.array[self.length-1]):
            return {"count": self.count, "index": self.length-1}

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
