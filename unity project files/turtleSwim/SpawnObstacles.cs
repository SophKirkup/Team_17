using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SpawnObstacles : MonoBehaviour
{
    public GameObject obstacle;
    public float maxX;// max x positon obstacle can spawn
    public float minX;// min x position obstacle can spawn
    public float maxY;// max y positon obstacle can spawn
    public float minY;// min y position obstacle can spawn
    public float timeBetweenSpawn;
    private float spawnTime;


    // Update is called once per frame
    void Update()
    {
        if(Time.time > spawnTime)
        {
            Spawn();
            spawnTime = Time.time + timeBetweenSpawn;// checks time between spawns
        }
    }

    void Spawn()
    {
        float randomX = Random.Range(minX,maxX);// creates random coordinates
        float randomY = Random.Range(minY,maxY);

        Instantiate(obstacle,transform.position + new Vector3(randomX,randomY, 0), transform.rotation);// spawns obstacle
    }

}
