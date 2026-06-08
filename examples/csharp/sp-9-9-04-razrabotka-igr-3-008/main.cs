using UnityEngine;

[RequireComponent(typeof(Rigidbody))]
public class DraggableObject : MonoBehaviour
{
    [SerializeField] private float followSpeed = 15f;
    [SerializeField] private float damping = 20f;

    private Rigidbody rb;
    private Vector3 targetPosition;
    private bool isFollowing;

    private void Awake() => rb = GetComponent<Rigidbody>();

    private void FixedUpdate()
    {
        if (!isFollowing) return;

        Vector3 directionToTarget = targetPosition - rb.position;
        float distanceToTarget = directionToTarget.magnitude;
        Vector3 desiredVelocity = directionToTarget.normalized * followSpeed * distanceToTarget;

        Vector3 current = GetLinearVelocity();
        SetLinearVelocity(Vector3.Lerp(current, desiredVelocity, damping * Time.fixedDeltaTime));
    }

    public void Follow(Vector3 target)
    {
        targetPosition = target;
        isFollowing = true;
        rb.useGravity = false;
    }

    public void StopFollow()
    {
        isFollowing = false;
        rb.useGravity = true;
        SetLinearVelocity(Vector3.zero);
    }

#if UNITY_6000_0_OR_NEWER
    private Vector3 GetLinearVelocity() => rb.linearVelocity;
    private void SetLinearVelocity(Vector3 v) => rb.linearVelocity = v;
#else
    private Vector3 GetLinearVelocity() => rb.velocity;
    private void SetLinearVelocity(Vector3 v) => rb.velocity = v;
#endif
}
