using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class deleter : MonoBehaviour
{

    public Animator anim; // the animator for the turtle graphic
    

    // Update is called once per frame
    void Update()
    {
        StartCoroutine("DeathAnimation");
    }

    IEnumerator DeathAnimation()
    {
        while (anim.GetCurrentAnimatorStateInfo(0).normalizedTime < 1.0f) // if the turtle death animation is not yet over
            yield return null;

        Destroy(gameObject);  // when animation ends, remove turtle object
        
    }
}
