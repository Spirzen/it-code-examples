Ext.define('App.controller.User', {
    extend: 'Ext.app.Controller',

    init: function() {
        this.listen({
            component: {
                'user-edit-form button[text=РЎРѕС…СЂР°РЅРёС‚СЊ]': {
                    click: 'onSave'
                }
            }
        });
    },

    onSave: function(button) {
        var form = button.up('form'),
            viewModel = form.getViewModel(),
            record = viewModel.get('record');

        form.updateRecord(record); // РїРµСЂРµРЅРѕСЃРёС‚ Р·РЅР°С‡РµРЅРёСЏ РёР· РїРѕР»РµР№ РІ РјРѕРґРµР»СЊ

        if (record.isValid()) {
            record.save({
                success: function() {
                    Ext.toast('data СЃРѕС…СЂР°РЅРµРЅС‹');
                },
                failure: function() {
                    Ext.Msg.alert('РћС€РёР±РєР°', 'РќРµ СѓРґР°Р»РѕСЃСЊ СЃРѕС…СЂР°РЅРёС‚СЊ');
                }
            });
        } else {
            form.getForm().markInvalid(record.getValidation().errors);
        }
    }
});
