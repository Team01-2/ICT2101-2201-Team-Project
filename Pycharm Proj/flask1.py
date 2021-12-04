# To start type "python "flask1.py" in terminal
import mysql.connector
from datetime import datetime
from flask import Flask, render_template, request
import socket, threading, time, json

cnx = None
cursor = None


# datatypes: string, list, list, list
def insert_cmap(mapname, obstaclearray, startpoint, endpoint):
    stmt_cmap = "INSERT INTO challengemaps (map_name, obstacle_array, start_point, end_point) VALUES (%s, %s, %s, %s)"  # prepared statement
    data_cmap = (mapname, json.dumps(obstaclearray), json.dumps(startpoint),
                 json.dumps(endpoint))  # data to be inserted - serialise python datatypes

    cursor.execute(stmt_cmap, data_cmap)  # INSERT INTO challengemaps VALUES;
    cnx.commit()  # commit changes


# datatypes: string, list
def insert_comhist(author, commandarray):
    stmt_comhist = "INSERT INTO commandhistory (upload_time, author, commandarray) VALUES (%s, %s, %s)"  # prepared statement
    data_comhist = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), author,
                    json.dumps(commandarray))  # data to be inserted - serialise python datatypes

    cursor.execute(stmt_comhist, data_comhist)  # INSERT INTO commandhistory VALUES;
    cnx.commit()  # commit changes


# datatypes: string
# returns: tuple
def select_cmap():
    stmt_cmap = "SELECT * FROM challengemaps"  # prepared statement

    cursor.execute(stmt_cmap)  # SELECT * FROM challengemaps WHERE;
    result = cursor.fetchall()
    try:
        row1 = ("", '[]', '[]', '[]')
        row2 = ("", '[]', '[]', '[]')
        row3 = ("", '[]', '[]', '[]')
        row1 = result[0]
        row2 = result[1]
        row3 = result[2]
    except:
        print("db error")
    x = (row1[0], json.loads(row1[1]), json.loads(row1[2]),
         json.loads(row1[3]), row2[0], json.loads(row2[1]), json.loads(row2[2]),
         json.loads(row2[3]), row3[0], json.loads(row3[1]), json.loads(row3[2]),
         json.loads(row3[3]))  # deserialise obstaclearray, startpoint, endpoint json string

    return x


# use alter_cmap if mapname already exists, don't try to insert a new one with the same name - primary key violation
# datatypes: string, list, list, list
def alter_cmap(mapname, obstaclearray, startpoint, endpoint):
    stmt_cmap = "UPDATE challengemaps SET obstacle_array = %s, start_point = %s, end_point = %s WHERE map_name = %s"  # prepared statement
    data_cmap = (json.dumps(obstaclearray), json.dumps(startpoint), json.dumps(endpoint),
                 mapname)  # redo the whole row if anything under an existing map name needs to change

    cursor.execute(stmt_cmap, data_cmap)  # UPDATE challengemaps SET values;
    cnx.commit()  # commit changes


# always select all, full command history
# returns: list of tuples
def select_comhist():
    stmt_comhist = "SELECT * FROM commandhistory"  # prepared statement
    cursor.execute(stmt_comhist)  # SELECT * FROM commandhistory

    result = cursor.fetchall()
    for x in result:
        x = (x[0].isoformat(sep=' '), x[1],
             json.loads(x[2]))  # make datetime human readable, deserialise commandarray json string too
        result.pop()
        result.insert(0, x)  # replace the tuple because tuples are immutable, tsk

    return result


# datatypes: string
def delete_cmap(mapname):
    stmt_cmap = "DELETE FROM challengemaps WHERE map_name = %s"  # prepared statement
    data_cmap = (mapname,)  # map to be deleted

    cursor.execute(stmt_cmap, data_cmap)  # DELETE FROM challengemaps WHERE;
    cnx.commit()  # commit changes


# init
def init_db():
    global cnx
    cnx = mysql.connector.connect(user='root', password='hahaha99', host='127.0.0.1', database='2201')  # use `2201`;
    global cursor
    cursor = cnx.cursor(buffered=True)  # set to True to make sure all retrieved rows put into cursor


def shutdown():
    global cursor
    cursor.close()  # pack it up, cursor then connection
    global cnx
    cnx.close()

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

# below variable for map usage
mapSelected = 0
name1 = ""
mapArray1 = []
startPoint1 = []
endPoint1 = []
name2 = ""
mapArray2 = []
startPoint2 = []
endPoint2 = []
name3 = ""
mapArray3 = []
startPoint3 = []
endPoint3 = []
cmdHistory = []
cmdTime = []

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
    #cmdHistory = select_comhist
    cmdHistJSON = {
        "cmdHistory": cmdHistory,
        "cmdTime": cmdTime
    }

    # convert into JSON:
    cmdData = json.dumps(cmdHistJSON)
    try:
        conn.sendall(b'%c0') #prompt robot car for speed, left rotation info etc
    finally:
        return render_template("admin-panel.html", speed=speed, left_rotation=left_rotation, right_rotation=right_rotation, cmd_received=cmd_received, cmd_executed=cmd_executed, status=status, surface=surface, cmdData=cmdData)


# direct to main page index-start.html
@app.route("/indexStart")
def indexStart():
    return render_template("index-start.html")


# direct to play-screen.html
@app.route("/playScreen")
def playScreen():
    if mapSelected == 0:
        mapData = {
            "map": []
        }
    elif mapSelected == 1:
        mapData = {
            "name": name1,
            "map": mapArray1,
            "start": startPoint1,
            "end": endPoint1,
        }
    elif mapSelected == 2:
        mapData = {
            "name": name2,
            "map": mapArray2,
            "start": startPoint2,
            "end": endPoint2,
        }
    elif mapSelected == 3:
        mapData = {
            "name": name3,
            "map": mapArray3,
            "start": startPoint3,
            "end": endPoint3,
        }
    mapData = json.dumps(mapData)
    return render_template("play-screen.html", mapData=mapData)


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
    global name1
    global name2
    global name3
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
        name1 = mapData['name']
        mapArray1 = mapData['map']
        startPoint1 = mapData['start']
        endPoint1 = mapData['end']
        insert_cmap(name1, mapArray1, startPoint1, endPoint1)
    elif index == 2:
        name2 = mapData['name']
        mapArray2 = mapData['map']
        startPoint2 = mapData['start']
        endPoint2 = mapData['end']
        insert_cmap(name2, mapArray2, startPoint2, endPoint2)
    elif index == 3:
        name3 = mapData['name']
        mapArray3 = mapData['map']
        startPoint3 = mapData['start']
        endPoint3 = mapData['end']
        insert_cmap(name3, mapArray3, startPoint3, endPoint3)
    return "Map saved successfully"


#when delete button is pressed
@app.route('/deleteMap/<string:mapData>', methods=['POST'])
def deleteMap(mapData):
    global name1
    global name2
    global name3
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
        delete_cmap(name1)
        name1 = ""
        mapArray1 = []
        startPoint1 = []
        endPoint1 = []
    elif index == 2:
        delete_cmap(name2)
        name2 = ""
        mapArray2 = []
        startPoint2 = []
        endPoint2 = []
    elif index == 3:
        delete_cmap(name3)
        name3 = ""
        mapArray3 = []
        startPoint3 = []
        endPoint3 = []
    return "Map deleted successfully"


#when play button is pressed
@app.route('/selectIndex/<string:Index>', methods=['POST'])
def selectIndex(Index):
    global mapSelected
    mapData = json.loads(Index)
    mapSelected = mapData['index']

    return "Switched map successfully"


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
    global cmdHistory
    global cmdTime
    if len(commandList) > 0:
        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")
        for cmd in commandList:
            cmdTime.append(currentTime)
            if cmd == b'%u0':
                insert_comhist("Suhaimi", ["up"])
                cmdHistory.append("up")
            elif cmd == b'%b0':
                insert_comhist("Suhaimi", ["down"])
                cmdHistory.append("down")
            elif cmd == b'%l0':
                insert_comhist("Suhaimi", ["left"])
                cmdHistory.append("left")
            elif cmd == b'%r0':
                insert_comhist("Suhaimi", ["right"])
                cmdHistory.append("right")
    t_end = time.time() + 5
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
        t_end = time.time() + 5  # reset timer
    commandList = []
    return render_template("play-screen.html")


#direct map editor page
@app.route('/mapEditor')
def go_mapEditor():
    global name1, mapArray1, startPoint1, endPoint1, name2, mapArray2, startPoint2, endPoint2, name3, mapArray3, startPoint3, endPoint3
    try:
        print(select_cmap())
        mapsDetail = select_cmap()
        name1 = mapsDetail[0]
        mapArray1 = mapsDetail[1]
        startPoint1 = mapsDetail[2]
        endPoint1 = mapsDetail[3]
        name2 = mapsDetail[4]
        mapArray2 = mapsDetail[5]
        startPoint2 = mapsDetail[6]
        endPoint2 = mapsDetail[7]
        name3 = mapsDetail[8]
        mapArray3 = mapsDetail[9]
        startPoint3 = mapsDetail[10]
        endPoint3 = mapsDetail[11]
    except:
        print("error querying map from db")
    mapData = {
        "name1": name1,
        "map1": mapArray1,
        "start1": startPoint1,
        "end1": endPoint1,
        "name2": name2,
        "map2": mapArray2,
        "start2": startPoint2,
        "end2": endPoint2,
        "name3": name3,
        "map3": mapArray3,
        "start3": startPoint3,
        "end3": endPoint3,
    }

    # convert into JSON:
    mapData = json.dumps(mapData)
    return render_template("mapEditor.html", mapData=mapData)


if __name__ == "__main__":
    init_db()
    t = threading.Thread(target=launchServer)
    t.daemon = True
    t.start()
    app.run(debug=False)