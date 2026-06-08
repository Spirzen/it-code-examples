using UnityEngine;

public class CoinPickup : MonoBehaviour
{
    [SerializeField] private int value = 10;
    [SerializeField] private GameManager gameManager;
    [SerializeField] private AudioSource pickupSound;

    private void OnTriggerEnter(Collider other)
    {
        if (!other.CompareTag("Player")) return;

        gameManager?.CollectItem(value);
        pickupSound?.Play();
        gameObject.SetActive(false);
    }
}
