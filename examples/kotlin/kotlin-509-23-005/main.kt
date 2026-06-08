@Composable
fun TamagotchiScreen(viewModel: PetViewModel = viewModel()) {
    val pet by viewModel.petState.collectAsState()
    val feedback by viewModel.feedback.collectAsState()
    val snackbarHostState = remember { SnackbarHostState() }

    LaunchedEffect(feedback) {
        feedback?.let {
            snackbarHostState.showSnackbar("${it.emoji}  ${it.message}")
            viewModel.clearFeedback()
        }
    }

    Scaffold(
        containerColor = CreamBackground,
        snackbarHost = { SnackbarHost(snackbarHostState) { data -> Snackbar(…) { Text(data.visuals.message) } } },
    ) { padding ->
        Column(Modifier.padding(padding).verticalScroll(rememberScrollState())) {
            PetDisplay(name = pet.name, mood = pet.mood)
            // Card + StatBar × 3
            Row {
                ActionButton(PetAction.Feed, MintGreen, enabled = pet.energy < 95) {
                    viewModel.onAction(PetAction.Feed)
                }
                // Play, Wash — см. эталон
            }
        }
    }
}
