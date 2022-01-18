using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;


public class spawnerMovement : MonoBehaviour
{
    public GameObject rightBound;   // bounding object for spawner movement
    public GameObject leftBound;    // bounding object for spawner movement
    [Range(0, 5)]                   // provides a slider for moveSpeed to be set between 0 and 5 in the unity editor
    public float moveSpeed; 
    public bool goLeft;             // should spawner move left on next tick?

    // Start is called before the first frame update
    void Start()
    {
        System.Random rand = new System.Random();       // generate random float between 0 and 1
        goLeft = (rand.NextDouble() > 0.5);             // if random number is more than 0.5, move left first
                                                        // (essentially randomises starting direction)

    }

    // FixedUpdate is called once per frame, FixedUpdate is to be used with physics scripts for better timing.
    void FixedUpdate()
    {
        float rightXValue = rightBound.transform.position.x;  // get right bound x coordinate
        float leftXValue = leftBound.transform.position.x;    // get left bound x coordinate
        float selfX = this.transform.position.x;              // get spawner current x coordinate

        if (moveSpeed < 0) {                                  // leftover code, makes sure moveSpeed is positive
            moveSpeed = -1 * moveSpeed;                       // in case of typo in editor
        }

        
        // check which direction to move and move in that direction

        if (goLeft)                 // if should move left
        {
            if (selfX <= leftXValue)        // if past left bound
            {
                goLeft = false;             // move right next tick
            }
            else {                          // if not past left bound
                this.transform.Translate(new Vector3(-1 * moveSpeed, 0, 0)); // move left with moveSpeed
            }
        }
        else
        {                          // if should move right
            if (selfX >= rightXValue)   // if past right bound
            {
                goLeft = true;          // move left next tick
            }
            else
            {                      // if not past right bound
                this.transform.Translate(new Vector3(1 * moveSpeed, 0, 0));  // move left with moveSpeed
            }
        }
    }
}
