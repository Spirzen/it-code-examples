class PetViewModel(application: Application) : AndroidViewModel(application) {

    private val repository = PetRepository(application)
    private val _petState = MutableStateFlow(PetState())
    val petState: StateFlow<PetState> = _petState.asStateFlow()

    private val _feedback = MutableStateFlow<ActionFeedback?>(null)
    val feedback: StateFlow<ActionFeedback?> = _feedback.asStateFlow()

    init {
        viewModelScope.launch {
            val saved = repository.petState.first()
            val withOffline = applyOfflineDecay(saved)
            _petState.value = withOffline
            repository.save(withOffline)
            startDecayLoop()
        }
    }
}
