using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{

  public float playerSpeed;
  private Rigidbody2D rb;
  private Vector2 playerDirection;
    // Start is called before the first frame update
    void Start()
    {
      rb = GetComponent<Rigidbody2D>();// references player object in editor

    }

    // Update is called once per frame
    void Update()
    {
      float directionY = Input.GetAxisRaw("Vertical");// handles input to move player
      playerDirection = new Vector2(0, directionY).normalized;

    }

    // called once per physics frame
    void FixedUpdate()
    {
      rb.velocity = new Vector2(0, playerDirection.y * playerSpeed);

    }
}
