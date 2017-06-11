from p1 import *
from mytime import *

class rent:
     NoOfClient=0
     def __init__(self, person, total_amount, deposite, day, month, from_hour, to_hour):
            self.person=person
            self.total_amount=total_amount
            self.deposite=deposite
            self.DateOfWalima=Date(day,month)
            self.StartTime=Time(from_hour)
            self.endTime=Time(to_hour)
            self.balance=self.total_amount-self.deposite
            rent.NoOfClient+=1
     def Bname(self):
          return self.person 
  
     def TotalToBepay(self):
          return self.total_amount

     def Deposited(self):
          return self.deposite

     def getBalance(self):
          return self.balance

     def getDate(self):
          return self.DateOfWalima 
     def getTime(self):
          print'Start from: ',
          self.StartTime.printStandart()
          print'End: ',
          self.endTime.printStandart()
     def Display(self):
          print'Name: {}'.format(self.person)
          print'Total amount to be paid:\n{}'.format(self.total_amount)
          print'Amount deposited:\n{}'.format(self.deposite)
          print'Balance: \n{}'.format(self.balance)
          print'Date of Walima: '
          self.DateOfWalima.display()
          print'Start from: '
          self.StartTime.printStandart()
          print'End: '
          self.endTime.printStandart()
class NetPayment(rent):
      TotalAmountGenerated=0
      def __init__(self,person, total_amount, deposite, day, month, from_hour, to_hour, refundedAmount):
         rent.__init__(self, person, total_amount, deposite, day, month, from_hour, to_hour)
         self.refundedAmount=refundedAmount
         self.Netpayment=self.total_amount-self.refundedAmount-2500
         NetPayment.TotalAmountGenerated+=self.Netpayment
      
      def Display(self):
          print
          print'Name:\n{}'.format(self.person)
          print
          print'Total amount to be paid:\n{}'.format(self.total_amount)
          print
          print'Amount deposited:\n{}'.format(self.deposite)
          print
          print'Balance:\n{}'.format(self.balance)
          print
          print'Date of Walima:'
          self.DateOfWalima.display()
          print
          print'Start from:'
          self.StartTime.printStandart()
          print
          print'End:'
          self.endTime.printStandart()
          print
          print 'Amount refunded: \n{}'.format( self.refundedAmount)
          print
          print 'General Cleaning:\n2500'
          print
	  print 'Net Payment:\n{}'.format(self.Netpayment)
          print
      def Netpayment(self):
          return self.Netpayment
      def GetRefundable(self):
          return self.refundedAmount
