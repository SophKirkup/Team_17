using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Threading.Tasks;
using System;

public class spawntrash : MonoBehaviour
{
    public float Cooldown_Ms_Min = 500f;  //min value for cooldown, defaults to 500 but changed in unity editor
    public float Cooldown_Ms_Max = 500f;  //max value for cooldown, defaults to 500 but changed in unity editor
    public List<GameObject> trashVariants;// list of prefab objects (blueprints) that can be spawned as a piece of pollution
    public bool canspawn = true;            
    System.Random rnd = new System.Random();
    public UIScript UIScript;             // script which handles on screen UI, end game and pause game functions


    // Start is called before the first frame update
    void Start()
    {
        StartCoroutine(Spawning()); // start trying to spawn pollution
    }

    IEnumerator Spawning()
    {
        while (Application.isPlaying)  // double checks application is running, this doesnt affect anything in final
                                       // build of game, but prevents errors while game runs in the editor,
                                       // where script would try spawning an object after game has been closed.
        {
            spawn();                   // attempt to spawn an item of pollution
            yield return new WaitForSeconds(UnityEngine.Random.Range(Cooldown_Ms_Min, Cooldown_Ms_Max)/1000f);
                                       // waits for a random time between min and max values before spawning again
        }
        
    }

    void spawn()
    {
        if (canspawn && !UIScript.GameIsPaused) {  // if game is not paused and pollution is able to be spawned

            GameObject tmp = Instantiate(trashVariants[rnd.Next(trashVariants.Count)]);
            // instantiate random pollution object from trashVariants list

            tmp.transform.position = this.transform.position;
            // move position of created pollution to location of spawner
        }
    }
}
