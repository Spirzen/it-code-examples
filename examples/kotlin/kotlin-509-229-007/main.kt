
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController

@Composable
fun AppNav() {
    val nav = rememberNavController()
    NavHost(navController = nav, startDestination = "home") {
        composable("home") {
            CounterScreen(onOpenDetails = { nav.navigate("details") })
        }
        composable("details") {
            DetailsScreen(onBack = { nav.popBackStack() })
        }
    }
}
