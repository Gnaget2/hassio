# Get Data from Automation Trigger
triggeredEntity = data.get('entity_id')
metatrackerName = "device_tracker." + data.get('meta_entity')
 
# Get new state
newState = 'Home'
newStatus = newState.state
 
Danell = hass.states.get('device_tracker.Danell')
sofias_iphone = hass.states.get('device_tracker.sofias_iphone')
 
 
if metatrackerName == 'device_tracker.Danell':
    picture = 'https://www.gravatar.com/avatar/59f9ec947c160ca5cf77cddf9c0a0e75.jpg?s=80&d=wavatar'
elif metatrackerName == 'device_tracker.sofias_iphone':
    picture = 'https://media.licdn.com/mpr/mpr/shrink_100_100'
 
hass.states.set(metatrackerName, newStatus, {
    'friendly_name' : data.get('meta_entity'),
    'entity_picture' : picture
})