Ext.define('App.view.user.UserViewModel', {
    extend: 'Ext.app.ViewModel',
    alias: 'viewmodel.user',

    data: {
        record: null // Р±СѓРґРµС‚ Р·Р°РїРѕР»РЅРµРЅРѕ РєРѕРЅС‚СЂРѕР»Р»РµСЂРѕРј
    },

    formulas: {
        fullName: function(get) {
            return (get('record.firstName') || '') + ' ' + 
                   (get('record.lastName') || '');
        }
    }
});
