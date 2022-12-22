### Vesselbot assignment Solution

**Problem Analysis(breakdown):**

-   Let points be a collection of planar spatial data(2D space). Then:

    -   If tile38 allows for the addition of a timestamp on these points:

        a. does tile38 perceive timestamps as an additional dimension, or,

        b. does tile38 simply add a timestamp as "alphanumerical" data?

        c. can events(cross, enter, exit and inside) derive time data based on these timestamps?

**Plan of attack:**

1. Create Test and connect to tile38 Server via Redis:

    a) Create Geofence from Polygon with SETHOOK command to DETECT events.

    b) Create a 2D point with a timestamp FIELD, that triggers an event.

2. Create Webhook listener in a flask app.

3. command:flask run

4. While flask app is up, debug the TEST file

5. Observe the request json. Assert if:

    -Events have timestamps. If they do:

    -is the timestamp a completely new one, or is it one of the previously defined ones?

---

Test idea:
If a point with (X,Y,tstamp) considers tstamp to be a third spatial dimension, instead of temporal,
then, 2 points with the same X, Y but different tstamp, will NEVER trigger an event.
That means, tstamp(int) behaves as Height and not as time.
