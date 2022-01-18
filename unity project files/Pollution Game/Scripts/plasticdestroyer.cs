using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class plasticdestroyer : MonoBehaviour
{
    public points points;  // reference to points script, holds score values
    
    void OnCollisionEnter2D(Collision2D coll) // when a collision occurs
        {
        if (coll.otherCollider.gameObject.tag == "net")  // if one of the objects was the net
        {
            if (coll.gameObject.tag == "trash") // if other item was piece of pollution
            {
                
                Destroy(coll.gameObject);  // destroy the pollution object
                points.score++;            // increment score
            }
        }    
    }
}
