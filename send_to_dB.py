import sys
import apachelog
import pymongo

from datetime import datetime


# Mongo DB config
MONGO_HOST='localhost'
MONGO_PORT=27017
MONGO_DB_NAME='logging_db'
MONGO_COLLECTION_NAME='access_log_collection'
MONGO_COLLECTION_SIZE=1*1024*1024 #  1MB

# Access Log format. Combined. 
ACCESS_LOG_FORMAT = r'%h %l %l %u %t \"%r\" %>s %b'

# Aliases for apache log parser
ACCESS_ALIAS = {
        '%>s': 'status',
        '%b': 'size',
        '%h': 'client_ip',
        '%r': 'request',
        '%t': 'time',
        '%{Referer}i': 'referer',
        '%{User-Agent}i': 'user_agent' }

# Configure alias
def apachelog_parser_alias(self, name):
    if name in ACCESS_ALIAS: return ACCESS_ALIAS[name]
    else: return name

apachelog.parser.alias = apachelog_parser_alias

# Initialize mongo
def do_mongo_init():
    # Connect allowing slave
    connection = pymongo.MongoClient("localhost", 27017)
    db = connection[MONGO_DB_NAME]
    
    # Mongo will create the collection automacly, BUT we want to set
    # capped collection to enable "log rotation".
    # If you try to create a collection that already exists, it thows
    # pymongo.CollectionInvalid
    try:
        collection = \
            db.create_collection(MONGO_COLLECTION_NAME, 
                                capped = True,
                                size = MONGO_COLLECTION_SIZE)
        print( "New collection created")
    except pymongo.errors.CollectionInvalid:
        # If already exists, get it.
        collection = db[MONGO_DB_NAME]
    
    return (connection, db, collection)


def main():

    (mongo_connection, mongo_db, mongo_collection) = do_mongo_init()
    
    parser = apachelog.parser(ACCESS_LOG_FORMAT)
    file = open('log.txt')
    while True:
        logline = file.readline()
        if logline == '': break
        try:
            data = parser.parse(logline)
            # save as datetime to allow date queries
            (timestamp_str, timezone_str) = data['time'][1:-1].split(' ')
            data['timestamp'] = datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S")
            data['timezone'] = int(timezone_str)
            (data['method'], data['url'], data['proto']) = data['request'].split(' ')
            
            # store the data in the Mongo DB
            mongo_collection.insert_one(data)
            
        except apachelog.ApacheLogParserError:
            # ignore invalid lines
            print('Invalid log format: "' + logline + '"')  
    
    mongo_connection.close()
    
if __name__ == '__main__':
    main()