# Ryan Zeigler
# Student ID: 001473355


import csv
import datetime

from package import Package



'''
 This is a class that creates a hash table from a package CSV file.

 Space complexity = O(n)
 Time Complexity = O(n)
'''
class PackageHashTable:

    '''
    Constructor with optional initial capacity parameter.
    Assigns all buckets with an empty list.
    Initializes the hash table with empty bucket list entries.

    Space complexity = O(n)
    Time Complexity = O(n)
    '''
    def __init__(self, initial_capacity=39):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])


    '''
    Function that inserts a new item into the hash table.
    Updates the key if it is already in the bucket.
    If key is not already in the bucket, it will insert the item at the end of the bucket list.
        
    Space complexity = O(n)
    Time Complexity = O(n)
    '''
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = item
                return True
        key_value = [key, item]
        bucket_list.append(key_value)
        return True


    '''
    Function that searches for an item with matching key in the hash table.
    Returns the item if found, or None if not found.
        
    Space complexity = O(n)
    Time Complexity = O(n)
    '''
    def lookup(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]
        return None


    '''
    Function that removes an item with matching key from the hash table, if it is present.
        
    Space complexity = O(n)
    Time Complexity = O(n)
    '''
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])




'''
Function that loads the package data into the package hash table. 
    
Space complexity = O(n)
Time Complexity = O(n)
'''
def loadPackageData(filename):
    with open(filename) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)
        for package in packageData:
            packageId = int(package[0])
            packageDeliveryAddress = package[1]
            packageDeliveryCity = package[2]
            packageDeliveryState = package[3]
            packageDeliveryZip = package[4]
            packageDeliveryDeadline = package[5]
            packageWeight = package[6]
            packageSpecialNotes = package[7]
            packageDeliveredStatus = 'At the hub'
            packageTimeDelivered = datetime.time()

            # Package object
            p = Package(packageId, packageDeliveryAddress, packageDeliveryCity, packageDeliveryState, packageDeliveryZip, packageDeliveryDeadline, packageWeight, packageSpecialNotes, packageDeliveredStatus, packageTimeDelivered)

            # insert it into the hash table
            myHash.insert(packageId, p)


# Hash table instance
myHash = PackageHashTable()

# Load packages into hash table
loadPackageData('packages.csv')



