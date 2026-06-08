Ext.define('App.mixin.DirtyTracking', {
    extend: 'Ext.Mixin',

    mixinConfig: {
        id: 'dirtytracking'
    },

    // Р”РѕР±Р°РІР»СЏСЋС‚СЃСЏ РјРµС‚РѕРґС‹ Рё РѕР±СЂР°Р±РѕС‚С‡РёРєРё
    onFieldChange: function(field, newValue, oldValue) {
        if (newValue !== oldValue) {
            this.markAsDirty();
        }
    },

    markAsDirty: function() {
        this.dirty = true;
        this.fireEvent('dirtychange', this, true);
    }
});
