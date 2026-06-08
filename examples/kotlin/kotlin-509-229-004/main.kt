
import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update

data class CounterUiState(val count: Int = 0)

class CounterViewModel : ViewModel() {
    private val _state = MutableStateFlow(CounterUiState())
    val state: StateFlow<CounterUiState> = _state.asStateFlow()

    fun increment() = _state.update { it.copy(count = it.count + 1) }
    fun reset() = _state.update { CounterUiState() }
}
