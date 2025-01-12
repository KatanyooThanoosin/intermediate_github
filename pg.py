class tv:
    def __init__(self, width, length, brand, status = False):
        self.width = width
        self.length = length 
        self.brand = brand
        self.status = status
    
    def getWidth(self):
        return self.width
    
    def getBrand(self):
        return self.brand
    
    def setWidth(self, width):
        self.width = width
    
    def power(self):
        self.status = not self.status

    def __str__(self):
        return "This is " + self.brand + " TV."

samsungTV = tv(89, 50, "sony")
print(samsungTV.__width)