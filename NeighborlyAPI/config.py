import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    DB_URL = os.environ.get('DB_URL') or 'mongodb://cosmosdbneighborly:HTzKflcYYNburFBuVdIUXAY0bzaHHDYrnfHURR1U98VXIxd05DK7uQU2aZUtdZE4ItgrwyITGAYjNhcH2WtA4g==@cosmosdbneighborly.mongo.cosmos.azure.com:10255/mongodbneighborly?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosdbneighborly@'

    DATABASE = os.environ.get('DATABASE') or 'mongodbneighborly'