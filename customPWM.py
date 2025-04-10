import os
import time
import threading

class SoftwarePWM:
    def __init__(self, pin, frequency=20, duty_cycle=0):
        self.pin = pin
        self.frequency = frequency
        self.duty_cycle = duty_cycle
        self.running = False
        os.system(f"gpio export {self.pin} out")
    def pwm(self):
        period = 1 / self.frequency
        while self.running:
            high_time = period * self.duty_cycle / 100
            low_time = period - high_time
            os.system(f"gpio write {self.pin} 1")
            time.sleep(high_time)
            os.system(f"gpio write {self.pin} 0")
            time.sleep(low_time)
    def start(self):
        self.running = True
        self.pwm_thread = threading.Thread(target=self.pwm)
        self.pwm_thread.start()
    def stop(self):
        self.running = False
        self.pwm_thread.join()
        os.system(f"gpio unexport {self.pin}")
        print("PWM stopped and pin unexported")
    def set_duty_cycle(self, duty_cycle):
        self.duty_cycle = duty_cycle


'''
pwm = SoftwarePWM(3)
pwm.start()
pwm.set_duty_cycle(x)
pwm.stop()
'''