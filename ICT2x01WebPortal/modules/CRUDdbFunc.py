import mysql.connector
import datetime
import json # serialise for storage

cnx = None
cursor = None


# datatypes: string, list, list, list
def insert_cmap(mapname, obstaclearray, startpoint, endpoint):
    try:
        stmt_cmap = "INSERT INTO challengemaps (map_name, obstacle_array, start_point, end_point) VALUES (%s, %s, %s, %s)"  # prepared statement
        data_cmap = (mapname, json.dumps(obstaclearray), json.dumps(startpoint),
                     json.dumps(endpoint))  # data to be inserted - serialise python datatypes

        cursor.execute(stmt_cmap, data_cmap)  # INSERT INTO challengemaps VALUES;
        cnx.commit()  # commit changes
        return "Inserted successfully"
    except:
        return "Inserted unsuccessfully"


# datatypes: string, list
def insert_comhist(author, commandarray):
    stmt_comhist = "INSERT INTO commandhistory (upload_time, author, commandarray) VALUES (%s, %s, %s)"  # prepared statement
    data_comhist = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), author,
                    json.dumps(commandarray))  # data to be inserted - serialise python datatypes

    cursor.execute(stmt_comhist, data_comhist)  # INSERT INTO commandhistory VALUES;
    cnx.commit()  # commit changes
    return "Inserted successfully"


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
        print("error query db")
    x = (row1[0], json.loads(row1[1]), json.loads(row1[2]),
         json.loads(row1[3]), row2[0], json.loads(row2[1]), json.loads(row2[2]),
         json.loads(row2[3]), row3[0], json.loads(row3[1]), json.loads(row3[2]),
         json.loads(row3[3]))  # deserialise obstaclearray, startpoint, endpoint json string
    print(x)
    return x


# use alter_cmap if mapname already exists, don't try to insert a new one with the same name - primary key violation
# datatypes: string, list, list, list
#def alter_cmap(mapname, obstaclearray, startpoint, endpoint):
    #stmt_cmap = "UPDATE challengemaps SET obstacle_array = %s, start_point = %s, end_point = %s WHERE map_name = %s"  # prepared statement
    #data_cmap = (json.dumps(obstaclearray), json.dumps(startpoint), json.dumps(endpoint),
                 #mapname)  # redo the whole row if anything under an existing map name needs to change

    #cursor.execute(stmt_cmap, data_cmap)  # UPDATE challengemaps SET values;
    #cnx.commit()  # commit changes


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

    print(result)
    return result


# datatypes: string
def delete_cmap(mapname):
    stmt_cmap = "DELETE FROM challengemaps WHERE map_name = %s"  # prepared statement
    data_cmap = (mapname,)  # map to be deleted

    cursor.execute(stmt_cmap, data_cmap)  # DELETE FROM challengemaps WHERE;
    cnx.commit()  # commit changes
    return "Deleted map successfully"


# init
def init_db():
    global cnx
    cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='2201')  # use `2201`;
    global cursor
    cursor = cnx.cursor(buffered=True)  # set to True to make sure all retrieved rows put into cursor