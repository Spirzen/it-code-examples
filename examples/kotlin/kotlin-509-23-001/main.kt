package com.kotlinochi.tamagotchi.model

data class PetState(
    val name: String = DEFAULT_NAME,
    val health: Int = 80,
    val energy: Int = 80,
    val cleanliness: Int = 80,
    val lastUpdatedMillis: Long = System.currentTimeMillis(),
) {
    val mood: PetMood get() = PetMood.fromStats(health, energy, cleanliness)

    fun clamped(): PetState = copy(
        health = health.coerceIn(0, MAX_STAT),
        energy = energy.coerceIn(0, MAX_STAT),
        cleanliness = cleanliness.coerceIn(0, MAX_STAT),
    )

    companion object {
        const val DEFAULT_NAME = "Коточи"
        const val MAX_STAT = 100
    }
}
