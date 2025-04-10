import customPWM
class motorCotroller:
    def __init__(self, pinR, pinL, isReversed=False):
        self.pinR = pinR
        self.pinL = pinL
        self.pwmR = customPWM.SoftwarePWM(pinR)
        self.pwmL = customPWM.SoftwarePWM(pinL)
        self.pwmR.start()
        self.pwmL.start()
        if (isReversed == True):
            self.multiplier = -1
        else:
            self.multiplier = 1
        self.percentOut = 0
    def drive(self, percent):
        self.percentOut = percent * self.multiplier
        if (self.percentOut > 0):
            self.pwmL.set_duty_cycle(self.percentOut)
            self.pwmR.set_duty_cycle(0)
        if (self.percentOut < 0):
            self.pwmL.set_duty_cycle(0)
            self.pwmR.set_duty_cycle(self.percentOut)
    def breakMode(self, percent):
        self.pwmL.set_duty_cycle(percent)
        self.pwmR.set_duty_cycle(percent)
    def stop(self):
        self.pwmL.stop()
        self.pwmR.stop()