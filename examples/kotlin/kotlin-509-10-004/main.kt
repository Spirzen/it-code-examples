class MainView : SimplePanel() {
    init {
        add(
            VPanel {
                h1 { +"Добро пожаловать в KVision!" }
                button("Нажми меня") {
                    onClickFunction = {
                        alert("Привет из Kotlin!")
                    }
                }
            }
        )
    }
}
