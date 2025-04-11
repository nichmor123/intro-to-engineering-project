import motorControl
class drivetrainControl:
    def __init__(self, FRR=2, FRL=5, FLR=7, FLL=8, BRR=25, BRL=23, BLR=3, BLL=4):
        self.FRmotor = motorControl.motorCotroller(FRR, FRL)
        self.FLmotor = motorControl.motorCotroller(FLR, FLL, True)
        self.BRmotor = motorControl.motorCotroller(BRR, BRL)
        self.BLmotor = motorControl.motorCotroller(BLR, BLL, True)
    def forward(self, percent):
        self.FRmotor.drive(percent)
        self.FLmotor.drive(percent)
        self.BRmotor.drive(percent)
        self.BLmotor.drive(percent)
    def backward(self, percent):
        self.FRmotor.drive(-percent)
        self.FLmotor.drive(-percent)
        self.BRmotor.drive(-percent)
        self.BLmotor.drive(-percent)
    def turnRight(self, percent):
        self.FRmotor.drive(-percent)
        self.FLmotor.drive(percent)
        self.BRmotor.drive(-percent)
        self.BLmotor.drive(percent)
    def turnLeft(self, percent):
        self.FRmotor.drive(percent)
        self.FLmotor.drive(-percent)
        self.BRmotor.drive(percent)
        self.BLmotor.drive(-percent)
    def stop(self):
        self.FRmotor.stop()
        self.FLmotor.stop()
        self.BRmotor.stop()
        self.BLmotor.stop()