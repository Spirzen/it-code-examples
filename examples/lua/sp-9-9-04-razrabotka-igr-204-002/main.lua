local function deepCopy(t: { [string]: any }): { [string]: any }
    local copy = {}
    for k, v in pairs(t) do
        copy[k] = if type(v) == "table" then deepCopy(v) else v
    end
    return copy
end

function DataModule.set(player: Player, stat: "Coins" | "Stage" | "Wins", value: number)
    local data = session[player]
    if not data then return end
    data[stat] = value
    local ls = player:FindFirstChild("leaderstats")
    local iv = ls and ls:FindFirstChild(stat) :: IntValue?
    if iv then iv.Value = value end
end
