using System.Collections.Generic;
using UnityEngine;

public class ObjectPool : MonoBehaviour
{
    [SerializeField] private GameObject objectPrefab; // Префаб объекта для пула
    [SerializeField] private int poolSize = 10;      // Начальный размер пула

    private Queue<GameObject> pooledObjects; // Очередь для хранения неактивных объектов

    private void Awake()
    {
        InitializePool();
    }

    private void InitializePool()
    {
        pooledObjects = new Queue<GameObject>();

        for (int i = 0; i < poolSize; i++)
        {
            GameObject obj = Instantiate(objectPrefab);
            obj.SetActive(false);
            pooledObjects.Enqueue(obj);
        }
    }

    public GameObject GetPooledObject()
    {
        if (pooledObjects.Count > 0)
        {
            GameObject obj = pooledObjects.Dequeue();
            obj.SetActive(true);
            return obj;
        }
        else
        {
            // Если пул пуст, можно либо создать новый объект (не рекомендуется), либо расширить пул
            Debug.LogWarning("Object pool is empty!");
            return null;
        }
    }

    public void ReturnToPool(GameObject obj)
    {
        obj.SetActive(false);
        pooledObjects.Enqueue(obj);
    }
}
