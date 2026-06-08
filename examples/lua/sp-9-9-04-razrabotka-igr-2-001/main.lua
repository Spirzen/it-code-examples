print("[Init] Server starting...")

game.Workspace.Loaded:Wait()
print("[Init] Workspace.Loaded = true")

game.Players.PlayerAdded:Connect(function(player)
	print("[Event] PlayerAdded:", player.Name)
	print("  → Character =", player.Character)
	print("  → PlayerGui =", player.PlayerGui and "exists" or "nil")

	player.CharacterAdded:Connect(function(char)
		print("[Event] CharacterAdded for", player.Name)
		print("  → Humanoid =", char:FindFirstChild("Humanoid") and "exists" or "nil")
		print("  → HRP =", char:FindFirstChild("HumanoidRootPart") and "exists" or "nil")
	end)

	task.delay(0.2, function()
		if player and player.Parent then
			print("[Check 0.2s] Char =", player.Character ~= nil)
		end
	end)
	task.delay(1, function()
		if player and player.Parent then
			local char = player.Character
			if char then
				print("[Check 1s] HRP =", char:FindFirstChild("HumanoidRootPart") ~= nil)
				local hum = char:FindFirstChild("Humanoid")
				print("[Check 1s] Humanoid.Health =", hum and hum.Health or "nil")
			end
		end
	end)
end)
