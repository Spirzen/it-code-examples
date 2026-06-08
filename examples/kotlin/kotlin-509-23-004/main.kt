fun onAction(action: PetAction) {
    val current = _petState.value
    val updated = when (action) {
        PetAction.Feed -> current.copy(
            energy = current.energy + 25,
            health = current.health + 8,
        )
        PetAction.Play -> current.copy(
            energy = current.energy - 18,
            health = current.health + 12,
            cleanliness = current.cleanliness - 8,
        )
        PetAction.Wash -> current.copy(
            cleanliness = current.cleanliness + 35,
            energy = current.energy - 5,
        )
    }.clamped().copy(lastUpdatedMillis = System.currentTimeMillis())

    _petState.value = updated
    _feedback.value = actionFeedback(action)
    persist(updated)
}
