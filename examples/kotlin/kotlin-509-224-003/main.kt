import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@Composable
fun NameCard() {
    var name by remember { mutableStateOf("") }
    var savedName by remember { mutableStateOf<String?>(null) }

    Column(Modifier.padding(16.dp)) {
        OutlinedTextField(
            value = name,
            onValueChange = { name = it },
            modifier = Modifier.fillMaxWidth(),
            label = { Text("Введите имя") }
        )
        Button(onClick = { savedName = name.trim() }) {
            Text("Сохранить")
        }
        if (!savedName.isNullOrBlank()) {
            Text("Привет, $savedName")
        }
    }
}
