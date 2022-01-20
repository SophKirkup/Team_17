using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Obstacle : MonoBehaviour
{

    private GameObject player;
    // Start is called before the first frame update
    void Start()
    {
        player = GameObject.FindGameObjectWithTag("Player");
        // as soon as game is started script locates player
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if(collision.tag == "Border")
        {
            Destroy(this.gameObject);// if obstacle collides with border, obstacle is destroyed
        }

        else if(collision.tag == "Player")
        {
            Destroy(player.gameObject);// if player collides with obstacle, player is destroyed
        }
    }

}
