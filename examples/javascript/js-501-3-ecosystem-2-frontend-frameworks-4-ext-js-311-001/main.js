Ext.define('MyApp.view.CustomButton', {
    extend: 'Ext.button.Button',
    xtype: 'custombutton',

    config: {
        customColor: '#000'
    },

    applyCustomColor: function(color) {
        this.el.setStyle('color', color);
        return color;
    },

    initialize: function() {
        this.callParent();
        // Дополнительная инициализация
    }
});
