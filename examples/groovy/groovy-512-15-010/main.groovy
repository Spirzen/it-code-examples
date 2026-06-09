class Smartphone {
    private String model
    private int battery

    Smartphone(String model) {
        this.model = model
        this.battery = 20
    }

    void call() {
        battery = Math.max(0, battery - 5)
        println "Звонок с ${model}... Заряд: ${battery}%"
    }

    void charge() {
        battery = Math.min(100, battery + 30)
        println "Зарядка ${model}... Заряд: ${battery}%"
    }

    void showStatus() {
        println "Смартфон ${model}: заряд ${battery}%"
    }
}

def phone = new Smartphone('Pixel')
phone.showStatus()
phone.call()
phone.charge()
phone.showStatus()
