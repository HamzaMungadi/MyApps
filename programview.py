class Programs:
      def __init__(self, title, start, end):
          self.title=title
          self.start=start
          if self.start=='2':
             self.duration=self.start+'nd'+'-'+end+'th'
          else:
             self.duration=self.start+'th'+'-'+end+'th'
      def display(self):
          print self.title+'    '+self.duration

prog1=Programs('HD workshop', '24', '28')
prog2=Programs('LTP for MCAN', '29', '30')

prog3=Programs('DIWA stepdowns', '4', '4')
prog4=Programs('TBI score-card', '7', '11')
prog5=Programs('Bro Nuru (meeting at Abuja)', '12', '12')

prog6=Programs('Switzerland', '2', '9')
prog7=Programs('Malasia', '27', 'Oct 16')

prog8=Programs('Malasia', '16', '16')
prog9=Programs('Nigeran Airforce Interfaith at Abuja', '23', '24')
prog10=Programs('Vienna', '29', 'Nov. 4')

prog11=Programs('MICA Lagos (DRM) ', '18', '19')

prog12=Programs('Izala group Jos', '4', '28')
prog13=Programs('The Revival of Islamic spririt Toronto, Canada', '20', '27')

JULY=[prog1, prog2]
AUGUST=[prog3,prog4,prog5]
SEPTEMBER=[prog6,prog7]
OCTOBER=[prog8,prog9,prog10]
NOVEMBER=[prog11]
DECEMBER=[prog12, prog13]
MONTHS=[JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER]
#for Month in MONTHS:
#Event=MONTHS[2]
#for prog in Event:
    #prog.display()

