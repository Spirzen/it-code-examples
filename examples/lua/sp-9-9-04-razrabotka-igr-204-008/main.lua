local BadgeService = game:GetService("BadgeService")

local function hookBadgePart(part: BasePart)
    local badgeIdVal = part:FindFirstChild("BadgeId") :: IntValue?
    if not badgeIdVal then return end
    local badgeId = badgeIdVal.Value
    part.Touched:Connect(function(hit)
        local player = playerFromHit(hit)
        if not player then return end
        local uid = player.UserId
        local ok, has = pcall(function()
            return BadgeService:UserHasBadgeAsync(uid, badgeId)
        end)
        if ok and not has then
            pcall(function()
                BadgeService:AwardBadge(uid, badgeId)
            end)
        end
    end)
end
