local playerData = {
    Level = 1,
    XP = 0,
    XPToNextLevel = 100
}

function addXP(amount)
    playerData.XP = playerData.XP + amount
    while playerData.XP >= playerData.XPToNextLevel do
        playerData.XP = playerData.XP - playerData.XPToNextLevel
        playerData.Level = playerData.Level + 1
        playerData.XPToNextLevel = math.floor(playerData.XPToNextLevel * 1.5)
        print("Уровень повышен до: " .. playerData.Level)
    end
end
