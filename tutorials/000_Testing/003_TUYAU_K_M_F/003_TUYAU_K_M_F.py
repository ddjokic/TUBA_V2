#---UnitCalculator to use different input units---
from external.UnitCalculator import *
auto_converter(mmNS)

outerRadius=35.0   #in mm
WallThickness=4.0   #in mm

SectionTuyau(outerRadius,WallThickness) #Model("TUYAU")
Material("SS304")  #Check the material library or autodoc for a complete list of available material properties.

#Sets the temperature of the vector objects. T_ref denotes the temperature at which thermal dilatation is supposed to be 0.
Temperature(550,T_ref=20)

#Set the internal pressure of the piping. The unit bar() is a function from UnitCalculator which translates bar to N/mm2
#These unit functions can only be used if the UnitCalculator module is imported(first lines)
Pressure(2*bar())



P(0,0,0)  
FixPoint()
V(1000,0,0)
Force(0,1000,0)
V(1000,0,0)
Block(z=0)
V(1000,0,0)
Spring(10,10,10)
Bent(150,90,90)

SectionTuyau("DN15","SCH-STD") #Model("TUYAU")

Vc(1000)
Block(y=0)
Vc(1000)
Block(x=-100)


