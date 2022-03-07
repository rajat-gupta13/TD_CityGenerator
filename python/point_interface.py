class Point:
    """
        Point interface class that allows you to create a point object for every point on the grid
    """
    def __init__(self, index):
        self.index = index
        self.allocated = False
        self.max_height = 0  # still need to figure out how to use this for the camera path gen

    def Allocated(self):
        """
        Returns the current allocated status of the point object
        """
        return self.allocated

    def Allocate(self):
        """
        Allocates the point object
        """
        self.allocated = True

    def Deallocate(self):
        """
        Deallocates the point object
        """
        self.allocated = False

    def Index(self):
        """
        Returns the index of the current accessed point object
        """
        return self.index