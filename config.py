SERVER_ADDRESS = ''  # Game server IP
SERVER_PORT = 27016  # Query port
SERVER_POLL_RATE = 5  # Max query rate, in seconds

DISCORD_TOKEN = ''  # App token
DISCORD_CHANNEL = ''  # Channel ID (numbers)

BOT_ICON_URL = 'https://i.imgur.com/DsxGVnu.jpg'

# Send alerts to @everyone trying to get more people in, only when threshold min < player count < threshold max
ALERT_EVERYONE_ENABLED = True
ALERT_EVERYONE_THRESHOLD_MIN = 7
ALERT_EVERYONE_THRESHOLD_MAX = 12

# Player count when to consider the game has started
ALERT_PLAYERCOUNT_START = 12

# Cap @everyone alerts to prevent spamming, in seconds
ALERT_EVERYONE_TIME_CAP = 300

# Send a RIP alert when everyone left the server after a successful ALERT_PLAYERCOUNT_START
ALERT_EVERYONE_RIP = True
