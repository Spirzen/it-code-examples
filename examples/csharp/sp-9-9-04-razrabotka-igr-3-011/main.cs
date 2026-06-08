using UnityEngine;

public class CheckpointManager : MonoBehaviour
{
    private void Start()
    {
        transform.position = new Vector3(
            PlayerPrefs.GetFloat("CheckpointX", 0f),
            PlayerPrefs.GetFloat("CheckpointY", 2f),
            PlayerPrefs.GetFloat("CheckpointZ", 0f)
        );
    }

    private void OnTriggerEnter(Collider other)
    {
        if (!other.CompareTag("Checkpoint")) return;

        PlayerPrefs.SetFloat("CheckpointX", transform.position.x);
        PlayerPrefs.SetFloat("CheckpointY", transform.position.y);
        PlayerPrefs.SetFloat("CheckpointZ", transform.position.z);
        PlayerPrefs.Save();
    }
}
