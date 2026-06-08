-- ModuleScript: Binder.lua
local CollectionService = game:GetService("CollectionService")

local Binder = {}
Binder.__index = Binder

function Binder.new(tagName: string, constructor: function)
    local self = setmetatable({
        Tag = tagName,
        Constructor = constructor,
        Instances = {},
        Active = false
    }, Binder)
    return self
end

function Binder:Start()
    if self.Active then return end
    self.Active = true

    -- Инициализация существующих
    for _, obj in ipairs(CollectionService:GetTagged(self.Tag)) do
        self:OnInstanceAdded(obj)
    end

    -- Подписка на изменения
    self.ConnAdded = CollectionService.InstanceAdded:Connect(function(tag, obj)
        if tag == self.Tag then self:OnInstanceAdded(obj) end
    end)
    self.ConnRemoved = CollectionService.InstanceRemoved:Connect(function(tag, obj)
        if tag == self.Tag then self:OnInstanceRemoved(obj) end
    end)
end

function Binder:Stop()
    if not self.Active then return end
    self.Active = false
    self.ConnAdded:Disconnect()
    self.ConnRemoved:Disconnect()
    for obj in pairs(self.Instances) do
        self:OnInstanceRemoved(obj)
    end
end

function Binder:OnInstanceAdded(obj)
    if self.Instances[obj] then return end
    local ctrl = self.Constructor(obj)
    self.Instances[obj] = ctrl
end

function Binder:OnInstanceRemoved(obj)
    local ctrl = self.Instances[obj]
    if ctrl then
        if type(ctrl) == "table" and ctrl.Destroy then
            ctrl:Destroy()
        end
        self.Instances[obj] = nil
    end
end

return Binder
