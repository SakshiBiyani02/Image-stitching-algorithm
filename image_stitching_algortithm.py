#Code by-Sakshi Biyani-22BLC1385
import cv2
import numpy as np
from google.colab import files

# Step 1: Upload images
uploaded = files.upload()

# Step 2: Load images
def load_images(image_paths):
    """
    Loads images from uploaded file names.
    """
    images = []
    for path in image_paths:
        img = cv2.imread(path)
        if img is None:
            print(f"Error: Unable to load image {path}")
            continue
        images.append(img)
    return images

# Step 3: Draw dense crisscross feature lines
def draw_dense_crisscross_lines(image):
    """
    Detects features in the image and connects them with colorful lines, including connections to image corners.
    """
    # Convert to grayscale for feature detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use ORB to detect keypoints
    orb = cv2.ORB_create()
    keypoints = orb.detect(gray, None)

    # Draw keypoints on the image
    image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, (0, 255, 0), flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

    # Get all keypoint positions
    points = [tuple(map(int, kp.pt)) for kp in keypoints]

    # Add the four corners of the image
    height, width = image.shape[:2]
    corners = [(0, 0), (0, height - 1), (width - 1, 0), (width - 1, height - 1)]
    points += corners

    # Draw colorful lines between all points
    for i, pt1 in enumerate(points):
        for j, pt2 in enumerate(points):
            if i < j:  # Avoid duplicate lines
                color = tuple(np.random.randint(0, 255, 3).tolist())  # Random color
                cv2.line(image_with_keypoints, pt1, pt2, color, 1)

    # Add annotation for aesthetics
    cv2.putText(image_with_keypoints, "Enhanced Feature Lines", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    return image_with_keypoints

# Step 4: Visualize enhanced feature matches
def visualize_feature_matches(images):
    """
    Draws enhanced feature matches between two images.
    """
    # Ensure at least two images are provided
    if len(images) < 2:
        print("Error: Need at least two images for feature matching visualization.")
        return None

    # Using ORB for feature detection
    detector = cv2.ORB_create()
    kp1, des1 = detector.detectAndCompute(images[0], None)
    kp2, des2 = detector.detectAndCompute(images[1], None)

    # Match features using BFMatcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    # Draw the top 100 matches for better visualization
    match_img = cv2.drawMatches(
        images[0], kp1, images[1], kp2, matches[:100], None,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )

    # Add colorful lines and annotations for beauty
    height, width, _ = match_img.shape
    cv2.line(match_img, (0, height // 4), (width, height // 4), (255, 0, 0), 2)
    cv2.line(match_img, (0, height // 2), (width, height // 2), (0, 255, 0), 2)
    cv2.line(match_img, (0, 3 * height // 4), (width, 3 * height // 4), (0, 0, 255), 2)
    cv2.putText(match_img, "Enhanced Feature Matches", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    # Save the matches image
    cv2.imwrite("feature_matches_enhanced.jpg", match_img)
    print("Enhanced feature matches visualization saved as 'feature_matches_enhanced.jpg'.")
    
    # Add feature lines visualization
    feature_lines_img = draw_dense_crisscross_lines(images[0])
    cv2.imwrite("dense_feature_lines_image.jpg", feature_lines_img)
    print("Dense feature lines visualization saved as 'dense_feature_lines_image.jpg'.")

# Step 5: Stitch images with improved settings
def stitch_images(images):
    """
    Stitches multiple images together using OpenCV's feature-based stitching.
    :param images: List of images.
    :return: Stitched image or None if stitching fails.
    """
    # Initialize the OpenCV Stitcher
    stitcher = cv2.Stitcher.create()

    # Perform the stitching process
    (status, stitched) = stitcher.stitch(images)

    if status == cv2.Stitcher_OK:
        print("Image stitching successful!")
        return stitched
    else:
        print(f"Image stitching failed with status code: {status}")
        if status == cv2.Stitcher_ERR_NEED_MORE_IMGS:
            print("Error: Not enough images or insufficient overlap.")
        elif status == cv2.Stitcher_ERR_HOMOGRAPHY_EST_FAIL:
            print("Error: Homography estimation failed. Check image alignment or feature detection.")
        elif status == cv2.Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL:
            print("Error: Camera parameter adjustment failed.")
        return None

# Step 6: Save the output
def save_image(output_path, image):
    """
    Saves the stitched image to a file.
    :param output_path: Path to save the image.
    :param image: Stitched image.
    """
    cv2.imwrite(output_path, image)
    print(f"Stitched image saved to {output_path}")

# Main workflow
image_paths = list(uploaded.keys())  # Use uploaded file names
images = load_images(image_paths)

if len(images) >= 2:
    # Visualize feature matches
    visualize_feature_matches(images)

    # Stitch images
    stitched_image = stitch_images(images)
    
    if stitched_image is not None:
        save_image("stitched_output.jpeg", stitched_image)
else:
    print("Error: Need at least two images for stitching!")
