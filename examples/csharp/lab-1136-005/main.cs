using UnityEngine;

public class SpawnerOnKey : MonoBehaviour
{
    [SerializeField] private GameObject prefab;
    [SerializeField] private Transform spawnPoint;
    [SerializeField] private KeyCode key = KeyCode.E;

    void Update()
    {
        if (Input.GetKeyDown(key) && prefab != null && spawnPoint != null)
        {
            Instantiate(prefab, spawnPoint.position, spawnPoint.rotation);
        }
    }
}
