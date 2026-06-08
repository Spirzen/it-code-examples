using UnityEngine;

public class ColorChanger : MonoBehaviour
{
    [SerializeField] private Color[] palette =
    {
        Color.red, Color.green, Color.blue, Color.yellow
    };

    private Renderer rend;
    private int index;

    void Awake()
    {
        rend = GetComponent<Renderer>();
    }

    void Update()
    {
        if (!Input.GetKeyDown(KeyCode.C)) return;

        index = (index + 1) % palette.Length;
        rend.material.color = palette[index];
    }
}
