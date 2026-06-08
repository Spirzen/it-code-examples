startButton.setOnAction(e -> {
    startButton.setDisable(true);
    resetButton.setDisable(true);
    manualSlider.setDisable(true);
    status.setText("Идёт имитация загрузки…");

    Timeline timeline = new Timeline(
            new KeyFrame(Duration.ZERO, ev -> manualSlider.setValue(0)),
            new KeyFrame(Duration.seconds(2.5),
                    new KeyValue(manualSlider.valueProperty(), 1))
    );
    timeline.setOnFinished(ev -> {
        startButton.setDisable(false);
        resetButton.setDisable(false);
        manualSlider.setDisable(false);
        status.setText("Загрузка завершена");
    });
    timeline.play();
});
