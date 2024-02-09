import random

#Ground shipping
weight_ground_shipping = random.randint(1, 20)

print('Weight in lb (Ground shipping): ' + str(weight_ground_shipping))
limit_1 = weight_ground_shipping * 1.50 + 20.00
limit_2 = weight_ground_shipping * 3.00 + 20.00
limit_3 = weight_ground_shipping * 4.00 + 20.00
limit_4 = weight_ground_shipping * 4.75 + 20.00

if weight_ground_shipping <= 2:
  print('Cost: ' + str(limit_1)) 
elif weight_ground_shipping > 2 and weight_ground_shipping <= 6:
  print('Cost: ' + str(limit_2)) 
elif weight_ground_shipping > 6 and weight_ground_shipping <= 10:
  print('Cost: ' + str(limit_3))
elif weight_ground_shipping > 10:
  print('Cost: ' + str(limit_4))
else:
  print('Error')
print('\n')

#Ground Shipping premium:
cost = 125.00
print('Ground Shipping premium: ' + '\n' + 'Cost: ' +  str(cost))
print('\n')

#Drone shipping
weight_Drone_shipping = random.randint(1, 20)
print('Weight in lb (Drone shipping): ' + str(weight_Drone_shipping))
limit_1 = weight_Drone_shipping * 4.50
limit_2 = weight_Drone_shipping * 9.00
limit_3 = weight_Drone_shipping * 12.00 
limit_4 = weight_Drone_shipping * 14.25 

if weight_Drone_shipping <= 2:
  print('Cost: ' + str(limit_1)) 
elif weight_Drone_shipping > 2 and weight_Drone_shipping <= 6:
  print('Cost: ' + str(limit_2)) 
elif weight_Drone_shipping > 6 and weight_Drone_shipping <= 10:
  print('Cost: ' + str(limit_3))
elif weight_Drone_shipping > 10:
  print('Cost: ' + str(limit_4))
else:
  print('Error')

