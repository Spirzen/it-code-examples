// Запуск действия
app.doAction("MyAction", "MySet");

// Получить список
var sets = app.actionSets;
for (var i = 0; i < sets.length; i++) {
    $.writeln(sets[i].name);
}

// Запись действия (начало/стоп)
app.beginModalState(); // блокирует UI
app.playbackParameters = new ActionDescriptor();
app.playbackParameters.putBoolean(stringIDToTypeID("useOverride"), true);
app.endModalState();
