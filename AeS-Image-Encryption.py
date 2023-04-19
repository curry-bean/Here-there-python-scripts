from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image

# Define AES encryption parameters
KEY_SIZE = 16  # AES-128
BLOCK_SIZE = 16  # 128-bit blocks

# Function to encrypt an image file with AES
def encrypt_image(image_path, key):
    # Load image
    image = Image.open(image_path)

    # Convert image to RGB mode if it's in a different mode (e.g., RGBA)
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Convert image to bytes
    image_bytes = image.tobytes()

    # Pad the image bytes to a multiple of the block size
    padded_image_bytes = pad(image_bytes, BLOCK_SIZE)

    # Generate a random initialization vector (IV)
    iv = get_random_bytes(BLOCK_SIZE)

    # Create AES cipher object in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Encrypt the padded image bytes
    ciphertext = cipher.encrypt(padded_image_bytes)

    # Return the ciphertext and IV
    return ciphertext, iv

# Function to decrypt an image file with AES
def decrypt_image(ciphertext, iv, key, image_path):
    # Create AES cipher object in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    decrypted_bytes = cipher.decrypt(ciphertext)

    # Unpad the decrypted bytes
    unpadded_bytes = unpad(decrypted_bytes, BLOCK_SIZE)

    # Create an image from the decrypted bytes
    decrypted_image = Image.frombytes("RGB", (image_path.size[0], image_path.size[1]), unpadded_bytes)

    # Save the decrypted image
    decrypted_image.save("decrypted_image.jpg")

# Load the image
image_path = "image.jpg"

# Generate a random 128-bit AES key
key = get_random_bytes(KEY_SIZE)

# Encrypt the image
ciphertext, iv = encrypt_image(image_path, key)

# Save the ciphertext and IV to files
with open("ciphertext.bin", "wb") as f:
    f.write(ciphertext)
with open("iv.bin", "wb") as f:
    f.write(iv)

# Decrypt the image
with open("ciphertext.bin", "rb") as f:
    ciphertext = f.read()
with open("iv.bin", "rb") as f:
    iv = f.read()
decrypt_image(ciphertext, iv, key, Image.open(image_path))
