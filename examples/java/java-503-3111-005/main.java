Label statusLabel = new Label("Готово — выберите вкладку и поиграйте с элементами");
statusLabel.getStyleClass().add("status-bar");
statusLabel.setMaxWidth(Double.MAX_VALUE);

TabPane tabs = new TabPane(
        formTab(statusLabel),
        listTab(statusLabel),
        progressTab(statusLabel)
);
tabs.setTabClosingPolicy(TabPane.TabClosingPolicy.UNAVAILABLE);

VBox header = new VBox(4,
        styledLabel("JavaFX Demo", "header-title"),
        styledLabel("Наглядные контролы, привязки и простая анимация", "header-subtitle")
);
header.setPadding(new Insets(20, 20, 8, 20));

BorderPane root = new BorderPane();
root.setTop(header);
root.setCenter(tabs);
root.setBottom(statusLabel);
BorderPane.setMargin(tabs, new Insets(0, 16, 12, 16));
