from flask import Flask
import drivetrain
app = Flask(__name__)
driveTrain = drivetrain.drivetrainControl()

@app.route('/forward/<int:forwardSpeed>', methods=['GET'])
def handle_forward(forwardSpeed):
    driveTrain.forward(forwardSpeed)
    return "done"

@app.route('/backward/<int:backwardSpeed>', methods=['GET'])
def handle_backward(backwardSpeed):
    driveTrain.back(backwardSpeed)
    return "done"

@app.route('/rightTurn/<int:rightTurnSpeed>', methods=['GET'])
def handle_rightTurn(rightTurnSpeed):
    driveTrain.turnRight(rightTurnSpeed)
    return "done"

@app.route('/leftTurn/<int:leftTurnSpeed>', methods=['GET'])
def handle_leftTurn(leftTurnSpeed):
    driveTrain.turnLeft(leftTurnSpeed)
    return "done"

@app.route('/stop', methods=['GET'])
def handle_stop():
    driveTrain.stop()
    return "done"

@app.route('/armPosition/<int:armPosition>', methods=['GET'])
def handle_armPosition(armPosition):
    #needs to be defined
    return " "

app.run(host='0.0.0.0')
