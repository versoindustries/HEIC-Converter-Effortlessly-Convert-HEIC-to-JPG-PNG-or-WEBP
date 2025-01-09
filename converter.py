# converter.py

import os
import logging
import shutil
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing
from PIL import Image
import pillow_heif  # Import pillow-heif to add HEIC support to Pillow

# Register pillow_heif with Pillow
pillow_heif.register_heif_opener()

def setup_logging():
    """Sets up logging to a file in the user's home directory."""
    # Create a directory in the user's home folder to store logs
    log_dir = os.path.join(os.path.expanduser("~"), "HEICtoImageConverterLogs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file = os.path.join(log_dir, 'heic_conversion.log')

    # Configure logging to write to the specified log file
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s %(levelname)s:%(message)s'
    )

def convert_heic_image(args):
    """Worker function for converting a single HEIC file to the specified format."""
    input_path, output_path, quality, output_format = args

    FORMAT_MAPPING = {
        'jpg': 'JPEG',
        'jpeg': 'JPEG',
        'png': 'PNG',
        'webp': 'WEBP',  # Add WEBP to the format mapping
    }

    try:
        # Open HEIC image using pillow-heif
        image = Image.open(input_path)

        # Convert image mode if necessary
        if output_format.lower() in ['jpg', 'jpeg']:
            # JPEG doesn't support alpha channels
            if image.mode in ('RGBA', 'LA'):
                background = Image.new('RGB', image.size, (255, 255, 255))
                background.paste(image, mask=image.split()[3])  # 3 is the alpha channel
                image = background
            else:
                image = image.convert('RGB')
        elif output_format.lower() == 'webp':
            # WEBP supports alpha channels, but you can manage mode conversion if needed
            pass  # No mode conversion needed unless specific requirements

        # Adjust save parameters based on output format
        save_kwargs = {}
        if output_format.lower() in ['jpg', 'jpeg']:
            save_kwargs['quality'] = quality
            save_kwargs['optimize'] = True
        elif output_format.lower() == 'png':
            save_kwargs['compress_level'] = int((100 - quality) / 10)
        elif output_format.lower() == 'webp':
            save_kwargs['quality'] = quality
            # For WEBP, you might consider adding 'lossless' parameter if needed
            # save_kwargs['lossless'] = True  # Uncomment for lossless WEBP compression

        # Get the correct format for saving
        save_format = FORMAT_MAPPING.get(output_format.lower(), output_format.upper())

        # Save the image
        image.save(output_path, format=save_format, **save_kwargs)
        logging.info(f"Converted {os.path.basename(input_path)} to {save_format} at '{output_path}'.")
        return True
    except Exception as e:
        logging.error(f"Failed to convert {input_path}: {e}")
        traceback.print_exc()
        return False


def copy_file_task(args):
    """Worker function for copying a file."""
    input_path, output_path = args
    try:
        shutil.copy2(input_path, output_path)
        logging.info(f"Copied {os.path.basename(input_path)} to output directory.")
        return True
    except Exception as e:
        logging.error(f"Failed to copy {input_path}: {e}")
        traceback.print_exc()
        return False

def batch_convert_heic(input_directory, output_directory, quality=90, output_format='PNG', progress_callback=None):
    """
    Converts all HEIC files in a directory to the specified format using multiprocessing.
    Non-HEIC files are copied over to the output directory.
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    files = os.listdir(input_directory)
    heic_files = []
    other_files = []

    for filename in files:
        input_path = os.path.join(input_directory, filename)
        if not os.path.isfile(input_path):
            continue  # Skip directories

        if filename.lower().endswith(('.heic', '.heif')):
            base_filename = os.path.splitext(filename)[0]
            output_filename = f"{base_filename}.{output_format.lower()}"
            output_path = os.path.join(output_directory, output_filename)
            heic_files.append((input_path, output_path, quality, output_format))
        else:
            output_path = os.path.join(output_directory, filename)
            other_files.append((input_path, output_path))

    total_tasks = len(heic_files) + len(other_files)

    # Limit the number of workers to avoid overloading the CPU
    max_workers = min(multiprocessing.cpu_count(), 4)  # Adjust as appropriate

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = []

        # Submit HEIC conversion tasks
        for args in heic_files:
            future = executor.submit(convert_heic_image, args)
            futures.append(future)

        # Submit file copy tasks
        for args in other_files:
            future = executor.submit(copy_file_task, args)
            futures.append(future)

        # Process futures as they complete
        processed_files = 0
        for future in as_completed(futures):
            try:
                result = future.result()
                processed_files += 1
                if progress_callback:
                    progress_callback(processed_files, total_tasks)
            except Exception as e:
                logging.error(f"Exception occurred: {e}")
