-- Шаблон: интерактивный объект с реакцией на касание
-- Размещается внутри объекта (script.Parent = объект)

local TweenService = game:GetService("TweenService")

local object = script.Parent  -- ← основное правило: привязка к родителю
local enabled = true          -- флаг для безопасного отключения логики

-- 1. Проверка: объект существует и поддерживает события
if not object:IsA("BasePart") and not object:IsA("Model") then
	warn("[Script] Ошибка: скрипт должен быть внутри Part/Model")
	return
end

-- 2. Вспомогательная функция (объявляем до onTouched)
local function activateEffect(target)
	if target:IsA("BasePart") then
		TweenService:Create(target, TweenInfo.new(0.2), { Transparency = 0.5 }):Play()
		task.delay(0.2, function()
			if enabled and target.Parent then
				TweenService:Create(target, TweenInfo.new(0.2), { Transparency = 0 }):Play()
			end
		end)
	elseif target:IsA("Model") then
		target:ScaleTo(1.2, 0.2)
		task.delay(0.2, function()
			if enabled and target.Parent then
				target:ScaleTo(1, 0.2)
			end
		end)
	end
end

-- 3. Обработчик события
local function onTouched(hit)
	if not enabled then return end

	-- Проверка: коснулся ли персонаж (Humanoid обычно в Model-родителе части)
	local character = hit.Parent
	if not character or not character:IsA("Model") then return end

	local humanoid = character:FindFirstChildOfClass("Humanoid")
	if not humanoid or humanoid.Health <= 0 then return end

	-- Проверка: это не наш собственный объект (защита от self-touch)
	if hit:IsDescendantOf(object) then return end

	-- ✅ Здесь — ваша логика
	print("Объект", object.Name, "активирован игроком", character.Name)

	if object:IsA("BasePart") then
		object.Color = Color3.fromRGB(math.random(255), math.random(255), math.random(255))
	end

	activateEffect(object)
end

-- 4. Подключение события (Touched есть у BasePart; для Model — у дочерней части)
local touchTarget = object:IsA("BasePart") and object or object:FindFirstChildWhichIsA("BasePart", true)
if not touchTarget then
	warn("[Script] Нет BasePart для события Touched")
	return
end

local connection = touchTarget.Touched:Connect(onTouched)

-- 5. Очистка при уничтожении объекта
script.Destroying:Connect(function()
	enabled = false
	if connection and connection.Connected then
		connection:Disconnect()
	end
end)
