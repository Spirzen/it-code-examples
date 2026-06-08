import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue

@Composable
fun CounterScreen() {
    var count by rememberSaveable { mutableIntStateOf(0) }

    // … внутри Column:
    Text(
        text = count.toString(),
        style = MaterialTheme.typography.displayLarge,
    )
    Button(onClick = { count++ }) {
        Text("Увеличить")
    }
}
