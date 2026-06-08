using UnityEngine;

public class MoveWASD : MonoBehaviour
{
    [SerializeField] private float moveSpeed = 6f;

    void Update()
    {
        float h = Input.GetAxis("Horizontal");
        float v = Input.GetAxis("Vertical");

        Vector3 move = new Vector3(h, 0f, v);
        if (move.sqrMagnitude > 1f)
            move.Normalize();

        transform.Translate(move * moveSpeed * Time.deltaTime, Space.World);
    }
}
