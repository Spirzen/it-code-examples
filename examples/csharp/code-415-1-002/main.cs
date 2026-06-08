public class ProjectileSpawner : MonoBehaviour
{
    public List<Projectile> activeProjectiles = new List<Projectile>(); // ← статический или долгоживущий контейнер

    void Spawn()
    {
        var p = new Projectile();
        activeProjectiles.Add(p); // добавили
        // ...
    }
}

// В момент столкновения:
void OnCollision()
{
    // this.Destroy(); — не вызвано
    // и не удалено из activeProjectiles!
}
