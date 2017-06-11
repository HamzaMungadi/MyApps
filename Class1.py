class Register:
     def __init__(self):
        self.TafsirHall=3000
        self.Generator=3000
        self.PAS=2000
        self.ClassRoom=1000
        self.Gcleaning=2500
        self.DepositeForDamage=3000
     #No options
     def TotalAmountTobePaid(self):
         print self.Hall+self.Classroom+self.PAP+self.GeneralCleaning+self.StandbyGenerator+self.DepositeForDamages
     #except classrom
     def TotalAmountTobePaidNoClassroom(self):
         print self.Hall+self.PAP+self.GeneralCleaning+self.StandbyGenerator+self.DepositeForDamages
     #no p.a.p
     def TotalAmountTobePaidNoPAP(self):
         print self.Hall+self.Classroom+self.GeneralCleaning+self.StandbyGenerator+self.DepositeForDamages

Re=Register()

