class Date:
      
      #class var
      daysPerMonth=[0,31,28,31,30,31,30,31,31,30,31,30,31]
      
      #class Constructor
      def __init__(self, day, month, year=2017):

          #self.day=day
       
          if 0<month<=12:
             self.month=month
          else:
              raise ValueError, "Invalid value for month: {}".format(month)
          if year>0:
             self.year=year  
          else:
              raise ValueError, "Invalid value for year: {}".format(year)
          self.day=self.checkDay(day)

          #print"Date of contractor"
          #self.display()

      def display(self):

          print "{}/{}/{}".format(self.day, self.month, self.year)

      def checkDay(self, testDay) :   
         """Validates day of month"""
         if 0 < testDay <= Date.daysPerMonth[self.month]:
             return testDay
         elif self.month == 2 and testDay == 29 and \
              ( self.year % 400 == 0 or 
              self.year % 100 != 0 and self.year % 4 == 0 ):
              return testDay
         else:
             raise ValueError, "Invalid day: %d for month: %d" % \
             ( testDay, self.month )
class searchDate(Date):
      
      def __init__(self, day, month, year, Dates):
         Date.__init__(self, day, month, year)   
         if Dates is None:
              self.Dates=[]
         else:
              self.Dates=Dates

      def add_date(self, date):
            if date not in self.Dates:
                 self.Dates.append(date)
      def remove_date(self, date):

            if date in self.date:
                 self.Dates.remove(date)
      def print_Dates(self):
            for date in self.Dates:
               print '-->', date.display()


Dy=Date(29,2,2016)
Date2017=searchDate(1,1,2017,[Dy])

#print   Dy.month
#print	Dy.day
#print	Dy.year
#Date2017.display()
#Date2017.print_Dates
#Dy.display()


