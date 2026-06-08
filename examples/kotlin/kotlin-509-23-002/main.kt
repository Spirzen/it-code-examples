private val Context.petDataStore by preferencesDataStore(name = "pet_state")

class PetRepository(private val context: Context) {

    val petState: Flow<PetState> = context.petDataStore.data.map { prefs ->
        PetState(
            name = prefs[KEY_NAME] ?: PetState.DEFAULT_NAME,
            health = prefs[KEY_HEALTH] ?: 80,
            energy = prefs[KEY_ENERGY] ?: 80,
            cleanliness = prefs[KEY_CLEANLINESS] ?: 80,
            lastUpdatedMillis = prefs[KEY_LAST_UPDATED] ?: System.currentTimeMillis(),
        )
    }

    suspend fun save(state: PetState) {
        context.petDataStore.edit { prefs ->
            prefs[KEY_NAME] = state.name
            prefs[KEY_HEALTH] = state.health
            prefs[KEY_ENERGY] = state.energy
            prefs[KEY_CLEANLINESS] = state.cleanliness
            prefs[KEY_LAST_UPDATED] = state.lastUpdatedMillis
        }
    }
}
