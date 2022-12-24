import geojson
import redis
import ast


#-------------------------------------------------------

def to_dict(a):
    #helper function to convert bytes object to dict
    return ast.literal_eval(a.decode('utf-8'))

#--------------------PREP TEST-------------------------

def test_create_point():
    """
    General tile38 Test
    """
    #set the client to redis. port 9851 for tile38
    client = redis.Redis(host='127.0.0.1', port=9851)

    client.execute_command("DROP", "fleet")

    # insert data
    result = client.execute_command('SET', 'fleet', 'truck', 'POINT', 33.32, 115.423)
   
    #Assert the SET command is executed
    assert result == True
    
    #get the result point as a dictionary
    point = to_dict(client.execute_command('GET', 'fleet', 'truck'))
    
    #assert the points coordinates are as expected
    assert [115.423,33.32] in point.values()



#------------------END OF PREP TEST-------------------


if __name__ == '__main__':
    test_create_point()
    