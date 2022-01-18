using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class pause_ui : MonoBehaviour

{

    public GameObject pauseCanvas; 
  
    public void Unpause() {

        pauseCanvas.SetActive(false); // disable pause menu
    }
}
