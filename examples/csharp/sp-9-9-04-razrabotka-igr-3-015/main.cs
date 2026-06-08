using UnityEngine;

public class EnemyHealth : MonoBehaviour
{
    [SerializeField] private float maxHealth = 30f;
    private float current;

    void Awake() => current = maxHealth;

    public void TakeDamage(float amount)
    {
        current -= amount;
        if (current <= 0f)
            Destroy(gameObject);
    }
}
