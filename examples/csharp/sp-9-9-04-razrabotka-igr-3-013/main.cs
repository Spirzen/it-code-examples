using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class GameHud : MonoBehaviour
{
    [SerializeField] private Slider healthBar;
    [SerializeField] private TMP_Text ammoText;
    [SerializeField] private GameObject winPanel;
    [SerializeField] private GameObject losePanel;

    void OnEnable()
    {
        if (GameManager.Instance != null)
            GameManager.Instance.StateChanged += Refresh;
    }

    void OnDisable()
    {
        if (GameManager.Instance != null)
            GameManager.Instance.StateChanged -= Refresh;
    }

    void Start() => Refresh();

    void Refresh()
    {
        var gm = GameManager.Instance;
        if (gm == null) return;

        healthBar.value = gm.Health / 100f;
        ammoText.text = gm.Ammo.ToString();

        winPanel.SetActive(gm.IsGameOver && gm.HasWon);
        losePanel.SetActive(gm.IsGameOver && !gm.HasWon);
    }
}
