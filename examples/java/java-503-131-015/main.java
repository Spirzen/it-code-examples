public class Player {
    private final String name;
    private int health;
    private final int maxHealth;
    private final Item[] inventory;
    private int inventoryCount;
    private Location currentLocation;

    public Player(String name, int maxHealth, int inventorySize) {
        this.name = name;
        this.maxHealth = maxHealth;
        this.health = maxHealth;
        this.inventory = new Item[inventorySize];
    }

    public void setLocation(Location location) {
        this.currentLocation = location;
        System.out.println(name + " переместился в " + location.getName());
    }

    public boolean pickUpItem(int index) {
        if (currentLocation == null || inventoryCount >= inventory.length) return false;
        Item item = currentLocation.removeItem(index);
        if (item == null) return false;
        inventory[inventoryCount++] = item;
        System.out.println(name + " подобрал " + item.getName());
        return true;
    }

    public boolean useItem(int index) {
        if (index < 0 || index >= inventoryCount) return false;
        Item item = inventory[index];
        if ("зелье".equals(item.getType())) {
            health = Math.min(health + item.getValue(), maxHealth);
            System.out.println(name + " восстановил " + item.getValue() + " HP");
        }
        for (int i = index; i < inventoryCount - 1; i++) {
            inventory[i] = inventory[i + 1];
        }
        inventory[--inventoryCount] = null;
        return true;
    }

    public void displayStatus() {
        System.out.println("=== " + name + " | HP: " + health + "/" + maxHealth + " ===");
        System.out.println("Локация: " + (currentLocation != null ? currentLocation.getName() : "— "));
        for (int i = 0; i < inventoryCount; i++) {
            System.out.println("  " + (i + 1) + ". " + inventory[i]);
        }
    }
}
