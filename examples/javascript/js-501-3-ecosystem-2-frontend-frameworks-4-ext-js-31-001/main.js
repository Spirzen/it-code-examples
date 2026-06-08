Ext.define('App.model.User', {
    extend: 'Ext.Data.Model',
    fields: [
        { name: 'id', type: 'int' },
        { name: 'firstName', type: 'string', defaultValue: '' },
        { name: 'lastName', type: 'string', defaultValue: '' },
        { name: 'email', type: 'string', 
          validate: { type: 'email' } }
    ],
    proxy: {
        type: 'rest',
        url: '/api/users',
        reader: { type: 'json', rootProperty: 'data' }
    }
});
