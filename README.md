### Tile38 Timestamp Tests

**Problem Analysis(breakdown):**

-   Let points be a collection of planar spatial data(2D space). Then:

    -   If tile38 allows for the addition of a timestamp on these points:

        a. does tile38 perceive timestamps as an additional dimension, or,

        b. does tile38 simply add a timestamp as "alphanumerical" data?

        c. can events(cross, enter, exit and inside) derive time data based on these timestamps?

---

**Plan of attack:**

1. Create Test and connect to tile38 Server via Redis:

    a. Create Geofence from Polygon with SETHOOK command to DETECT events.

    b. Create 2D-3D points with a timestamp FIELD, that trigger an event.

2. Create Webhook listener in a flask app.

3. command: python server.py

4. While flask server is up,set breakpoints and debug the **_tile38_assignment_solution.py_** file

5. Observe the request.txt.

---

**Final Assertion:**

When a point with **(X,Y,tstamp)** triggers an event, the **_tstamp dimension_** is considered to be a spatial parameter, not a temporal one.
Therefore, adding a timestamp/Z-dimension on 2D-data, is a neat trick to perform calculations on that dimension,
but when 3D-data is essential, timestamp has no place as a dimension (4D points are not allowed).
