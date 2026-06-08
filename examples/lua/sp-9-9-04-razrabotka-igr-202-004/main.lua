-- Описание всех предметов в магазине.
-- Не содержит состояния игрока — только "что можно купить и за сколько".

return {
    Coins_1000 = {
        Id = "Coins_1000",
        DisplayName = "1000 монет",
        Description = "Пополните запасы внутриигровой валюты",
        Price = { RobuxProduct = "prod_coins_1k" }, -- имя, не ID!
        Type = "CurrencyPack",
        Metadata = { Amount = 1000 }
    },

    Sword_Fire = {
        Id = "Sword_Fire",
        DisplayName = "Огненный меч",
        Description = "Наносит +5 урона и поджигает врагов",
        Price = { Coins = 500 },
        Type = "Tool",
        Metadata = {
            ToolAssetId = 123456789, -- rbxassetid ссылка на Tool в Toolbox или Inventory
            DamageBonus = 5,
            HasFireEffect = true
        }
    },

    Skin_RedArmor = {
        Id = "Skin_RedArmor",
        DisplayName = "Красные доспехи",
        Description = "Эксклюзивный внешний вид",
        Price = { Coins = 1200 },
        Type = "Appearance",
        Metadata = {
            ShirtTemplate = "rbxassetid://987000001",
            PantsTemplate = "rbxassetid://987000002"
        }
    }
}
