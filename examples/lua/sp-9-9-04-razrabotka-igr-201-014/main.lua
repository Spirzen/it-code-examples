-- Server
local BadgeService = game:GetService("BadgeService")
local Players = game:GetService("Players")

local BADGE_ID = 87654321

-- Проверка, есть ли уже
local success, hasBadge = pcall(function()
    return BadgeService:UserHasBadgeAsync(player.UserId, BADGE_ID)
end)

if success and not hasBadge then
    local awarded = BadgeService:AwardBadge(player.UserId, BADGE_ID)
    if awarded then
        -- Показать уведомление
    end
end
