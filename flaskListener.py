from flask import Flask
import drivetrain
app = Flask(__name__)
driveTrain = drivetrain.drivetrainControl()
driveTrain.stop()

@app.route('/forward/<int:forwardSpeed>', methods=['GET'])
def handle_forward(forwardSpeed):
    driveTrain.forward(forwardSpeed)
    return str(forwardSpeed)

@app.route('/backward/<int:backwardSpeed>', methods=['GET'])
def handle_backward(backwardSpeed):
    driveTrain.back(backwardSpeed)
    return str(backwardSpeed)

@app.route('/rightTurn/<int:rightTurnSpeed>', methods=['GET'])
def handle_rightTurn(rightTurnSpeed):
    driveTrain.turnRight(rightTurnSpeed)
    return str(rightTurnSpeed)

@app.route('/leftTurn/<int:leftTurnSpeed>', methods=['GET'])
def handle_leftTurn(leftTurnSpeed):
    driveTrain.turnLeft(leftTurnSpeed)
    return str(leftTurnSpeed)

@app.route('/stop', methods=['GET'])
def handle_stop():
    driveTrain.stop()
    return "stopping"

@app.route('/armPosition/<int:armPosition>', methods=['GET'])
def handle_armPosition(armPosition):
    #needs to be defined
    return str(armPosition)

app.run(host='0.0.0.0')
