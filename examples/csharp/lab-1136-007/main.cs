using UnityEngine;
using UnityEngine.UI;

public class GameUI : MonoBehaviour
{
    [SerializeField] private Text scoreLabel;
    [SerializeField] private Button restartButton;

    void OnEnable()
    {
        if (restartButton != null)
            restartButton.onClick.AddListener(OnRestartClicked);
    }

    void OnDisable()
    {
        if (restartButton != null)
            restartButton.onClick.RemoveListener(OnRestartClicked);
    }

    void Update()
    {
        if (scoreLabel != null && ScoreManager.Instance != null)
            scoreLabel.text = $"Монеты: {ScoreManager.Instance.Score}";
    }

    void OnRestartClicked()
    {
        Debug.Log("Restart — подключите LevelRestart.ReloadCurrentScene");
    }
}
