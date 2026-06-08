using UnityEngine;

public class MyFirstScript : MonoBehaviour
{
    [SerializeField] private float speed = 5f;

    void Awake()
    {
        Debug.Log("Awake: объект создан");
    }

    void Start()
    {
        Debug.Log("Start: сцена пошла");
    }

    void Update()
    {
        // Каждый кадр — ввод, таймеры, transform.Translate
        // Rigidbody — в FixedUpdate
    }
}
