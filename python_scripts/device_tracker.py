# Get Data from Automation Trigger
metatrackerName = "device_tracker." + data.get('meta_entity')
 
# Set new state
newStatus = 'home'
 
hass.states.set(metatrackerName, newStatus, {
    'friendly_name' : data.get('meta_entity')
})