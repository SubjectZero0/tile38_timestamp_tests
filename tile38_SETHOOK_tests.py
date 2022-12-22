import redis


def main():
    def test_SETHOOK():
        """
        Sets up a simple hook to test with the webhook listener.
        Subject to change.

        """
        # Connect to the Tile38 server
        client = redis.Redis(host='localhost', port=9851)

        #test the client responds
        client.ping()

        # Clear any existing points in the fleet
        client.execute_command("DROP", "fleet")

        # Add a point to the fleet
        client.execute_command("SET", "fleet", "p1","POINT", 37.7, -122.4, "FIELD", "speed", 75)

        #Add a geofence for the fleet
        client.execute_command("NEARBY", "fleet","FENCE", "POINT",37.7, -122.4, 10000)

        #Set the Hook for the geofence
        res = client.execute_command('SETHOOK', 'inline_tests', 'http://localhost:9851/hook',"NEARBY","fleet","FENCE","DETECT","enter,exit,inside,cross","POINT", 37.7, -122.4)

        # Add more points to the fleet, to trigger the hook.
        client.execute_command("SET", "fleet", "p2", "POINT", 37.8, -122.5, "FIELD", "speed", 50)
        client.execute_command("SET", "fleet", "p3", "POINT", 37.9, -122.6, "FIELD", "speed", 25)

        return res

    test_SETHOOK()

if __name__=="__main__":
    main()

"""
Note: Need to setup a webhook listener, in order to access http://localhost:9851/hook. The listener will be set up in Flask.

"""
