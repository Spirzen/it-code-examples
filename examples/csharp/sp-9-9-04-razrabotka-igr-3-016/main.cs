using UnityEngine;

public class GameOverManager : MonoBehaviour
{
    [SerializeField] private GameObject loseScreen;
    [SerializeField] private MonoBehaviour playerController; // например PlayerController

    public void ShowGameOver()
    {
        if (playerController != null)
            playerController.enabled = false;
        loseScreen.SetActive(true);
    }

    public void HideGameOver()
    {
        loseScreen.SetActive(false);
        if (playerController != null)
            playerController.enabled = true;
    }
}
