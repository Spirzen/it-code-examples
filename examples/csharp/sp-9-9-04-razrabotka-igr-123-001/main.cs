using System.Collections.Generic;
using UnityEngine;

public class BulletPool : MonoBehaviour
{
    [SerializeField] private GameObject bulletPrefab;
    [SerializeField] private int prewarmCount = 32;

    private readonly Queue<GameObject> _pool = new();

    void Awake()
    {
        for (int i = 0; i < prewarmCount; i++)
        {
            var go = Instantiate(bulletPrefab, transform);
            go.SetActive(false);
            _pool.Enqueue(go);
        }
    }

    public GameObject Get(Vector3 position, Quaternion rotation)
    {
        GameObject go = _pool.Count > 0 ? _pool.Dequeue() : Instantiate(bulletPrefab, transform);
        go.transform.SetPositionAndRotation(position, rotation);
        go.SetActive(true);
        return go;
    }

    public void Release(GameObject go)
    {
        go.SetActive(false);
        _pool.Enqueue(go);
    }
}
