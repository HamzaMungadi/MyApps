class Time:

     def __init__(self, hour=0, minute=0, second=0):

         self.setTime(hour,minute,second)
     def setTime(self,hour,minute,second):
         self.setHour(hour)
         self.setMinute(minute)
         self.setSecond(second)
     def setHour(self,hour):
         if 0<=hour<24:
             self.hour=hour
         else:
            print'Invalid hour value: {}'.format(hour)
     def setMinute(self,minute):
         if 0<=minute<60:
             self.minute=minute
         else:
            print'Invalid minute value: {}'.format(minute)
     def setSecond(self,second):
         if 0<=second<60:
             self.second=second
         else:
            print'Invalid second value: {}'.format(second)
     def getHour(self):
          return self.hour
     def getMinute(self):
          return self.minute
     def getSecond(self):
          return self.second
     def printMilitary(self):
         print'%.2d:%.2d:%.2d'%(self.hour,self.minute, self.second)
     def printStandart(self):
         standartTime=""
         if self.hour==0 or self.hour==12:
            standartTime+='12:'
         else:
            standartTime+='%d:'%(self.hour %12)
         standartTime+='%.2d:%.2d'%(self.minute,self.second)
         if self.hour<12:
            standartTime+='AM'
         else:
            standartTime+='PM'
         print standartTime
t1=Time()
t2=Time(23)
t3=Time(12,3,6)
#t1.printStandart()
#t2.printStandart()
#t3.printStandart()
#t1.printMilitary()
#t2.printMilitary()
#t3.printMilitary()
#t4.printStandart





