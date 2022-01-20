using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

//request imports
using UnityEngine.Networking;
using System;
using System.Collections;
using UnityEngine;
using SimpleJSON;

public class GameOver : MonoBehaviour
{

    public GameObject gameOverPanel;// refers to game over panel

    public ScoreManager scm;// refers to score manager

    // these values are used to ensure the sent score has been sent from this script, and not an external request
    public float s1 = 541f;
    public float s2 = 225f;


    // Update is called once per frame
    void Update()
    {
        if(GameObject.FindGameObjectWithTag("Player")== null)
        {
            gameOverPanel.SetActive(true);
            float points = scm.score;
            SubmitScore(points);
        }
    }

    public void restart()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }

    void SubmitScore(float score)
    {

        if (score > 0) { StartCoroutine(PostScore(score)); }

    }

    IEnumerator PostScore(float score)
    {

        WWWForm form = new WWWForm();
        form.AddField("sourceGame", "TurtleGame");
        form.AddField("score", score.ToString());
        form.AddField("checkSum", (((s1 + score) * s2) * s1).ToString());


        using (UnityWebRequest www = UnityWebRequest.Post("http://127.0.0.1:5000/submitScore", form))
        {
            yield return www.SendWebRequest();

            if (www.isNetworkError || www.isHttpError)
            {
                if (www.error == "Cannot connect to destination host")
                {
                    Debug.Log("Error - Could not connect to server, therefore score has not been saved");
                }
                else
                {
                    Debug.Log(www.error);
                }

            }
            else
            {
                Debug.Log("Score sent to server!");
                var responseJSON = JSON.Parse(www.downloadHandler.text);
                List<String> responseErrors = new List<String>();

                foreach (JSONNode error in responseJSON["errors"])
                {
                    responseErrors.Add(error.Value);
                }


                if (responseErrors.Count != 0)
                {
                    Debug.Log("Server response - Score not saved, errors: " + String.Join(",", responseErrors));
                }
                else
                {
                    Debug.Log("Server response - Successfully recieved score of " + responseJSON["score"].Value + " from " + responseJSON["game"].Value + "!");
                }

            }
        }
    }
}
