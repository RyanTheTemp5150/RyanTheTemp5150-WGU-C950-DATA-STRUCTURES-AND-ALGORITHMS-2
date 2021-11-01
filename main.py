# Ryan Zeigler
# Student ID: 001473355

import datetime
import packageHashTable


'''
This is a 2D array(array of arrays) that contains lists of the distance values.

Space complexity = O(n^2)
Time Complexity = O(n^2)
'''
distanceArray = [
    [0, 7.2, 3.8, 11, 2.2, 3.5, 10.9, 8.6, 7.6, 2.8, 6.4, 3.2, 7.6, 5.2, 4.4, 3.7, 7.6, 2, 3.6, 6.5, 1.9, 3.4, 2.4, 6.4,
     2.4, 5, 3.6],
    [7.2, 0, 7.1, 6.4, 6, 4.8, 1.6, 2.8, 4.8, 6.3, 7.3, 5.3, 4.8, 3, 4.6, 4.5, 7.4, 6, 5, 4.8, 9.5, 10.9, 8.3, 6.9, 10,
     4.4, 13],
    [3.8, 7.1, 0, 9.2, 4.4, 2.8, 8.6, 6.3, 5.3, 1.6, 10.4, 3, 5.3, 6.5, 5.6, 5.8, 5.7, 4.1, 3.6, 4.3, 3.3, 5, 6.1, 9.7,
     6.1, 2.8, 7.4],
    [11, 6.4, 9.2, 0, 5.6, 6.9, 8.6, 4, 11.1, 7.3, 1, 6.4, 11.1, 3.9, 4.3, 4.4, 7.2, 5.3, 6, 10.6, 5.9, 7.4, 4.7, 0.6,
     6.4, 10.1, 10.1],
    [2.2, 6, 4.4, 5.6, 0, 1.9, 7.9, 5.1, 7.5, 2.6, 6.5, 1.5, 7.5, 3.2, 2.4, 2.7, 1.4, 0.5, 1.7, 6.5, 3.2, 5.2, 2.5, 6,
     4.2, 5.4, 5.5],
    [3.5, 4.8, 2.8, 6.9, 1.9, 0, 6.3, 4.3, 4.5, 1.5, 8.7, 0.8, 4.5, 3.9, 3, 3.8, 5.7, 1.9, 1.1, 3.5, 4.9, 6.9, 4.2, 9,
     5.9, 3.5, 7.2],
    [10.9, 1.6, 8.6, 8.6, 7.9, 6.3, 0, 4, 4.2, 8, 8.6, 6.9, 4.2, 4.2, 8, 5.8, 7.2, 7.7, 6.6, 3.2, 11.2, 12.7, 10, 8.2,
     11.7, 5.1, 14.2],
    [8.6, 2.8, 6.3, 4, 5.1, 4.3, 4, 0, 7.7, 9.3, 4.6, 4.8, 7.7, 1.6, 3.3, 3.4, 3.1, 5.1, 4.6, 6.7, 8.1, 10.4, 7.8, 4.2,
     9.5, 6.2, 10.7],
    [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0, 4.8, 11.9, 4.7, 0.6, 7.6, 7.8, 6.6, 7.2, 5.9, 5.4, 1, 8.5, 10.3, 7.8,
     11.5, 9.5, 2.8, 14.1],
    [2.8, 6.3, 1.6, 7.3, 2.6, 1.5, 8, 9.3, 4.8, 0, 9.4, 1.1, 5.1, 4.6, 3.7, 4, 6.7, 2.3, 1.8, 4.1, 3.8, 5.8, 4.3, 7.8,
     4.8, 3.2, 6],
    [6.4, 7.3, 10.4, 1, 6.5, 8.7, 8.6, 4.6, 11.9, 9.4, 0, 7.3, 12, 4.9, 5.2, 5.4, 8.1, 6.2, 6.9, 11.5, 6.9, 8.3, 4.1,
     0.4, 4.9, 11, 6.8],
    [3.2, 5.3, 3, 6.4, 1.5, 0.8, 6.9, 4.8, 4.7, 1.1, 7.3, 0, 4.7, 3.5, 2.6, 2.9, 6.3, 1.2, 1, 3.7, 4.1, 6.2, 3.4, 6.9,
     5.2, 3.7, 6.4],
    [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.6, 5.1, 12, 4.7, 0, 7.3, 7.8, 6.6, 7.2, 5.9, 5.4, 1, 8.5, 10.3, 7.8,
     11.5, 9.5, 2.8, 14.1],
    [5.2, 3, 6.5, 3.9, 3.2, 3.9, 4.2, 1.6, 7.6, 4.6, 4.9, 3.5, 7.3, 0, 1.3, 1.5, 4, 3.2, 3, 6.9, 6.2, 8.2, 5.5, 4.4,
     7.2, 6.4, 10.5],
    [4.4, 4.6, 5.6, 4.3, 2.4, 3, 8, 3.3, 7.8, 3.7, 5.2, 2.6, 7.8, 1.3, 0, 0.6, 6.4, 2.4, 2.2, 6.8, 5.3, 7.4, 4.6, 4.8,
     6.3, 6.5, 8.8],
    [3.7, 4.5, 5.8, 4.4, 2.7, 3.8, 5.8, 3.4, 6.6, 4, 5.4, 2.9, 6.6, 1.5, 0.6, 0, 5.6, 1.6, 1.7, 6.4, 4.9, 6.9, 4.2, 5.6,
     5.9, 5.7, 8.4],
    [7.6, 7.4, 5.7, 7.2, 1.4, 5.7, 7.2, 3.1, 7.2, 6.7, 8.1, 6.3, 7.2, 4, 6.4, 5.6, 0, 7.1, 6.1, 7.2, 10.6, 12, 9.4, 7.5,
     11.1, 6.2, 13.6],
    [2, 6, 4.1, 5.3, 0.5, 1.9, 7.7, 5.1, 5.9, 2.3, 6.2, 1.2, 5.9, 3.2, 2.4, 1.6, 7.1, 0, 1.6, 4.9, 3, 5, 2.3, 5.5, 4,
     5.1, 5.2],
    [3.6, 5, 3.6, 6, 1.7, 1.1, 6.6, 4.6, 5.4, 1.8, 6.9, 1, 5.4, 3, 2.2, 1.7, 6.1, 1.6, 0, 4.4, 4.6, 6.6, 3.9, 6.5, 5.6,
     4.3, 6.9],
    [6.5, 4.8, 4.3, 10.6, 6.5, 3.5, 3.2, 6.7, 1, 4.1, 11.5, 3.7, 1, 6.9, 6.8, 6.4, 7.2, 4.9, 4.4, 0, 7.5, 9.3, 6.8,
     11.4, 8.5, 1.8, 13.1],
    [1.9, 9.5, 3.3, 5.9, 3.2, 4.9, 11.2, 8.1, 8.5, 3.8, 6.9, 4.1, 8.5, 6.2, 5.3, 4.9, 10.6, 3, 4.6, 7.5, 0, 2, 2.9, 6.4,
     2.8, 6, 4.1],
    [3.4, 10.9, 5, 7.4, 5.2, 6.9, 12.7, 10.4, 10.3, 5.8, 8.3, 6.2, 10.3, 8.2, 7.4, 6.9, 12, 5, 6.6, 9.3, 2, 0, 4.4, 7.9,
     3.4, 7.9, 4.7],
    [2.4, 8.3, 6.1, 4.7, 2.5, 4.2, 10, 7.8, 7.8, 4.3, 4.1, 3.4, 7.8, 5.5, 4.6, 4.2, 9.4, 2.3, 3.9, 6.8, 2.9, 4.4, 0,
     4.5, 1.7, 6.8, 3.1],
    [6.4, 6.9, 9.7, 0.6, 6, 9, 8.2, 4.2, 11.5, 7.8, 0.4, 6.9, 11.5, 4.4, 4.8, 5.6, 7.5, 5.5, 6.5, 11.4, 6.4, 7.9, 4.5,
     0, 5.4, 10.6, 7.8],
    [2.4, 10, 6.1, 6.4, 4.2, 5.9, 11.7, 9.5, 9.5, 4.8, 4.9, 5.2, 9.5, 7.2, 6.3, 5.9, 11.1, 4, 5.6, 8.5, 2.8, 3.4, 1.7,
     5.4, 0, 7, 1.3],
    [5, 4.4, 2.8, 10.1, 5.4, 3.5, 5.1, 6.2, 2.8, 3.2, 11, 3.7, 2.8, 6.4, 6.5, 5.7, 6.2, 5.1, 4.3, 1.8, 6, 7.9, 6.8,
     10.6, 7, 0, 8.3],
    [3.6, 13, 7.4, 10.1, 5.5, 7.2, 14.2, 10.7, 14.1, 6, 6.8, 6.4, 14.1, 10.5, 8.8, 8.4, 13.6, 5.2, 6.9, 13.1, 4.1, 4.7,
     3.1, 7.8, 1.3, 8.3, 0]
]

'''
This is a dictionary that contains a list of the addresses as keys, and address ID numbers as values.

Space complexity = O(1)
Time Complexity = O(1)
'''
addressDict = {'4001 South 700 East': 0,
               '1060 Dalton Ave S': 1,
               '1330 2100 S': 2,
               '1488 4800 S': 3,
               '177 W Price Ave': 4,
               '195 W Oakland Ave': 5,
               '2010 W 500 S': 6,
               '2300 Parkway Blvd': 7,
               '233 Canyon Rd': 8,
               '2530 S 500 E': 9,
               '2600 Taylorsville Blvd': 10,
               '2835 Main St': 11,
               '300 State St': 12,
               '3060 Lester St': 13,
               '3148 S 1100 W': 14,
               '3365 S 900 W': 15,
               '3575 W Valley Central Station bus Loop': 16,
               '3595 Main St': 17,
               '380 W 2880 S': 18,
               '410 S State St': 19,
               '4300 S 1300 E': 20,
               '4580 S 2300 E': 21,
               '5025 State St': 22,
               '5100 South 2700 West': 23,
               '5383 S 900 East #104': 24,
               '600 E 900 South': 25,
               '6351 South 900 East': 26
               }


'''
This is an empty dictionary that will contain a list of package ID's as keys, and delivery times as values.
It is populated as the core algorithm runs.

Space complexity = O(1)
Time Complexity = O(1)
'''
deliveryTimeDict = {}


'''
These are lists that contain the package ID's loaded on the trucks.
These lists are reduced down to zero in size as the core algorithm runs.

Space complexity = O(1)
Time Complexity = O(1)
'''
truck1Packages = [1, 2, 4, 5, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
truck2Packages = [3, 6, 7, 8, 17, 18, 21, 22, 23, 24, 25, 26, 28, 32, 36, 38]
truck3Packages = [9, 10, 11, 12, 27, 33, 35, 39]

'''
These are lists that contain the package ID's loaded on the trucks.
These lists do not change, and they are accessed by the comparison operators at the end.

Space complexity = O(1)
Time Complexity = O(1)
'''
truck1PackageSnapshot = [1, 2, 4, 5, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
truck2PackageSnapshot = [3, 6, 7, 8, 17, 18, 21, 22, 23, 24, 25, 26, 28, 32, 36, 38]
truck3PackageSnapshot = [9, 10, 11, 12, 27, 33, 35, 39]

# Set initial address for each truck
truck1Address = addressDict['4001 South 700 East']
truck2Address = addressDict['4001 South 700 East']
truck3Address = addressDict['4001 South 700 East']

# Set initial miles driven for each truck.
truck1TotalMiles = 0
truck2TotalMiles = 0
truck3TotalMiles = 0

# Set delivery day start time for trucks 1 and 2, for use in comparison operators at the end.
truck1StartTime = datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 8, 00, 00, 00)
truck2StartTime = datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 9, 5, 00, 00)

# Set delivery day start time for trucks 1 and 2. These times are changed as the core algorithm runs.
truck1Time = datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 8, 00, 00, 00)
truck2Time = datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 9, 5, 00, 00)


'''
Start algorithm

This is the core algorithm that finds the next closest location out of the packages on the truck.
Once the nearest package delivery address is located, the truck is "moved" to that location, and that package is removed from the truck.
Each truck is run separately, sequentially. 

Space complexity = O(n^2)
Time Complexity = O(n^2)
'''
while len(truck1Packages) > 0:
    minDistance = 100000000

    for p in truck1Packages:
        packageUpdateStatus = packageHashTable.myHash.lookup(p)
        packageUpdateStatus.packageDeliveredStatus = 'En Route'
        destinationAddress = addressDict[str(packageHashTable.myHash.lookup(p).packageDeliveryAddress)]
        distance = distanceArray[truck1Address][destinationAddress]
        if distance < minDistance:
            minDistance = distance
            minPackageID = p
            pkg = packageHashTable.myHash.lookup(p)
    truck1TimeDelta = datetime.timedelta(minutes=+(minDistance / .3))
    truck1Time = truck1Time + truck1TimeDelta
    truck1Address = addressDict[packageHashTable.myHash.lookup(minPackageID).packageDeliveryAddress]
    truck1TotalMiles = truck1TotalMiles + minDistance
    truck1Packages.remove(minPackageID)
    pkg.packageDeliveredStatus = 'Delivered'
    pkg.packageTimeDelivered = truck1Time.time()
    deliveryTimeDict[pkg.packageId] = pkg.packageTimeDelivered
destinationAddress = addressDict['4001 South 700 East']
distance = distanceArray[truck1Address][destinationAddress]
truck1TotalMiles = truck1TotalMiles + distance
truck1TimeDelta = datetime.timedelta(minutes=+(distance / .3))
truck1Time = truck1Time + truck1TimeDelta
truck3Time = truck1Time + truck1TimeDelta
truck3StartTime = truck1Time
print("\n")
print('Truck 1 total miles traveled:', round(truck1TotalMiles, 2))
print('Truck 1 end time:', truck1Time.time())

while len(truck2Packages) > 0:
    minDistance = 100000000

    for p in truck2Packages:
        packageUpdateStatus = packageHashTable.myHash.lookup(p)
        packageUpdateStatus.packageDeliveredStatus = 'En Route'
        destinationAddress = addressDict[str(packageHashTable.myHash.lookup(p).packageDeliveryAddress)]
        distance = distanceArray[truck2Address][destinationAddress]
        if distance < minDistance:
            minDistance = distance
            minPackageID = p
            pkg = packageHashTable.myHash.lookup(p)
    truck2TimeDelta = datetime.timedelta(minutes=+(minDistance / .3))
    truck2Time = truck2Time + truck2TimeDelta
    truck2Address = addressDict[packageHashTable.myHash.lookup(minPackageID).packageDeliveryAddress]
    truck2TotalMiles = truck2TotalMiles + minDistance
    truck2Packages.remove(minPackageID)
    pkg.packageDeliveredStatus = 'Delivered'
    pkg.packageTimeDelivered = truck2Time.time()
    deliveryTimeDict[pkg.packageId] = pkg.packageTimeDelivered
print("\n")
print('Truck 2 total miles traveled:', round(truck2TotalMiles, 2))
print('Truck 2 end time:', truck2Time.time())

while len(truck3Packages) > 0:
    minDistance = 100000000

    for p in truck3Packages:
        packageUpdateStatus = packageHashTable.myHash.lookup(p)
        packageUpdateStatus.packageDeliveredStatus = 'En Route'
        destinationAddress = addressDict[str(packageHashTable.myHash.lookup(p).packageDeliveryAddress)]
        distance = distanceArray[truck3Address][destinationAddress]
        if distance < minDistance:
            minDistance = distance
            minPackageID = p
            pkg = packageHashTable.myHash.lookup(p)
    truck3TimeDelta = datetime.timedelta(minutes=+(minDistance / .3))
    truck3Time = truck3Time + truck3TimeDelta
    truck3Address = addressDict[packageHashTable.myHash.lookup(minPackageID).packageDeliveryAddress]
    truck3TotalMiles = truck2TotalMiles + minDistance
    truck3Packages.remove(minPackageID)
    pkg.packageDeliveredStatus = 'Delivered'
    pkg.packageTimeDelivered = truck3Time.time()
    deliveryTimeDict[pkg.packageId] = pkg.packageTimeDelivered
print("\n")
print('Truck 3 total miles traveled:', round(truck3TotalMiles, 2))
print('Truck 3 end time:', truck3Time.time())
print("\n")
print('Total miles traveled for all trucks:', round(truck1TotalMiles + truck2TotalMiles + truck3TotalMiles, 2))
print('End of delivery day:', truck3Time.time())
print("\n")
print("\n")



'''
This is creating an ordered dictionary out of the delivery times dictionary.

Space complexity = O(1)
Time Complexity = O(1)
'''
orderedDeliveryTimeDict = dict(sorted(deliveryTimeDict.items()))


'''
This is a comparison algorithm that compares the time entered by the user to the time each package was delivered,
and returns the appropriate package statuses.

Space complexity = O(n^2)
Time Complexity = O(n^2)
'''
while True:
    year = str(datetime.date.today().year)
    month = str(datetime.date.today().month)
    day = str(datetime.date.today().day)
    testTimeRaw = input("Please enter a time to search the status of packages (HH:MM 24-hour format): ")
    testTimeRefined = datetime.datetime.strptime(year + '-' + month + '-' + day + ' ' + testTimeRaw, '%Y-%m-%d %H:%M')
    print("\n")
    print("***** All package statuses as of", testTimeRefined.time().strftime('%H:%M'), "*****")

    for key, value in orderedDeliveryTimeDict.items():
        if testTimeRefined < truck1StartTime:
            print("Package", packageHashTable.myHash.lookup(key).packageId, ":", packageHashTable.myHash.lookup(key).packageDeliveryAddress,",", "Delivery deadline:", packageHashTable.myHash.lookup(key).packageDeliveryDeadline,",", "Status:", "At the hub ")
        elif truck1StartTime <= testTimeRefined < truck2StartTime:
            if key in truck1PackageSnapshot:
                if value < testTimeRefined.time():
                    print("Package", packageHashTable.myHash.lookup(key).packageId, ":", packageHashTable.myHash.lookup(key).packageDeliveryAddress,",",  "Delivery deadline:", packageHashTable.myHash.lookup(key).packageDeliveryDeadline,",", "Status:",  "Delivered at ", packageHashTable.myHash.lookup(key).packageTimeDelivered)
                else:
                    print("Package", packageHashTable.myHash.lookup(key).packageId, ":", packageHashTable.myHash.lookup(key).packageDeliveryAddress,",",  "Delivery deadline:", packageHashTable.myHash.lookup(key).packageDeliveryDeadline,",", "Status:",  "En route ")
            else:
                print("Package", packageHashTable.myHash.lookup(key).packageId, ":", packageHashTable.myHash.lookup(key).packageDeliveryAddress,",",  "Delivery deadline:", packageHashTable.myHash.lookup(key).packageDeliveryDeadline,",", "Status:", "At the hub ")
        elif truck2StartTime <= testTimeRefined < truck3StartTime:
            if key in truck1PackageSnapshot:
                if value < testTimeRefined.time():
                    print("Package", packageHashTable.myHash.lookup(key).packageId, ":", packageHashTable.myHash.lookup(key).packageDeliveryAddress,",",  "Delivery deadline:", packageHashTable.myHash.lookup(key).packageDeliveryDeadline,",", "Status:", "Delivered at ", packageHashTable.myHash.lookup(key).packageTimeDelivered)
                else:
                    print("Package", packageHashTable.myHash.lookup(key).packageId, ":", packageHashTable.myHash.lookup(key).packageDeliveryAddress,",",  "Delivery deadline:", packageHashTable.myHash.lookup(key).packageDeliveryDeadline,",", "Status:", "En route ")
            elif key in truck2PackageSnapshot:
                if value < testTimeRefined.time():
                    print("Package", packageHashTable.myHash.lookup(key).packageId, ":", packageHashTable.myHash.lookup(key).packageDeliveryAddress,",",  "Delivery deadline:", packageHashTable.myHash.lookup(key).packageDeliveryDeadline,",", "Status:", "Delivered at ", packageHashTable.myHash.lookup(key).packageTimeDelivered)
                else:
                    print("Package", packageHashTable.myHash.lookup(key).packageId, ":", packageHashTable.myHash.lookup(key).packageDeliveryAddress,",",  "Delivery deadline:", packageHashTable.myHash.lookup(key).packageDeliveryDeadline,",", "Status:", "En route ")
            else:
                print("Package", packageHashTable.myHash.lookup(key).packageId, ":", packageHashTable.myHash.lookup(key).packageDeliveryAddress,",",  "Delivery deadline:", packageHashTable.myHash.lookup(key).packageDeliveryDeadline,",", "Status:", "At the hub ")
        else:
            if value < testTimeRefined.time():
                print("Package", packageHashTable.myHash.lookup(key).packageId, ":", packageHashTable.myHash.lookup(key).packageDeliveryAddress,",",  "Delivery deadline:", packageHashTable.myHash.lookup(key).packageDeliveryDeadline,",", "Status:", "Delivered at ", packageHashTable.myHash.lookup(key).packageTimeDelivered)
            else:
                print("Package", packageHashTable.myHash.lookup(key).packageId, ":", packageHashTable.myHash.lookup(key).packageDeliveryAddress,",",  "Delivery deadline:", packageHashTable.myHash.lookup(key).packageDeliveryDeadline,",", "Status:", "En route ")
    print("\n")
    continue



