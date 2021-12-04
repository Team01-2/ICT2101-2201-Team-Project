import mysql.connector
import datetime
import json # serialise for storage

cnx = None
cursor = None

# datatypes: string, list, list, list
def insert_cmap (mapname, obstaclearray, startpoint, endpoint):
    stmt_cmap = "INSERT INTO challengemaps (map_name, obstacle_array, start_point, end_point) VALUES (%s, %s, %s, %s)" # prepared statement
    data_cmap = (mapname, json.dumps(obstaclearray), json.dumps(startpoint), json.dumps(endpoint)) # data to be inserted - serialise python datatypes
    
    cursor.execute(stmt_cmap, data_cmap) # INSERT INTO challengemaps VALUES;
    cnx.commit() # commit changes

# datatypes: string, list
def insert_comhist (author, commandarray):
    stmt_comhist = "INSERT INTO commandhistory (upload_time, author, commandarray) VALUES (%s, %s, %s)" # prepared statement
    data_comhist = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), author, json.dumps(commandarray)) # data to be inserted - serialise python datatypes
    
    cursor.execute(stmt_comhist, data_comhist) # INSERT INTO commandhistory VALUES;
    cnx.commit() # commit changes

# datatypes: string
# returns: tuple
def select_cmap (mapname):
    stmt_cmap = "SELECT * FROM challengemaps WHERE map_name = %s" # prepared statement
    data_cmap = (mapname, ) # map to be selected
    
    cursor.execute(stmt_cmap, data_cmap) # SELECT * FROM challengemaps WHERE;
    result = cursor.fetchone()
    x = (result[0], json.loads(result[1]), json.loads(result[2]), json.loads(result[3])) # deserialise obstaclearray, startpoint, endpoint json string
    
    return x

# use alter_cmap if mapname already exists, don't try to insert a new one with the same name - primary key violation
# datatypes: string, list, list, list
def alter_cmap (mapname, obstaclearray, startpoint, endpoint):
    stmt_cmap = "UPDATE challengemaps SET obstacle_array = %s, start_point = %s, end_point = %s WHERE map_name = %s" # prepared statement
    data_cmap = (json.dumps(obstaclearray), json.dumps(startpoint), json.dumps(endpoint), mapname) # redo the whole row if anything under an existing map name needs to change
    
    cursor.execute(stmt_cmap, data_cmap) # UPDATE challengemaps SET values;
    cnx.commit() # commit changes

# always select all, full command history
# returns: list of tuples
def select_comhist:
    stmt_comhist = "SELECT * FROM commandhistory" # prepared statement
    cursor.execute(stmt_comhist) # SELECT * FROM commandhistory
    
    result = cursor.fetchall()
    for x in result:
        x = (x[0].isoformat(sep=' '), x[1], json.loads(x[2])) # make datetime human readable, deserialise commandarray json string too
        result.pop()
        result.insert(0, x) # replace the tuple because tuples are immutable, tsk
        
    return result

# datatypes: string
def delete_cmap (mapname):
    stmt_cmap = "DELETE FROM challengemaps WHERE map_name = %s" # prepared statement
    data_cmap = (mapname, ) # map to be deleted
    
    cursor.execute(stmt_cmap, data_cmap) # DELETE FROM challengemaps WHERE;
    cnx.commit() # commit changes

# init
def init_db():
    global cnx
    cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='2201') # use `2201`;
    global cursor
    cursor = cnx.cursor(buffered=True) # set to True to make sure all retrieved rows put into cursor

def shutdown():
    global cursor
    cursor.close() # pack it up, cursor then connection
    global cnx
    cnx.close()