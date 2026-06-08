struct Config {
    var theme: String
}

class AppState {
    var isOnline = false
}

var cfgA = Config(theme: "light")
var cfgB = cfgA
cfgB.theme = "dark"        // cfgA.theme всё ещё "light"

let state = AppState()
let copy = state
copy.isOnline = true       // state.isOnline тоже true
