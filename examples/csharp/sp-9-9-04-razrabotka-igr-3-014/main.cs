using UnityEngine;
using UnityEngine.AI;

public class EnemyPatrol : MonoBehaviour
{
    [SerializeField] private Transform[] waypoints;
    private NavMeshAgent agent;
    private int index;

    void Awake() => agent = GetComponent<NavMeshAgent>();

    void Start()
    {
        if (waypoints.Length > 0)
            agent.SetDestination(waypoints[0].position);
    }

    void Update()
    {
        if (waypoints.Length == 0 || agent.pathPending) return;
        if (agent.remainingDistance <= agent.stoppingDistance)
        {
            index = (index + 1) % waypoints.Length;
            agent.SetDestination(waypoints[index].position);
        }
    }
}
