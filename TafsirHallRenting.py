from p1 import *
from mytime import *
from tafsirhall import *
Booker1=NetPayment('FOMWAN', 11500, 11500, 1,2,12,14, 0)
Booker2=NetPayment('Sani Auwal Family', 17500, 17500, 25,3,16,18, 9000)
Booker3=NetPayment('Abdul-kadir Kuso', 26500, 5000,23,2,16,19,12000)
Booker4=NetPayment('Ramadam', 6000, 5000, 9,4,13,14, 3000)
Booker5=NetPayment('Aliyu B. Abdullahi', 18500, 18500, 19,4,16,18, 6000)
Booker6=NetPayment('Alh Wasagi', 14800, 14800, 26,4,16,18, 3000)
Booker7=NetPayment('Aisha Usman', 18500, 17000, 30,3,16,18, 6000)
#TotalClient=[Booker1, Booker2,Booker3, Booker4, Booker5, Booker6, Booker7]
def ShowAll():
    for client in TotalClient:
	    print
	    client.Display()
	    print
#print'Number of Client: ', rent.NoOfClient
#print 'Total money generated: ', NetPayment.TotalAmountGenerated
#Booker1.Display()
#ShowAll()
