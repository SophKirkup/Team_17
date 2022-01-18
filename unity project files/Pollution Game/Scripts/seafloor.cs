using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class seafloor : MonoBehaviour
{
    public GameObject canvas;       // main UI canvas used for scoretext, pause button, etc
    public points points;           // points script holds score values
    public GameObject SadTurtle;    // this object plays animation of turtle death
    public int lives = 3;           // starting number of lives
    public List<GameObject> turtles;// List of objects, which respresent the lives remaining graphically
    public UIScript uIScript;       // script which handles on screen UI, end game and pause game functions




    void OnCollisionEnter2D(Collision2D coll)  // when collision with this object occurs
    {

        if (coll.gameObject.tag == "trash")  //if other object in collision event was pollution
        {
            
            GameObject tmp = Instantiate(SadTurtle);          // instantiate a sadTurtle object
            tmp.transform.position = coll.transform.position; // move sadTurtle to the location of collision

            lives = lives - 1;  // decrement lives

            if (lives > -1)   // if lives are 0 or above
            {
                turtles[lives].SetActive(false); // remove the life icon for the correct lost life 
            }

            Destroy(coll.gameObject); // remove the pollution object
            
            points.score = points.score - 1;  // decrement points

            if (lives <= 0) {  // if lives reach 0 or less

                uIScript.EndGame(points.score);  // trigger end of game, pass score
            }
        }
    }
}
