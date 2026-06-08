#target photoshop
var doc = app.activeDocument;
for (var i = 0; i < doc.layers.length; i++) {
    var layer = doc.layers[i];
    if (layer.visible) {
        layer.visible = false;
        doc.activeLayer = layer;
        layer.visible = true;
        var file = new File("~/exports/" + layer.name + ".png");
        var opts = new PNGSaveOptions();
        opts.compression = 9;
        doc.saveAs(file, opts, true, Extension.LOWERCASE);
        layer.visible = false;
    }
}
