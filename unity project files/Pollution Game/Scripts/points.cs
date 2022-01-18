using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class points : MonoBehaviour
{
    public int score;                  
    public TextMeshProUGUI ScoreText;   // score UI element
    public string prefix = "Score: ";   // string prefix for score UI element
    

    // Start is called before the first frame update
    void Start()
    {
        ScoreText.SetText(scorify(score));  // Display current score
    }

    // Update is called once per frame
    void Update()
    {
        ScoreText.SetText(scorify(score));   // Display current score
    }

    string scorify(int score) {       // turns score integer into presentable string in form "Score: x"

        return (prefix + score.ToString());
    }

}
