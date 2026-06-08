public class Game {
    public static void main(String[] args) {
        Item sword = new Item("Меч", "оружие", 15);
        Item potion = new Item("Зелье здоровья", "зелье", 30);

        Location forest = new Location("Тёмный лес", "Густой лес с высокими деревьями.", 5);
        forest.addItem(sword);
        forest.addItem(potion);

        Player hero = new Player("Герой", 100, 10);
        hero.setLocation(forest);
        forest.displayInfo();

        hero.pickUpItem(0);
        hero.pickUpItem(0);
        hero.useItem(0);
        hero.displayStatus();
    }
}
