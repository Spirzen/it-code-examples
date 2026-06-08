using UnityEngine;

public class SmoothMovement : MonoBehaviour
{
    [SerializeField] private float targetHeight = 1f; // Конечная высота
    [SerializeField] private float duration = 1f;     // Время перехода

    private Vector3 startPosition;
    private float elapsedTime = 0f;

    void Start()
    {
        startPosition = transform.position;
    }

    void Update()
    {
        if (elapsedTime < duration)
        {
            elapsedTime += Time.deltaTime;
            float t = elapsedTime / duration; // Прогресс от 0 до 1
            float currentY = Mathf.Lerp(startPosition.y, targetHeight, t);
            transform.position = new Vector3(transform.position.x, currentY, transform.position.z);
        }
    }
}
