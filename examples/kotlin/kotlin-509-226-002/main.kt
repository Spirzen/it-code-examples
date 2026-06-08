val queryFlow: Flow<String> = textChanges()

val resultsFlow: Flow<List<Item>> =
    queryFlow
        .map { it.trim() }
        .debounce(300)
        .distinctUntilChanged()
        .flatMapLatest { query ->
            if (query.isBlank()) {
                flowOf(emptyList())
            } else {
                repository.search(query)
            }
        }
