@Composable
fun NotesScreen(vm: NotesViewModel = viewModel(
    factory = /* фабрика с dao — см. ниже */
)) {
    val notes by vm.notes.collectAsState()
    var input by remember { mutableStateOf("") }

    Column(Modifier.padding(16.dp)) {
        OutlinedTextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("Заметка") },
            modifier = Modifier.fillMaxWidth()
        )
        Button(
            onClick = {
                vm.addNote(input)
                input = ""
            },
            modifier = Modifier.padding(vertical = 8.dp)
        ) { Text("Добавить") }

        LazyColumn {
            items(notes, key = { it.id }) { note ->
                Text(note.text, modifier = Modifier.padding(8.dp))
            }
        }
    }
}
