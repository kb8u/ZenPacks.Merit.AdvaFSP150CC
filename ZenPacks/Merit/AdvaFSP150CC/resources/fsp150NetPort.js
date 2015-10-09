(function(){

var ZC = Ext.ns('Zenoss.component');


function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.FSP150NetPortPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'FSP150NetPort',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'name'},
                {name: 'cmEthernetNetPortSfpPartNumber'},
                {name: 'cmEthernetNetPortSfpReach'},
                {name: 'cmEthernetNetPortLaserWaveLength'}
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
                id: 'cmEthernetNetPortLaserWaveLength',
                dataIndex: 'cmEthernetNetPortLaserWaveLength',
                header: _t('Wavelength'),
                sortable: true,
                width: 100
            },{
                id: 'cmEthernetNetPortSfpReach',
                dataIndex: 'cmEthernetNetPortSfpReach',
                header: _t('SFP reach'),
                sortable: true,
                width: 150
            },{
                id: 'cmEthernetNetPortSfpPartNumber',
                dataIndex: 'cmEthernetNetPortSfpPartNumber',
                header: _t('SFP Part Number'),
                sortable: true,
                width: 200
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
        ZC.FSP150NetPortPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('FSP150NetPortPanel', ZC.FSP150NetPortPanel);
ZC.registerName('FSP150NetPort', _t('NetPort'), _t('NetPorts'));
})();


