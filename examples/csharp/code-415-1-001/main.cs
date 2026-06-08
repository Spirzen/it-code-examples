// C# (Unity-подобный код)
void OnCollision(Enemy enemy)
{
    // ... эффект взрыва
    enemy.TakeDamage(damage);
    // Забыли: this.gameObject.SetActive(false) или Destroy(this)
}
