using UnityEngine;

public class PatrolBetweenPoints : MonoBehaviour
{
    [SerializeField] private Transform pointA;
    [SerializeField] private Transform pointB;
    [SerializeField] private float speed = 3f;

    private Transform currentTarget;

    void Start() => currentTarget = pointB;

    void Update()
    {
        if (pointA == null || pointB == null) return;

        transform.position = Vector3.MoveTowards(
            transform.position,
            currentTarget.position,
            speed * Time.deltaTime);

        if (Vector3.Distance(transform.position, currentTarget.position) < 0.05f)
            currentTarget = currentTarget == pointA ? pointB : pointA;
    }
}
