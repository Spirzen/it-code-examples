class NotesViewModel(private val dao: NoteDao) : ViewModel() {

    val notes: StateFlow<List<NoteEntity>> =
        dao.observeAll()
            .stateIn(
                scope = viewModelScope,
                started = SharingStarted.WhileSubscribed(5_000),
                initialValue = emptyList()
            )

    fun addNote(text: String) {
        if (text.isBlank()) return
        viewModelScope.launch {
            dao.insert(NoteEntity(text = text.trim()))
        }
    }
}
