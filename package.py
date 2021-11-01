# Ryan Zeigler
# Student ID: 001473355


'''
This is a class that represents a package on a delivery truck.

Space complexity = O(1)
Time Complexity = O(1)
'''
class Package:

    # Initializing the package attributes so that they can be accessed externally
    packageId = -1
    packageDeliveryAddress = -1
    packageDeliveryCity = -1
    packageDeliveryState = -1
    packageDeliveryZip = -1
    packageDeliveryDeadline = -1
    packageWeight = -1
    packageSpecialNotes = -1
    packageDeliveredStatus = -1
    packageTimeDelivered = -1


    '''
    Constructor for the package object

    Space complexity = O(1)
    Time complexity = O(1)
    '''
    def __init__(self, packageId, packageDeliveryAddress, packageDeliveryCity, packageDeliveryState, packageDeliveryZip, packageDeliveryDeadline, packageWeight, packageSpecialNotes, packageDeliveredStatus, packageTimeDelivered):
        self.packageId = packageId
        self.packageDeliveryAddress = packageDeliveryAddress
        self.packageDeliveryCity = packageDeliveryCity
        self.packageDeliveryState = packageDeliveryState
        self.packageDeliveryZip = packageDeliveryZip
        self.packageDeliveryDeadline = packageDeliveryDeadline
        self.packageWeight = packageWeight
        self.packageSpecialNotes = packageSpecialNotes
        self.packageDeliveredStatus = packageDeliveredStatus
        self.packageTimeDelivered = packageTimeDelivered


    '''
    Returns the package object

    Space complexity = O(1)
    Time complexity = O(1)
    '''
    def __str__(self):
         return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.packageId, self.packageDeliveryAddress,
                                                   self.packageDeliveryCity, self.packageDeliveryState,
                                                   self.packageDeliveryZip, self.packageDeliveryDeadline,
                                                   self.packageWeight, self.packageSpecialNotes, self.packageDeliveredStatus, self.packageTimeDelivered)


