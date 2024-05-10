from PIL import Image

# Function to hide a message within an image
def hide_message(image_path, message, output_image_path):
    img = Image.open(image_path)
    width, height = img.size
    
    # Convert message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    message_length = len(binary_message)
    
    # Check if the message can fit into the image
    if message_length > width * height * 3:
        print("Message is too long to be hidden in the image!")
        return
    
    # Iterate over each pixel in the image
    data_index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))
            for i in range(3):  # For each RGB component
                if data_index < message_length:
                    pixel[i] = pixel[i] & ~1 | int(binary_message[data_index])
                    data_index += 1
            img.putpixel((x, y), tuple(pixel))
    
    img.save(output_image_path)
    print("Message hidden successfully!")

# Function to extract a message from an image
def extract_message(image_path):
    img = Image.open(image_path)
    width, height = img.size
    
    binary_message = ''
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            for i in range(3):  # For each RGB component
                binary_message += str(pixel[i] & 1)
    
    # Convert binary message to string
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))
        if message[-1] == '\0':  # Null terminator indicates end of message
            break
    
    return message.rstrip('\0')

# if __name__ == "__main__":
    # # Hide a message in an image
    # hide_message("image.jpg", "Hello, world!", "output_image.png")
    
    # # Extract the hidden message from the image
    # extracted_message = extract_message("output_image.png")
    # print("Extracted message:", extracted_message)