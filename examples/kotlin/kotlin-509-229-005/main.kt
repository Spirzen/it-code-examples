
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue

@Composable
fun CounterScreen(vm: CounterViewModel = viewModel()) {
    val uiState by vm.state.collectAsState()

    Column(Modifier.padding(24.dp)) {
        Text("Счётчик: ${uiState.count}")
        Button(onClick = vm::increment) { Text("+1") }
        OutlinedButton(onClick = vm::reset) { Text("Сброс") }
    }
}
