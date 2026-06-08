public class PlayerMovement : NetworkBehaviour
{
    [ServerRpc]
    void InputServerRpc(Vector2 input, ServerRpcParams rpcParams = default)
    {
        // Валидация скорости, позиции
        velocity.Value = input * speed;
    }

    public override void OnNetworkSpawn()
    {
        if (IsLocalPlayer)
            Camera.main.GetComponent<CameraFollow>().target = transform;
    }
}
