import customPWM
import time
'''
pwm = SoftwarePWM(3)
pwm.start()
pwm.set_duty_cycle(x)
pwm.stop()
'''
class motorCotroller:
    def __init__(self, pinR, pinL):
        self.pinR = pinR
        self.pinL = pinL
        self.pwmR = customPWM.SoftwarePWM(pinR)
        self.pwmL = customPWM.SoftwarePWM(pinL)
        self.pwmR.start()
        self.pwmL.start()
    def drive(self, percent):
        if (percent > 0):
            self.pwmL.set_duty_cycle(percent)
            self.pwmR.set_duty_cycle(0)
        if (percent < 0):
            self.pwmL.set_duty_cycle(0)
            self.pwmR.set_duty_cycle(percent)
    def breakMode(self, percent):
        self.pwmL.set_duty_cycle(percent)
        self.pwmR.set_duty_cycle(percent)
    def stop(self):
        self.pwmL.stop()
        self.pwmR.stop()


motor = motorCotroller(3, 4)

motor.stop()