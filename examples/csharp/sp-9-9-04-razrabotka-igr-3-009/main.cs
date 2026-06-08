using UnityEngine;

public class PlayerInteraction : MonoBehaviour
{
    [SerializeField] private Transform cameraTransform;
    [SerializeField] private float maxDistance = 5f;
    [SerializeField] private LayerMask interactableLayers;
    [SerializeField] private float dragDistance = 2f;

    private DraggableObject currentlyDraggedObject;

    void Update()
    {
        if (!Input.GetMouseButtonDown(0)) return;

        if (currentlyDraggedObject != null)
        {
            currentlyDraggedObject.StopFollow();
            currentlyDraggedObject = null;
            return;
        }

        Ray ray = new Ray(cameraTransform.position, cameraTransform.forward);
        if (!Physics.Raycast(ray, out RaycastHit hit, maxDistance, interactableLayers))
            return;

        if (!hit.collider.CompareTag("DraggableObject")) return;
        if (!hit.collider.TryGetComponent(out DraggableObject draggable)) return;

        Vector3 holdPoint = cameraTransform.position + cameraTransform.forward * dragDistance;
        draggable.Follow(holdPoint);
        currentlyDraggedObject = draggable;
    }

    void LateUpdate()
    {
        if (currentlyDraggedObject == null) return;
        Vector3 holdPoint = cameraTransform.position + cameraTransform.forward * dragDistance;
        currentlyDraggedObject.Follow(holdPoint);
    }
}
