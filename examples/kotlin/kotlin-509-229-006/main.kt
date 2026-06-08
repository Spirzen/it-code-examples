
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.launch

class NotesViewModel(private val api: NotesApi) : ViewModel() {
    private val _state = MutableStateFlow<List<Note>>(emptyList())
    val state = _state.asStateFlow()

    init {
        viewModelScope.launch {
            _state.value = api.fetchNotes()
        }
    }
}
