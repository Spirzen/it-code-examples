using UnityEngine;

public class Projectile : MonoBehaviour
{
    [SerializeField] private float damage = 10f;
    [SerializeField] private float lifetime = 3f;
    [SerializeField] private LayerMask hitMask;

    void Start() => Destroy(gameObject, lifetime);

    void OnCollisionEnter(Collision collision)
    {
        if (((1 << collision.gameObject.layer) & hitMask) == 0) return;

        if (collision.collider.TryGetComponent<EnemyHealth>(out var enemy))
            enemy.TakeDamage(damage);

        Destroy(gameObject);
    }
}
