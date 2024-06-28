AllowedVehiclesList = ['Ford F-150','Chevrolet Silverado','Tesla Cybertruck','Toyota Tundra','Nissan Titan']

print("********************************")
print("AutoCountry Vehicle Finder v0.1")
print("********************************")
print("Please Enter one of the following numbers below from the following menu:")
print(" ")
print('1. PRINT all Authorized Vehicles')
print('2. Exit')

while (True):
  selection = input("Please enter your choice: ")
  if int(selection) == 1:
    print(AllowedVehiclesList)
    continue
  if int(selection) != 2:
    print("Invalid Choice,Please select a valid choice from the menu")
    continue
  if int(selection) == 2:
    print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
    break

  