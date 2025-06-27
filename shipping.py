#In this project, I’m building a program to help determine the cheapest way to ship a package using Sal’s Shippers. The program will take the weight of a package and calculate the cost for three different shipping methods: Ground Shipping (a flat fee plus a rate based on weight), Ground Shipping Premium (a higher flat fee with no weight-based charge), and Drone Shipping (no flat fee but a higher rate per pound). Based on the weight, the program will figure out which option is the most affordable.





weight = 41.5


#ground shipping

if weight <= 2:
  cost = 1.50 * weight + 20.00
elif weight <= 6:
  cost = 3.00 * weight + 20.00
elif weight <= 10:
  cost = 4.00 * weight + 20.00
else:
  cost = 4.75 * weight + 20.00


print ("Ground Shipping cost: ", cost)

print("""
""")



#premium ground shipping

premium_ground_shipping = 125.00

print("Dont forget that for premium ground shipping, the flat fee is just $125.00 regardless of weight.")



print("""
""")

#Drone Shipping

if weight <= 2:
  cost = weight * 4.50 + 0.00
elif weight <= 6:
  cost = weight * 9.00 + 0.00
elif weight <= 10:
  cost = weight * 12.00 + 0.00
else:
  cost = weight * 14.25 + 0.00

print("Drone shipping cost: ", cost)




#If you change the weight variable to any number, you will be able to determine what is the most effective pricing plan to go with. 
