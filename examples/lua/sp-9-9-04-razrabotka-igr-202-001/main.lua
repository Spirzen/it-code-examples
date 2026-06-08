-- ReplicatedStorage/Catalog/Items.lua
return {
    Sword_001 = {
        Id = "Sword_001",
        DisplayName = "Огненный клинок",
        Description = "Меч, оставляющий след из пламени",
        Price = { Coins = 500 },
        Type = "Tool",
        Unlockable = true,
        Metadata = {
            Damage = 25,
            FireEffect = true
        }
    },
    Skin_Warrior_Red = {
        Id = "Skin_Warrior_Red",
        DisplayName = "Красный воин",
        Description = "Эксклюзивный скин для класса Воин",
        Price = { RobuxProduct = "prod_123abc" }, -- ссылка на Developer Product ID
        Type = "Appearance",
        Metadata = {
            MeshId = "rbxassetid://123456789",
            TextureId = "rbxassetid://987654321"
        }
    }
}
