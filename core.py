import numpy as np
from scipy.optimize import minimize

#defining mathematical function

def objective(x,y):
    WB_Height_red = x[0]
    WB_Pass = x[1]
    WB_Temp = x[2]
    WB_Thickness = y
    Bulge = (-3.53449 + 0.242763*WB_Height_red + 10.3013*WB_Pass -0.00561165*WB_Temp -0.0197274*WB_Thickness + 0.0706014*WB_Height_red*WB_Pass -0.000487719*WB_Height_red*WB_Temp + 0.00191491*WB_Height_red*WB_Thickness -0.00555013*WB_Pass*WB_Temp -0.0116927*WB_Pass*WB_Thickness + 5.47149e-05*WB_Temp*WB_Thickness)
    return Bulge

#initialising start values for the function

x0 = [15,2,1100]     #x0 = [WB_Height_red, WB_Pass, WB_Temp]   

#setting up the boundary conditions 

b1 = (5,30)          #b1 = WB_Height_red
b2 = (2,4)          #b2 = WB_Pass
b3 = (1000,1200)     #b3 = WB_Temperature
    
bnds = (b1,b2,b3)

#calling the optimiser function to choose parametes that minimize the bulge width
    


#getting the input: thickness value from the user
def thickness(y):
    sol = minimize(objective,x0,y,method='SLSQP',bounds=bnds)
    return [sol.fun, sol.x[0],int(sol.x[1]),sol.x[2]]
'''y=1
sol = minimize(objective,x0,y,method='SLSQP',bounds=bnds)
#printing the output

print('The bulge width is :',sol.fun)
print('The height reduction per pass is :',sol.x[0],'mm')
print('Optimized number of pass is :',int(sol.x[1]))
print('Operating temperature is :',sol.x[2],'°C')'''
