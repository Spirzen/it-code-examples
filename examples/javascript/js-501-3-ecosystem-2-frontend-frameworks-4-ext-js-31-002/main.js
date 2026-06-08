Ext.define('App.view.user.EditForm', {
    extend: 'Ext.form.Panel',
    xtype: 'user-edit-form',
    
    viewModel: {
        type: 'user' // СЃСЃС‹Р»РєР° РЅР° App.view.user.UserViewModel
    },

    items: [{
        xtype: 'textfield',
        fieldLabel: 'РРјСЏ',
        bind: '{record.firstName}'
    }, {
        xtype: 'textfield',
        fieldLabel: 'Р¤Р°РјРёР»РёСЏ',
        bind: '{record.lastName}'
    }, {
        xtype: 'textfield',
        fieldLabel: 'Email',
        vtype: 'email',
        bind: '{record.email}'
    }],

    buttons: [{
        text: 'РЎРѕС…СЂР°РЅРёС‚СЊ',
        handler: 'onSave'
    }]
});
