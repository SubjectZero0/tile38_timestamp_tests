import redis
import geojson


def test_solution():
    # Connect to the Tile38 server
        client = redis.Redis(host='localhost', port=9851, db=0)

        #test the client responds
        client.ping()

        # Clear any existing data
        client.execute_command("FLUSHDB")

        #create a polygon to set as a geofence
        geo_json= geojson.Polygon([[(2.38, 57.322), (23.194, -20.28), (-120.43, 19.15), (2.38, 57.322)]])

        #Set Hook for the geofence
        client.execute_command('SETHOOK', 'inline_tests', 'http://localhost:5000/hook',"WITHIN","fleet","FENCE","DETECT","enter,exit,inside,cross","OBJECT", geo_json)

        """Add more points to the fleet, to trigger the hook."""

        #point X,Y,tstamp and FIELD timestamp
        p1 = client.execute_command("SET", "fleet", "p1", "POINT", 57.321,2.379, 1671731640, "FIELD", "speed", 50, "FIELD", "timestamp", 1671731640)

        #point X,Y and FIELD timestamp
        p2 = client.execute_command("SET", "fleet", "p2", "POINT", 57.321,2.379, "FIELD", "speed", 50, "FIELD", "timestamp", 1571731640)

        #point X,Y,tstamp
        p3 = client.execute_command("SET", "fleet", "p3", "POINT", 57.321,2.379, 1471731640, "FIELD", "speed", 50)

        #point X,Y,Z,tstamp and FIELD timestamp. tstamp in the coordinates is an invalid argument, as expected.
        p4 = client.execute_command("SET", "fleet", "p4", "POINT", 57.321, 2.379,100, 1671731640, "FIELD", "speed", 50, "FIELD", "timestamp", 1671731640)


if __name__ == '__main__':
   test_solution()
   