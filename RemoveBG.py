import os
import io
import multiprocessing
from rembg import new_session, remove
from PIL import Image
from concurrent.futures import ProcessPoolExecutor

TARGET_WIDTH = 900

# Resize: width 900, auto height
def resize_width(img, target_width=900):
    w_percent = (target_width / float(img.width))
    target_height = int((float(img.height) * float(w_percent)))
    return img.resize((target_width, target_height), Image.LANCZOS)

# Process a single image
def process_image(args):
    file_name, current_dir, output_folder, model_name = args
    try:
        input_path = os.path.join(current_dir, file_name)
        output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".png")

        # Each process creates its own session
        session = new_session(model_name)

        with open(input_path, "rb") as inp:
            result = remove(inp.read(), session=session)

        with Image.open(io.BytesIO(result)).convert("RGBA") as img:
            final_img = resize_width(img, TARGET_WIDTH)
            final_img.save(output_path, dpi=(72, 72), format="PNG")

        return f"Processed successfully: {file_name}"
    except Exception as e:
        return f"Error processing {file_name}: {e}"

def main():
    current_dir = os.getcwd()
    output_folder = os.path.join(current_dir, "output")
    os.makedirs(output_folder, exist_ok=True)

    files = [f for f in os.listdir(current_dir) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    if not files:
        print("No images found in the current folder.")
        input("Press Enter to exit...")
        return

    print(f"Found {len(files)} image(s).")

    # Number of CPU cores
    cpu_count = multiprocessing.cpu_count()
    max_workers = max(1, cpu_count - 1)
    print(f"Using {max_workers} parallel processes (out of {cpu_count} cores).")

    # Prepare arguments for each file
    args_list = [(f, current_dir, output_folder, "u2net") for f in files]

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(process_image, args_list)
        for r in results:
            print(r)

    print("\nAll images processed and saved in the 'output' folder.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()