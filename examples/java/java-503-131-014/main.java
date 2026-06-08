public class Location {
    private final String name;
    private final String description;
    private final Item[] items;
    private int itemCount;

    public Location(String name, String description, int maxItems) {
        this.name = name;
        this.description = description;
        this.items = new Item[maxItems];
    }

    public String getName() { return name; }

    public boolean addItem(Item item) {
        if (itemCount >= items.length) return false;
        items[itemCount++] = item;
        return true;
    }

    public Item removeItem(int index) {
        if (index < 0 || index >= itemCount) return null;
        Item removed = items[index];
        for (int i = index; i < itemCount - 1; i++) {
            items[i] = items[i + 1];
        }
        items[--itemCount] = null;
        return removed;
    }

    public int getItemCount() { return itemCount; }

    public void displayInfo() {
        System.out.println("=== " + name + " ===");
        System.out.println(description);
        for (int i = 0; i < itemCount; i++) {
            System.out.println((i + 1) + ". " + items[i]);
        }
    }
}
