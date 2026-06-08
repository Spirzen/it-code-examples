
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@Composable
fun CounterScreen() {
    var count by remember { mutableStateOf(0) }

    Column(
        modifier = Modifier.fillMaxSize().padding(24.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        Text("Счётчик: $count", style = MaterialTheme.typography.headlineMedium)
        Button(onClick = { count++ }) {
            Text("Увеличить")
        }
        OutlinedButton(onClick = { count = 0 }) {
            Text("Сбросить")
        }
    }
}
