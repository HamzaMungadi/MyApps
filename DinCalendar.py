from p1 import *

class DinPrograms: 
      def __init__(self, pName, startDay, startMonth, endDay, endMonth):
          self.startProgram=Date(startDay, startMonth)
          self.endProgram=Date(endDay, endMonth)
          self.pName=pName
      def Details(self):
          print "Program title:\n{}".format(self.pName)
          print "From:"
	  self.startProgram.display()
	  print "To:"
	  self.endProgram.display()
      
      def Name( self ):
	  """Prints employee information"""
	  print "{}".format( self.pName)
	 
