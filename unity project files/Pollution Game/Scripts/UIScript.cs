using System.Collections.Generic;
using UnityEngine.SceneManagement;
using TMPro;

//request imports
using UnityEngine.Networking;
using System;
using System.Collections;
using UnityEngine;
using SimpleJSON;

public class UIScript : MonoBehaviour
{

    public GameObject pauseCanvas;           // canvas which holds the pause menu
    public bool GameIsPaused;
    public GameObject MainCanvas;            // canvas holding main UI, eg scoretext, pause button etc
    public GameObject StartCanvas;           // canvas holding the main menu shown before game
    public GameObject EndCanvas;             // canvas holding the end screen
    public TextMeshProUGUI EndScoreText;     // TextMeshPro object which displays final score
    public string prefix = "Final Score: ";  // string prefix for final score UI element

    // these values are used in checksum generation,
    // to ensure the sent score has been sent from this script, and not an external request
    public float s1 = 541f;
    public float s2 = 225f;  // these values are hard coded into both games, and the web server


    string scorify(int score)  // turns score integer into presentable string in form "Final Score: x"
    {
        return (prefix + score.ToString());
    }

    // Start is called before the first frame update
    void Start()
    {
        // ensures that the correct screens are shown when game loads

        Time.timeScale = 0.0f;         // pause time, stops any in game objects from moving, spawning items etc
        StartCanvas.SetActive(true);   // open start screen
        MainCanvas.SetActive(false);   // hide in game UI
        EndCanvas.SetActive(false);    // hide end screen
    }

    public void Play() {               // called when play button is pressed

        GameIsPaused = false;          
        StartCanvas.SetActive(false);  // hide start screen
        MainCanvas.SetActive(true);    // show in-game UI
        Time.timeScale = 1.0f;         // unpause in-game time

    }

    public void EndGame(int points) {    // called when lives reach 0
        EndCanvas.SetActive(true);       // show end screen
        MainCanvas.SetActive(false);     // hide in-game UI
        GameIsPaused = true;
        Time.timeScale = 0.0f;           // pause in-game time
        SubmitScore(points);             // submit score to web server
        EndScoreText.SetText(scorify(points)); // display final score on end screen
    }

    public void Unpause() {     
        GameIsPaused = false;
        Time.timeScale = 1.0f;   // unpause in-game time
    }

    public void Pause()
    {
        pauseCanvas.SetActive(true);  // show pause screen
        GameIsPaused = true;
        Time.timeScale = 0.0f;   // pause in-game time
    }

    public void Restart() {                  // called by restart/play again button on end screen
        SceneManager.LoadScene("TurtleGame"); // reload scene
    }

    void SubmitScore(int score) {
        if(score > 0) {StartCoroutine(PostScore(score));}  // only send positive none zero scores, stops
                                                           // divide by zero errors. score of zero does not 
                                                           // need to be sumbitted, so prevents unnessasary
                                                           // http requests
    }

    IEnumerator PostScore(int score)
    {

        WWWForm form = new WWWForm();
        form.AddField("sourceGame", "PollutionGame");    // add value to POST body
        form.AddField("score", score);                   // add value to POST body
        form.AddField("checkSum", (((s1 + score) * s2) * s1).ToString()); // add value to POST body
        // checksum is calculated here, and same calculation is done in reverse on server to check if score is legitimate.
        // discourages illegitimate POST requests being sent by a third party to cheat

        // address here is hard coded, so that is why port must remain static on webserver to allow score submission.
        using (UnityWebRequest www = UnityWebRequest.Post("http://127.0.0.1:5000/submitScore", form))
        {
            yield return www.SendWebRequest(); // wait until response is recieved

            if (www.isNetworkError || www.isHttpError)  // if a network or http error has occurred
            {
                if (www.error == "Cannot connect to destination host") {  // this happens when server is not turned on, most likely error when running game in editor
                    Debug.Log("Error - Could not connect to server, therefore score has not been saved");
                    // these error messages can be seen in web browser through 
                    // (Web developer tools/ inspect element) -> (Console Tab)
                }
                else {  // if other error
                    Debug.Log(www.error); // display error message in console
                }
                    
            }
            else
            {

                /*     Server sends JSON formatted response of:
                         {
                         "errors": string[],
                         "success": bool,
                         "score": int,
                         "game": string
                         }

                        possible error messages include:

                        -noUserLoggedIn
                        -noCheckSum
                        -checksumFalse
                        -noScore
                        -noSourceGame
                */


                Debug.Log("Score sent to server!");
                var  responseJSON = JSON.Parse(www.downloadHandler.text);  // parse response into JSONNode
                List<String> responseErrors = new List<String>();          // initalise list

                foreach (JSONNode error in responseJSON["errors"])         // for every error sent in response
                {
                    responseErrors.Add(error.Value);                       // add to responseErrors
                }
                
               
                if (responseErrors.Count != 0)  // if there were any error messages sent in response
                {
                    Debug.Log("Server response - Score not saved, errors: " + String.Join(",",responseErrors));  // display error message
                }
                else { // if no errors
                    //display confirmation message in console
                    Debug.Log("Server response - Successfully recieved score of "+ responseJSON["score"].Value + " from "+responseJSON["game"].Value+"!");
                }
            }
        }
    }
}
