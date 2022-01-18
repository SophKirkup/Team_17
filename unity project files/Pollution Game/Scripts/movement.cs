using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class movement : MonoBehaviour

    
{
    
    public UIScript UIScript;  // script which handles on screen UI, end game and pause game functions
    public GameObject netObj;  // net cursor object

    
    // Update is called once per frame
    void Update()
    {

        if (UIScript.GameIsPaused)
        {
            // make net object invisible while game paused
            netObj.SetActive(false);

        }
        else {
            // make net object visible while game is not paused
            netObj.SetActive(true);
            Vector3 mousePosition = Camera.main.ScreenToWorldPoint(Input.mousePosition); //get mouse position
            mousePosition.z += Camera.main.nearClipPlane; // make sure object is in front of camera
            this.transform.position = mousePosition; // set net position to mouse position
        }
        
       
    }
}
