import mysql.connector
import datetime

cnx = None
cursor = None

# datatypes: string, list, Point, Point
def insert_cmap (mapname, obstaclearray, startpoint, endpoint):
    stmt_cmap = "INSERT INTO challengemaps (map_name, obstacle_array, start_point, end_point) VALUES (%s, %s, %s, %s)" # prepared statement
    data_cmap = (mapname, obstaclearray, startpoint, endpoint) # data to be inserted
    cursor.execute(stmt_cmap, data_cmap) # INSERT INTO challengemaps VALUES;
    cnx.commit() # commit changes

# datatypes: string, list
def insert_comhist (author, commandarray):
    stmt_comhist = "INSERT INTO commandhistory (upload_time, author, commandarray) VALUES (%s, %s, %s)" # prepared statement
    data_comhist = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), author, commandarray) # data to be inserted
    cursor.execute(stmt_comhist, data_comhist) # INSERT INTO commandhistory VALUES;
    cnx.commit() # commit changes

# datatypes: string
# returns: list of tuples
def select_cmap (mapname):
    stmt_cmap = "SELECT * FROM challengemaps WHERE map_name = %s" # prepared statement
    data_cmap = (mapname, ) # map to be selected
    cursor.execute(stmt_cmap, data_cmap) # SELECT * FROM challengemaps WHERE;
    return cursor.fetchone() # is blob datatype in database wrong? IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT CHECK THIS

# returns: list of tuples
def select_comhist:
    stmt_comhist = "SELECT * FROM commandhistory" # prepared statement
    cursor.execute(stmt_comhist) # SELECT * FROM commandhistory
    result = cursor.fetchall()
    
    for x in result:
        x = (x[0].isoformat(sep=' '), x[1], x[2]) # make datetime human readaable
        result.pop()
        result.insert(0, x) # replace the tuple because tuples are immutable, dumb
    return result

# datatypes: string
def delete_cmap (mapname):
    stmt_cmap = "DELETE FROM challengemaps WHERE map_name = %s" # prepared statement
    data_cmap = (mapname, ) # map to be deleted
    cursor.execute(stmt_cmap, data_cmap) # DELETE FROM challengemaps WHERE;
    cnx.commit() # commit changes


def init_db():
    
    # init
    global cnx
    cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='2201') # use `2201`;
    global cursor
    cursor = cnx.cursor(buffered=True) # set to True to make sure all retrieved rows put into cursor


def shutdown():
    global cursor
    cursor.close() # pack it up, cursor then connection
    global cnx
    cnx.close()