using UnityEngine;

public class PlayerShooting : MonoBehaviour
{
    [SerializeField] private GameObject projectilePrefab;
    [SerializeField] private Transform firePoint;
    [SerializeField] private float projectileSpeed = 25f;

    void Update()
    {
        if (!Input.GetMouseButtonDown(0)) return;
        if (GameManager.Instance != null && !GameManager.Instance.TryConsumeAmmo()) return;

        GameObject shot = Instantiate(projectilePrefab, firePoint.position, firePoint.rotation);
        if (shot.TryGetComponent<Rigidbody>(out var rb))
        {
#if UNITY_6000_0_OR_NEWER
            rb.linearVelocity = firePoint.forward * projectileSpeed;
#else
            rb.velocity = firePoint.forward * projectileSpeed;
#endif
        }
    }
}
