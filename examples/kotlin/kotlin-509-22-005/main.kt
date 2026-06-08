import androidx.compose.ui.res.stringResource
import androidx.compose.ui.tooling.preview.Preview

Text(
    text = stringResource(R.string.greeting),
    style = MaterialTheme.typography.headlineMedium,
    textAlign = TextAlign.Center,
)
Button(onClick = { count++ }) {
    Text(text = stringResource(R.string.increment))
}

@Preview(showBackground = true)
@Composable
private fun CounterScreenPreview() {
    KotlinMobileAppTheme {
        CounterScreen()
    }
}
