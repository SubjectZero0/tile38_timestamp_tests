import redis
from geojson import Polygon

def main():
    def test_SETHOOK():
        """
        Sets up a simple hook to test with the webhook listener.
        Subject to change.

        """
        # Connect to the Tile38 server
        client = redis.Redis(host='localhost', port=9851, db=0)

        #test the client responds
        client.ping()

        # Clear any existing data
        client.execute_command("FLUSHDB")

        #create a polygon to set as a geofence
        geo_json= Polygon([[(2.38, 57.322), (23.194, -20.28), (-120.43, 19.15), (2.38, 57.322)]])

        #Set WITHIN Hook for the geofence
        client.execute_command('SETHOOK', 'inline_tests', 'http://localhost:5000/hook',"WITHIN","fleet","FENCE","DETECT","enter,exit,inside,cross","OBJECT", geo_json)

        # Add more points to the fleet, to trigger the hook.
        client.execute_command("SET", "fleet", "p1", "POINT", 57.321,2.379, "FIELD", "speed", 50, "FIELD", "timestamp", 1671731640)


    test_SETHOOK()

if __name__=="__main__":
    main()

"""
Note: Need to setup a webhook listener, in order to access http://localhost:5000/hook. The listener will be set up in Flask.

"""
