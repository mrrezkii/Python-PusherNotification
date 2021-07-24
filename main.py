from pusher_push_notifications import PushNotifications

pn_client = PushNotifications(
    instance_id='664b9c5f-0e58-442f-a7e4-4f7c7e0c2b87',
    secret_key='A975DDC2A5253248B6DEA2167B6ADBFC20BE8473F27B671D0D50FF1103EA3F7A',
)

response = pn_client.publish(
    interests=['hello'],
    publish_body={'apns': {'aps': {'alert': 'Report Created'}},
                  'fcm': {'notification': {'title': "First notif", 'body': "First notif body"}}}
)

print(response['publishId'])