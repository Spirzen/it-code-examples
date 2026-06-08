using UnityEngine;

public class ChasePlayer : MonoBehaviour
{
    [SerializeField] private Transform player;
    [SerializeField] private float speed = 4f;
    [SerializeField] private float stopDistance = 1.5f;

    void Update()
    {
        if (player == null) return;

        Vector3 toPlayer = player.position - transform.position;
        toPlayer.y = 0f;

        if (toPlayer.magnitude <= stopDistance) return;

        transform.position += toPlayer.normalized * speed * Time.deltaTime;
        transform.rotation = Quaternion.LookRotation(toPlayer);
    }
}
