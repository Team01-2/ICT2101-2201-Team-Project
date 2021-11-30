# To start type "python "flask1.py" in terminal

from flask import Flask, render_template, request
import socket, threading, time, json

#TCP SERVER
HOST = '172.20.10.3'  # Standard loopback interface address (localhost)
PORT = 8000        # Port to listen on (non-privileged ports are > 1023)
data = b'' # storing data receive from car
someData = "" # storing data received from car
conn = {} #global conn
speed = 0
left_rotation = 0
right_rotation = 0
cmd_received = 0
cmd_executed = 0
status = "disconnected"
surface = "White"
s = socket

mapArray1 = []
startPoint1 = []
endPoint1 = []
mapArray2 = []
startPoint2 = []
endPoint2 = []
mapArray3 = []
startPoint3 = []
endPoint3 = []

def launchServer():
    global conn
    global speed
    global left_rotation
    global right_rotation
    global cmd_received
    global cmd_executed
    global status
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    print('listening')
    s.listen()
    conn, addr = s.accept()
    with conn: # when connected
        print('Connected by', addr)
        status = "connected"
        conn.sendall(b'%10')
        while True:
            try:
                data2 = conn.recv(1024)
                length = len(data2) # number of 8 bytes received
                if length == 10: # below it decode the bytes into data
                    counter = 0  # track the current item index
                    for item in data2:
                        if counter <= 1:
                            if counter % 2 == 0:
                                speed = (item - 48) * 10
                            else:
                                speed += item - 48
                        elif counter <= 3:
                            if counter % 2 == 0:
                                left_rotation = (item - 48) * 10
                            else:
                                left_rotation += item - 48
                        elif counter <= 5:
                            if counter % 2 == 0:
                                right_rotation = (item - 48) * 10
                            else:
                                right_rotation += item - 48
                        elif counter <= 7:
                            if counter % 2 == 0:
                                cmd_received = (item - 48) * 10
                            else:
                                cmd_received += item - 48
                        elif counter <= 9:
                            if counter % 2 == 0:
                                cmd_executed = (item - 48) * 10
                            else:
                                cmd_executed += item - 48
                        counter += 1

                global data
                data = data2
            except:
                status = "disconnected" # when socket connection is disconnected, reconnect
                s.listen()
                conn, addr = s.accept()
                status = "connected"


app = Flask(__name__)

# direct to main page index-start.html
@app.route("/")
def home():
    return render_template("index-start.html")

# direct to admin-panel.html
@app.route("/adminPanel")
def adminPanel():
    global s
    try:
        conn.sendall(b'%c0') #prompt robot car for speed, left rotation info etc
    finally:
        return render_template("admin-panel.html", speed=speed, left_rotation=left_rotation, right_rotation=right_rotation, cmd_received=cmd_received, cmd_executed=cmd_executed, status=status, surface=surface)

# direct to main page index-start.html
@app.route("/indexStart")
def indexStart():
    return render_template("index-start.html")

# direct to play-screen.html
@app.route("/playScreen")
def playScreen():
    return render_template("play-screen.html")


#@app.route('/rotate_left')
#def send_left():
    #conn.sendall(b'%l0')
    #return render_template("index.html")

#@app.route('/move_up')
#def send_up():
    #conn.sendall(b'%u0')
    #return render_template("index.html")


#@app.route('/move_back')
#def send_back():
    #conn.sendall(b'%b0')
    #return render_template("index.html")


#@app.route('/rotate_right')
#def send_right():
    #conn.sendall(b'%r0')
    #return render_template("index.html")


#@app.route('/stop')
#def send_stop():
    #conn.sendall(b'%s0')
    #return render_template("index.html")


# always called by javascript to access robot car reply
@app.route('/receiveOK', methods=['POST'])
def receiveOK():
    global someData
    global surface
    if someData == "GO":
        surface = "White"
    elif someData == "KO":
        surface = "Black"
    someData1 = someData
    someData = ""
    return someData1


#when save button is pressed
@app.route('/saveMap/<string:mapData>', methods=['POST'])
def saveMap(mapData):
    global mapArray1
    global mapArray2
    global mapArray3
    global startPoint1
    global startPoint2
    global startPoint3
    global endPoint1
    global endPoint2
    global endPoint3
    mapData = json.loads(mapData)
    index = mapData['index']
    if index == 1:
        mapArray1 = mapData['map']
        startPoint1 = mapData['start']
        endPoint1 = mapData['end']
    elif index == 2:
        mapArray2 = mapData['map']
        startPoint2 = mapData['start']
        endPoint2 = mapData['end']
    elif index == 3:
        mapArray3 = mapData['map']
        startPoint3 = mapData['start']
        endPoint3 = mapData['end']
    print(mapData['map'])
    print(mapData['start'])
    print(mapData['end'])
    return "Map saved successfully"


#when upload button is pressed, command list is pass using post
@app.route('/upload/<string:commands>', methods=['POST'])
def upload(commands):
    global commandList
    commands = json.loads(commands)
    commandList = []
    print(f"User Name: {commands['name']}")
    for item in commands['name']:
        if item == "up":
            commandList.append(b'%u0')
        elif item == "down":
            commandList.append(b'%b0')
        elif item == "left":
            commandList.append(b'%l0')
        elif item == "right":
            commandList.append(b'%r0')
    return "uploaded Successfully"


#called when run button is clicked
@app.route('/run')
def run():
    global commandList
    global data
    global someData
    t_end = time.time() + 10
    for cmd in commandList:
        counter = 0
        data = b'o'
        conn.sendall(cmd)
        while True:
            if data == b'GO':  # when car about to execute command
                if counter == 0:
                    someData = "GO"
                    counter = 1
            if data == b'OK':  # when commands executed by robot car successfully
                time.sleep(1)
                break
            if data == b'KO': # when black line is detected
                someData = "KO"
                commandList.clear()
                break
            if time.time() > t_end:   # when web portal don't get OK reply after sending commands. Might want to handle this
                print("time is up")
                someData = "TO"  # TO = Timeout
                commandList.clear()
                break
        t_end = time.time() + 10  # reset timer
    commandList = []
    return render_template("play-screen.html")

#direct map editor page
@app.route('/mapEditor')
def go_mapEditor():
    mapData = {
        "map1": mapArray1,
        "start1": startPoint1,
        "end1": endPoint1,
        "map2": mapArray2,
        "start2": startPoint2,
        "end2": endPoint2,
        "map3": mapArray3,
        "start3": startPoint3,
        "end3": endPoint3,
    }

    # convert into JSON:
    mapData = json.dumps(mapData)
    return render_template("mapEditor.html", mapData=mapData)


if __name__ == "__main__":
    t = threading.Thread(target=launchServer)
    t.daemon = True
    t.start()
    app.run(debug=False)