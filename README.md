# Virtual_Environmentalists - Sea Savers website

## Games

Games have been created in Unity, the files in the `../static/PollutionGame/` 
and `../static/TurtleGame/`
 folders are the built files generated by Unity to run in Unity's WebGL player.
 the `pollutionGame.html` and `turtleGame.html` files were also generated by unity,
  and edited to fit
  better within our website. The scripts, art, and other files used in the 
  development of the games can be found at `PUT PATH HERE`.
  
  In order to run the games, you must have a screen of at least 960 
by 720 pixels, and be using a computer, as mobile is not supported by the Unity WebGL player.

If the website is not running correctly on your network, or port 5000 is not 
available, you can change the `StaticPort` variable in `app.py` to **False**, which
will dynamically assign the port to one which is free.

**PLEASE NOTE: Assigning a port dynamically will stop games from correctly submitting 
scores to the server/database, so scores will not be saved.**

### Pollution Game

### Turtle Game

