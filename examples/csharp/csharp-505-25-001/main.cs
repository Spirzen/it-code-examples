using UnityEngine;

public class Health : MonoBehaviour
{
    [SerializeField] private float maxHealth = 100f;
    private float current;

    void Awake() => current = maxHealth;

    public void TakeDamage(float amount)
    {
        current = Mathf.Max(0f, current - amount);
        if (current <= 0f)
            Destroy(gameObject);
    }
}
