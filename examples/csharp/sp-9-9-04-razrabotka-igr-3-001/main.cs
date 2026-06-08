    using UnityEngine;

    public class PlayerController : MonoBehaviour
    {
        [SerializeField] private GameObject applePrefab;
        [SerializeField] private float speed = 5f;

        void Update()
        {
            float h = Input.GetAxis("Horizontal");
            float v = Input.GetAxis("Vertical");
            Vector3 move = new Vector3(h, 0f, v) * speed * Time.deltaTime;
            transform.Translate(move, Space.World);

            if (Input.GetKeyDown(KeyCode.Space) && applePrefab != null)
            {
                Instantiate(applePrefab, transform.position, Quaternion.identity);
            }
        }
    }
