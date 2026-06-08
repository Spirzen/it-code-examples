using UnityEngine;
using UnityEngine.UI;

public class PlayerHealth : MonoBehaviour
{
    [SerializeField] private Slider healthBar; // Ссылка на слайдер
    [SerializeField] private float maxHealth = 100f;
    private float currentHealth;

    void Start()
    {
        currentHealth = maxHealth;
        UpdateHealthBar();
    }

    public void TakeDamage(float damage)
    {
        currentHealth = Mathf.Clamp(currentHealth - damage, 0f, maxHealth);
        UpdateHealthBar();

        if (currentHealth <= 0f)
        {
            // Логика поражения
            Debug.Log("Игрок погиб!");
        }
    }

    private void UpdateHealthBar()
    {
        healthBar.value = currentHealth / maxHealth; // Обновляем значение от 0 до 1
    }
}
