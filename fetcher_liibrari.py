import requests
import os
from urllib.parse import urlparse
import uuid

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URL from user
    url = input("Please enter the image URL: ").strip()
    
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Fetch the image with timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Check if response is actually an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print("✗ The provided URL does not point to an image.")
            return
        
        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename or "." not in filename:
            # Generate unique filename with uuid
            extension = content_type.split("/")[-1] or "jpg"
            filename = f"image_{uuid.uuid4().hex}.{extension}"
        
        filepath = os.path.join("Fetched_Images", filename)
        
        # Prevent duplicate downloads
        if os.path.exists(filepath):
            print(f"✗ Duplicate detected: {filename} already exists in Fetched_Images.")
            return
        
        # Save the image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)
        
        # Respectful success messages
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")
    
    except requests.exceptions.MissingSchema:
        print("✗ Invalid URL. Please include 'http://' or 'https://'.")
    except requests.exceptions.HTTPError as e:
        print(f"✗ HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("✗ Failed to connect. Please check your internet connection or the URL.")
    except requests.exceptions.Timeout:
        print("✗ Request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
