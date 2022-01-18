using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class trashCollect : MonoBehaviour
{

    public points points;  // points script holds score values

    void OnTriggerEnter2D(Collider2D col)  // when collision occurs with the piece of pollution this script is attached to
    {
        if (col.gameObject.tag == "net")   // if item collided with is the net
        {
            Destroy(this);                 // destroy self
            points.score++;                // increment score
        }
    }
}
