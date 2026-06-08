package com.test;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class BattleGame extends JFrame {
    private Unit player;
    private Unit enemy;
    private Random random = new Random();

    private JLabel playerHealthLabel;
    private JLabel enemyHealthLabel;
    private JLabel playerManaLabel;
    private JLabel enemyManaLabel;
    private JLabel playerExpLabel;
    private JLabel enemyNameLabel;

    private JTextArea battleLog;
    private JPanel abilitiesPanel;

    public BattleGame() {
        setTitle("Битва героев: Фэнтези РПГ");
        setSize(850, 650);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        player = createUnitByClass("Воин", Unit.ClassType.WARRIOR);
        enemy = createUnitByClass("Тёмный Маг", Unit.ClassType.MAGE);

        JPanel statsPanel = new JPanel(new GridLayout(1, 2, 20, 10));
        statsPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        statsPanel.add(createPlayerStatsPanel());
        statsPanel.add(createEnemyStatsPanel());
        add(statsPanel, BorderLayout.NORTH);

        battleLog = new JTextArea();
        battleLog.setEditable(false);
        battleLog.setFont(new Font("Monospaced", Font.PLAIN, 13));
        battleLog.setBackground(new Color(240, 240, 240));
        JScrollPane logScrollPane = new JScrollPane(battleLog);
        logScrollPane.setBorder(BorderFactory.createTitledBorder("Хроники битвы"));
        add(logScrollPane, BorderLayout.CENTER);

        JPanel controlPanel = new JPanel(new BorderLayout(10, 10));
        controlPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        abilitiesPanel = new JPanel();
        abilitiesPanel.setLayout(new FlowLayout(FlowLayout.LEFT));
        updateAbilitiesPanel();
        controlPanel.add(abilitiesPanel, BorderLayout.CENTER);

        JPanel buttonPanel = new JPanel();
        JButton newBattleBtn = new JButton("Новая битва");
        newBattleBtn.addActionListener(e -> startNewBattle());
        buttonPanel.add(newBattleBtn);

        controlPanel.add(buttonPanel, BorderLayout.SOUTH);
        add(controlPanel, BorderLayout.SOUTH);

        logMessage("⚔️ Битва началась! " + player.name + " (" + player.classType.getName() + ") против " + enemy.name);
        logMessage("💡 Совет: Используйте способности для тактического преимущества!");
    }

    private JPanel createPlayerStatsPanel() {
        JPanel panel = new JPanel(new BorderLayout());
        panel.setBorder(BorderFactory.createTitledBorder("Игрок: " + player.name + " (" + player.classType.getName() + ")"));

        JPanel statsGrid = new JPanel(new GridLayout(5, 2, 5, 5));
        statsGrid.add(new JLabel("Уровень:"));
        statsGrid.add(new JLabel(String.valueOf(player.level)));

        statsGrid.add(new JLabel("Здоровье:"));
        playerHealthLabel = new JLabel(player.health + "/" + player.maxHealth);
        statsGrid.add(playerHealthLabel);

        statsGrid.add(new JLabel("Мана:"));
        playerManaLabel = new JLabel(player.mana + "/" + player.maxMana);
        statsGrid.add(playerManaLabel);

        statsGrid.add(new JLabel("Опыт:"));
        playerExpLabel = new JLabel(player.experience + "/" + player.nextLevelExp);
        statsGrid.add(playerExpLabel);

        statsGrid.add(new JLabel("Экипировка:"));
        statsGrid.add(new JLabel(getEquipmentString(player)));

        panel.add(statsGrid, BorderLayout.CENTER);
        return panel;
    }

    private JPanel createEnemyStatsPanel() {
        JPanel panel = new JPanel(new BorderLayout());
        panel.setBorder(BorderFactory.createTitledBorder("Противник"));

        JPanel statsGrid = new JPanel(new GridLayout(4, 2, 5, 5));
        enemyNameLabel = new JLabel(enemy.name + " (" + enemy.classType.getName() + ")");
        statsGrid.add(new JLabel("Имя:"));
        statsGrid.add(enemyNameLabel);

        statsGrid.add(new JLabel("Здоровье:"));
        enemyHealthLabel = new JLabel(enemy.health + "/" + enemy.maxHealth);
        statsGrid.add(enemyHealthLabel);

        statsGrid.add(new JLabel("Мана:"));
        enemyManaLabel = new JLabel(enemy.mana + "/" + enemy.maxMana);
        statsGrid.add(enemyManaLabel);

        statsGrid.add(new JLabel("Экипировка:"));
        statsGrid.add(new JLabel(getEquipmentString(enemy)));

        panel.add(statsGrid, BorderLayout.CENTER);
        return panel;
    }

    private String getEquipmentString(Unit unit) {
        String weapon = unit.weapon != null ? unit.weapon.name : "— ";
        String armor = unit.armor != null ? unit.armor.name : "— ";
        return "Оружие: " + weapon + " | Доспехи: " + armor;
    }

    private void updateAbilitiesPanel() {
        abilitiesPanel.removeAll();

        for (Ability ability : player.abilities) {
            JButton btn = new JButton(ability.name + " (" + ability.manaCost + " MP)");
            btn.setEnabled(player.mana >= ability.manaCost && player.health > 0 && enemy.health > 0);
            final Ability selectedAbility = ability;
            btn.addActionListener(e -> executePlayerTurn(selectedAbility));
            abilitiesPanel.add(btn);
        }

        JButton basicAttackBtn = new JButton("Базовая атака");
        basicAttackBtn.setEnabled(player.health > 0 && enemy.health > 0);
        basicAttackBtn.addActionListener(e -> executePlayerTurn(null));
        abilitiesPanel.add(basicAttackBtn);

        abilitiesPanel.revalidate();
        abilitiesPanel.repaint();
    }

    private void executePlayerTurn(Ability ability) {
        if (player.health <= 0 || enemy.health <= 0) return;

        int damage = ability != null ? calculateAbilityDamage(player, enemy, ability) : calculatePhysicalDamage(player, enemy);
        String actionName = ability != null ? ability.name : "базовая атака";

        if (calculateDodgeChance(enemy)) {
            logMessage(String.format("💨 %s уклонился от %s %s!", enemy.name, actionName, player.name));
        } else {
            if (calculateBlockChance(enemy)) {
                int blocked = (int)(damage * 0.6);
                damage -= blocked;
                logMessage(String.format("🛡️ %s заблокировал %d урона!", enemy.name, blocked));
            }
            enemy.health = Math.max(0, enemy.health - damage);
            logMessage(String.format("💥 %s нанёс %d урона %s (%s)", player.name, damage, enemy.name, actionName));
        }

        if (ability != null) {
            player.mana -= ability.manaCost;
        }

        updateUI();

        if (enemy.health <= 0) {
            enemy.health = 0;
            int expGain = 50 + enemy.level * 25;
            player.gainExperience(expGain);
            logMessage(String.format("🎉 %s победил! Получено %d опыта", player.name, expGain));
            if (player.checkLevelUp()) {
                logMessage(String.format("✨ %s достиг %d уровня! Характеристики улучшены.", player.name, player.level));
            }
            disableControls();
            return;
        }

        Timer timer = new Timer(800, e -> {
            executeEnemyTurn();
            updateUI();
        });
        timer.setRepeats(false);
        timer.start();
    }

    private void executeEnemyTurn() {
        if (player.health <= 0 || enemy.health <= 0) return;

        Ability enemyAbility = null;
        if (enemy.classType == Unit.ClassType.MAGE && enemy.mana >= 20 && random.nextInt(100) < 60) {
            enemyAbility = enemy.abilities.get(0);
        }

        int damage = enemyAbility != null ? calculateAbilityDamage(enemy, player, enemyAbility) : calculatePhysicalDamage(enemy, player);
        String actionName = enemyAbility != null ? enemyAbility.name : "базовая атака";

        if (calculateDodgeChance(player)) {
            logMessage(String.format("💨 %s уклонился от %s %s!", player.name, actionName, enemy.name));
        } else {
            if (calculateBlockChance(player)) {
                int blocked = (int)(damage * 0.6);
                damage -= blocked;
                logMessage(String.format("🛡️ %s заблокировал %d урона!", player.name, blocked));
            }
            player.health = Math.max(0, player.health - damage);
            logMessage(String.format("💥 %s нанёс %d урона %s (%s)", enemy.name, damage, player.name, actionName));
        }

        if (enemyAbility != null) {
            enemy.mana -= enemyAbility.manaCost;
        }

        if (player.health <= 0) {
            player.health = 0;
            logMessage(String.format("☠️ %s пал в бою...", player.name));
            disableControls();
        }
    }

    private int calculatePhysicalDamage(Unit attacker, Unit defender) {
        int baseDamage = attacker.strength;
        if (attacker.weapon != null) baseDamage += attacker.weapon.damageBonus;
        int reduction = defender.armor != null ? defender.armor.damageReduction : 0;
        int finalDamage = (int)(baseDamage * (1 - reduction / 100.0)) + attacker.level;
        return Math.max(1, finalDamage); // Минимум 1 урона
    }

    private int calculateAbilityDamage(Unit caster, Unit target, Ability ability) {
        if (ability.type == Ability.Type.HEAL) {
            return Math.min(ability.power, caster.maxHealth - caster.health);
        }
        return caster.intel * 2 + ability.power + caster.level;
    }

    private boolean calculateDodgeChance(Unit unit) {
        int chance = Math.min(50, unit.agility / 2);
        return random.nextInt(100) < chance;
    }

    private boolean calculateBlockChance(Unit unit) {
        int chance = Math.min(40, (unit.strength + unit.agility) / 4);
        return random.nextInt(100) < chance;
    }

    private void updateUI() {
        playerHealthLabel.setText(player.health + "/" + player.maxHealth);
        enemyHealthLabel.setText(enemy.health + "/" + enemy.maxHealth);
        playerManaLabel.setText(player.mana + "/" + player.maxMana);
        enemyManaLabel.setText(enemy.mana + "/" + enemy.maxMana);
        playerExpLabel.setText(player.experience + "/" + player.nextLevelExp);
        enemyNameLabel.setText(enemy.name + " (" + enemy.classType.getName() + ")");
        updateAbilitiesPanel();
    }

    private void disableControls() {
        for (Component c : abilitiesPanel.getComponents()) {
            if (c instanceof JButton) ((JButton) c).setEnabled(false);
        }
    }

    private void startNewBattle() {
        Unit.ClassType[] classes = Unit.ClassType.values();
        Unit.ClassType playerClass = classes[random.nextInt(classes.length)];
        Unit.ClassType enemyClass = classes[random.nextInt(classes.length)];

        player = createUnitByClass("Герой", playerClass);
        enemy = createUnitByClass("Враг", enemyClass);

        battleLog.setText("");
        logMessage(String.format("⚔️ Новая битва! %s (%s) против %s (%s)",
                player.name, player.classType.getName(),
                enemy.name, enemy.classType.getName()));

        updateUI();
        for (Component c : abilitiesPanel.getComponents()) {
            if (c instanceof JButton) ((JButton) c).setEnabled(true);
        }
    }

    private Unit createUnitByClass(String name, Unit.ClassType type) {
        Unit unit = new Unit(name, type);

        switch (type) {
            case WARRIOR:
                unit.equipWeapon(new Weapon("Стальной меч", 10));
                unit.equipArmor(new Armor("Латы", 20));
                break;
            case MAGE:
                unit.equipWeapon(new Weapon("Волшебный посох", 4));
                unit.equipArmor(new Armor("Магическая роба", 8));
                break;
            case ARCHER:
                unit.equipWeapon(new Weapon("Композитный лук", 8));
                unit.equipArmor(new Armor("Кожаный доспех", 12));
                break;
            case ASSASSIN:
                unit.equipWeapon(new Weapon("Серебряные кинжалы", 7));
                unit.equipArmor(new Armor("Теневая мантия", 10));
                break;
        }

        return unit;
    }

    private void logMessage(String message) {
        battleLog.append(message + "\n");
        battleLog.setCaretPosition(battleLog.getDocument().getLength());
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            BattleGame game = new BattleGame();
            game.setVisible(true);
        });
    }

    // ========== ВНУТРЕННИЕ КЛАССЫ ==========
    static class Unit {
        enum ClassType {
            WARRIOR("Воин"), MAGE("Маг"), ARCHER("Лучник"), ASSASSIN("Ассасин");
            private final String name;
            ClassType(String name) { this.name = name; }
            public String getName() { return name; }
        }

        String name;
        ClassType classType;
        int intel, agility, strength;
        int health, maxHealth;
        int mana, maxMana;
        int level;
        int experience, nextLevelExp;
        Weapon weapon;
        Armor armor;
        List<Ability> abilities = new ArrayList<>();

        public Unit(String name, ClassType classType) {
            this.name = name;
            this.classType = classType;
            this.level = 1;
            this.experience = 0;
            this.nextLevelExp = 100;

            switch (classType) {
                case WARRIOR:
                    this.strength = 28; this.agility = 14; this.intel = 8;
                    this.maxHealth = 130; this.maxMana = 45;
                    this.abilities.add(new Ability("Щитовой удар", Ability.Type.DAMAGE, 18, 20));
                    break;
                case MAGE:
                    this.strength = 7; this.agility = 12; this.intel = 32;
                    this.maxHealth = 85; this.maxMana = 110;
                    this.abilities.add(new Ability("Фаербол", Ability.Type.DAMAGE, 28, 25));
                    this.abilities.add(new Ability("Исцеление", Ability.Type.HEAL, 25, 35));
                    break;
                case ARCHER:
                    this.strength = 14; this.agility = 30; this.intel = 11;
                    this.maxHealth = 100; this.maxMana = 65;
                    this.abilities.add(new Ability("Прицельный выстрел", Ability.Type.DAMAGE, 24, 22));
                    break;
                case ASSASSIN:
                    this.strength = 20; this.agility = 35; this.intel = 13;
                    this.maxHealth = 95; this.maxMana = 55;
                    this.abilities.add(new Ability("Рывок из тени", Ability.Type.DAMAGE, 26, 28));
                    break;
            }

            this.health = maxHealth;
            this.mana = maxMana;
        }

        public void equipWeapon(Weapon weapon) { this.weapon = weapon; }
        public void equipArmor(Armor armor) { this.armor = armor; }

        public void gainExperience(int amount) { this.experience += amount; }

        public boolean checkLevelUp() {
            if (this.experience < this.nextLevelExp) return false;

            this.level++;
            this.strength += 2 + (classType == ClassType.WARRIOR ? 2 : 0);
            this.agility += 2 + (classType == ClassType.ASSASSIN || classType == ClassType.ARCHER ? 2 : 0);
            this.intel += 2 + (classType == ClassType.MAGE ? 3 : 0);
            this.maxHealth += 18;
            this.maxMana += 12;
            this.health = this.maxHealth;
            this.mana = this.maxMana;
            this.experience -= this.nextLevelExp;
            this.nextLevelExp = (int)(this.nextLevelExp * 1.6);

            return true;
        }
    }

    static class Weapon {
        String name; int damageBonus;
        Weapon(String name, int damageBonus) { this.name = name; this.damageBonus = damageBonus; }
    }

    static class Armor {
        String name; int damageReduction;
        Armor(String name, int damageReduction) { this.name = name; this.damageReduction = damageReduction; }
    }

    static class Ability {
        enum Type { DAMAGE, HEAL }
        String name; Type type; int power; int manaCost;
        Ability(String name, Type type, int power, int manaCost) {
            this.name = name; this.type = type; this.power = power; this.manaCost = manaCost;
        }
    }
}
