# Get Data from Automation Trigger
triggeredEntity = data.get('entity_id')
metatrackerName = "device_tracker." + data.get('meta_entity')
 
# Set new state
newStatus = 'home'
 
hass.states.set(metatrackerName, newStatus, {
    'friendly_name' : data.get('meta_entity')
})