import pyshorteners

# Create a pyshorteners.Shortener object with the desired URL shortener service
shortener = pyshorteners.Shortener('Tinyurl')

# Prompt the user to enter the long URL
long_url = input('Enter the long URL: ')

# Shorten the URL
short_url = shortener.short(long_url)

# Print the short URL
print(f'Short URL: {short_url}')
