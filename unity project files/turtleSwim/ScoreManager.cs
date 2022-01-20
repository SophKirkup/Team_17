using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine;
using UnityEngine.UI;

public class ScoreManager : MonoBehaviour
{
    public Text scoreText;
    public float score;




    // Update is called once per frame
    void Update()
    {
        if(GameObject.FindGameObjectWithTag("Player")!= null)// if player is alive
        {
            score += 1 * Time.deltaTime;// score is equal to total time passed
            scoreText.text = ((int)score).ToString();
        }
    }
}
