(function(){

var ZC = Ext.ns('Zenoss.component');


function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.FSP150SlotPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'FSP150Slot',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'name'},
                {name: 'slotCardUnitName'},
                {name: 'slotCardPartNumber'},
                {name: 'slotCardSerialNum'}
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'status'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true,
                width: 150
            },{
                id: 'slotCardUnitName',
                dataIndex: 'slotCardUnitName',
                header: _t('Model'),
                sortable: true,
                width: 150
            },{
                id: 'slotCardPartNumber',
                dataIndex: 'slotCardPartNumber',
                header: _t('Part Number'),
                sortable: true,
                width: 150
            },{
                id: 'slotCardSerialNum',
                dataIndex: 'slotCardSerialNum',
                header: _t('Serial Number'),
                sortable: true,
                width: 150
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                sortable: true
            },{
                id: 'status',
                dataIndex: 'status',
                header: _t('Status'),
                renderer: Zenoss.render.pingStatus,
            }]
        });
        ZC.FSP150SlotPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('FSP150SlotPanel', ZC.FSP150SlotPanel);
ZC.registerName('FSP150Slot', _t('Slot'), _t('Slots'));
})();


