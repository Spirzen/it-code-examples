using System;
using UnityEngine;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }

    [SerializeField] private float maxHealth = 100f;
    [SerializeField] private int maxAmmo = 20;
    [SerializeField] private int itemsToWin = 5;

    public float Health { get; private set; }
    public int Ammo { get; private set; }
    public int ItemsCollected { get; private set; }
    public bool IsGameOver { get; private set; }
    public bool HasWon { get; private set; }

    public event Action StateChanged;

    void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        Instance = this;
    }

    void Start()
    {
        Health = maxHealth;
        Ammo = maxAmmo;
        Notify();
    }

    public void TakeDamage(float amount)
    {
        if (IsGameOver) return;
        Health = Mathf.Max(0f, Health - amount);
        if (Health <= 0f)
        {
            IsGameOver = true;
            HasWon = false;
        }
        Notify();
    }

    public bool TryConsumeAmmo()
    {
        if (Ammo <= 0) return false;
        Ammo--;
        Notify();
        return true;
    }

    public void CollectItem(int value = 1)
    {
        ItemsCollected += value;
        Health = Mathf.Min(maxHealth, Health + 10f);
        if (ItemsCollected >= itemsToWin)
        {
            IsGameOver = true;
            HasWon = true;
        }
        Notify();
    }

    void Notify() => StateChanged?.Invoke();
}
