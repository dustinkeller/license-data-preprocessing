import csv
import os
import cv2

# Function to convert bounding box coordinates to YOLO format
def convert_to_yolo_format(image_width, image_height, x_min, y_min, x_max, y_max):
    # Normalize coordinates and dimensions
    x_center = (x_min + x_max) / 2 / image_width
    y_center = (y_min + y_max) / 2 / image_height
    width = (x_max - x_min) / image_width
    height = (y_max - y_min) / image_height
    return x_center, y_center, width, height

csv_file = 'plates.csv'

# Directory to save YOLO annotation files
output_root_dir = 'annotations_yolo'
os.makedirs(output_root_dir, exist_ok=True)
os.makedirs(f"{output_root_dir}/train/labels", exist_ok=True)
os.makedirs(f"{output_root_dir}/train/images", exist_ok=True)
os.makedirs(f"{output_root_dir}/test/labels", exist_ok=True)
os.makedirs(f"{output_root_dir}/test/images", exist_ok=True)
os.makedirs(f"{output_root_dir}/valid/labels", exist_ok=True)
os.makedirs(f"{output_root_dir}/valid/images", exist_ok=True)



with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row if exists
    image_index = 1
    for row in csv_reader:
        class_id, image_path, labels, dataset = row

        purpose = image_path.split('/')[0]

        image = cv2.imread(image_path)
        image_height, image_width, _ = image.shape

        # Generate YOLO-compatible annotation
        # Since the entire image is considered as the license plate, we set the bounding box
        # to cover the entire image with a class ID of 0.
        x_center, y_center, width, height = 0.5, 0.5, 1.0, 1.0


        annotation_filename = f"{image_index}.txt"

        annotation_path = os.path.join(f"{output_root_dir}/{purpose}/labels", annotation_filename)
        with open(annotation_path, 'w') as annotation_file:
            annotation_file.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

        print(f"Annotation file saved for {image_path} at {annotation_path}")

        new_image_filename = f"{image_index}.jpg"
        new_image_path = os.path.join(f"{output_root_dir}/{purpose}/images", new_image_filename)
        with open(new_image_path, 'w') as new_image_file:
            cv2.imwrite(new_image_path, image)
        
        image_index += 1
