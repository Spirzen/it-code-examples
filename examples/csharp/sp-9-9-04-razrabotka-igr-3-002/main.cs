using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerControllerInputSystem : MonoBehaviour
{
    [SerializeField] private GameObject applePrefab;
    [SerializeField] private float speed = 5f;

    private InputAction jumpAction;

    void Awake()
    {
        jumpAction = new InputAction(type: InputActionType.Button, binding: "<Keyboard>/space");
        jumpAction.Enable();
    }

    void OnDestroy() => jumpAction?.Dispose();

    void Update()
    {
        var kb = Keyboard.current;
        if (kb != null)
        {
            float h = (kb.dKey.isPressed ? 1f : 0f) - (kb.aKey.isPressed ? 1f : 0f);
            float v = (kb.wKey.isPressed ? 1f : 0f) - (kb.sKey.isPressed ? 1f : 0f);
            transform.Translate(new Vector3(h, 0f, v) * speed * Time.deltaTime);
        }

        if (jumpAction.WasPressedThisFrame() && applePrefab != null)
            Instantiate(applePrefab, transform.position, Quaternion.identity);
    }
}
