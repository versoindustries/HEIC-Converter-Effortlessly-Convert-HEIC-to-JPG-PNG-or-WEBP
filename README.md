Sure, here is the revised version of the second sample with the developer instructions and table of contents from the first sample included:

# HEIC Converter: Effortlessly Convert HEIC to JPG, PNG, or WEBP

**Version:** 1.1  
**Author:** Verso Industries, Crafted by Michael Zimmerman  
**License:** MIT License

## Transform Your HEIC Images with Ease

Are you looking for a reliable way to convert HEIC files to JPG or other universally compatible formats? HEIC Converter is your go-to solution for batch converting HEIC images to JPG, PNG, or WEBP formats swiftly and efficiently. Whether you're dealing with photos from your iPhone or need to process HEIC images on your PC, our converter simplifies the process, making your images accessible and editable across all platforms.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Developer Instructions](#developer-instructions)
  - [Prerequisites](#prerequisites)
  - [Setting Up the Development Environment](#setting-up-the-development-environment)
  - [Building the Executable](#building-the-executable)
  - [Creating the Installer](#creating-the-installer)
  - [Project Structure](#project-structure)
- [License](#license)

## Why Choose HEIC Converter?

- **Batch Conversion Made Simple:** Bulk convert HEIC to JPG or other formats in just a few clicks.
- **Preserve Image Quality:** Customize the quality of your output images to maintain high resolution.
- **User-Friendly Interface:** Intuitive design ensures a smooth conversion experience for all users.
- **Multi-Processing Support:** Leverage multiple CPU cores for faster conversions.
- **Cross-Platform Compatibility:** Available for Windows, macOS, and Linux.
- **Free and Open Source:** Completely free to use, modify, and distribute.

## Key Features

### Batch Convert HEIC to JPG, PNG, or WEBP

- Convert multiple HEIC files simultaneously.
- Save time and enhance productivity with efficient batch processing.

### High-Quality Conversion

- **Adjustable Quality Settings:** Define image quality levels between 1-100.
- **Maintain Original Quality:** Ensure your converted images retain their original clarity.

### Easy-to-Use Interface

- **Simple Navigation:** User-friendly GUI built with PyQt5.
- **Step-by-Step Guidance:** Follow straightforward prompts to complete conversions.

### Multi-Processing Power

- **Faster Conversion Times:** Utilize all available CPU cores.
- **Efficient Performance:** Handle large batches without slowdowns.

## How to Convert HEIC to JPG (or Other Formats)

### Step-by-Step Guide

#### Download and Install HEIC Converter

**Windows Users:**

1. Download the installer (HEICConverterSetup.exe) from our official website.
2. Run the installer and follow the on-screen instructions.

**macOS/Linux Users:**

1. Download the source code or executable from our GitHub repository.
2. Install dependencies as needed.

#### Launch the Application

Open HEIC Converter from your desktop or application folder.

#### Select Input Directory

1. Click on the "Browse" button next to "Input Directory."
2. Navigate to the folder containing your HEIC images.
3. Click "OK."

#### Select Output Directory

1. Click on the "Browse" button next to "Output Directory."
2. Choose where you want to save the converted images.
3. Click "OK."

#### Set Conversion Preferences

- **Quality (1-100):** Enter a value to set your desired image quality (default is 90).
- **Output Format:** Choose JPG, PNG, or WEBP from the dropdown menu.

#### Start Conversion

1. Click on the "Convert" button.
2. A progress bar will display the conversion status.

#### Completion

After the process completes, a confirmation message will appear. Access your converted images in the output directory you selected.

## Installation and Setup

### System Requirements

- **Operating System:** Windows 7 or higher, macOS*, or Linux*.
- **Python 3.6+** (if running from source).
- **Dependencies:** pillow-heif, PyQt5 (included in the installer).

* Build required for macOS and Linux. Executable is for Windows.

### For Windows Users

#### Download the Installer

Obtain HEICConverterSetup.exe from the official website.

#### Run the Installer

1. Double-click the installer file.
2. Follow the setup wizard instructions.

#### Launch HEIC Converter

Find the application in your Start Menu or on your desktop.

### For macOS/Linux Users

#### Clone the Repository

```bash
git clone https://github.com/VersoIndustries/heic-converter.git
cd heic-converter
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Run the Application

```bash
python gui.py
```

## Developer Instructions

### Prerequisites

Ensure you have the following installed:

- **Python:** Download Python 3.6 or higher
- **pip:** Comes bundled with Python 3.6+, or install separately
- **Inno Setup Compiler:** [Download here](https://jrsoftware.org/isdl.php)

### Setting Up the Development Environment

#### Clone the Repository

```bash
git clone https://github.com/yourusername/heic-converter.git
cd heic-converter
```

#### Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

#### Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

#### Install Required Packages

```bash
pip install -r requirements.txt
```

If a requirements.txt file is not present, install the packages manually:

```bash
pip install cx-Freeze PyQt5 Pillow pillow-heif
```

Note: Installing pillow-heif might require additional system dependencies. For Windows, wheels are usually available. For macOS/Linux, ensure you have libheif and libde265 installed.

### Building the Executable

The application uses cx_Freeze to build an executable for Windows.

#### Run the Build Script

```bash
python setup.py build
```

This will create a build_exe directory containing the executable and all necessary files.

#### Verify the Build

Navigate to the build_exe directory and test the executable:

```bash
cd build_exe
HEICConverter.exe
```

Ensure the application runs without errors.

### Creating the Installer

The installer is created using Inno Setup.

#### Install Inno Setup Compiler

Download and install from [here](https://jrsoftware.org/isdl.php).

#### Prepare the Installer Script

The installer script is located in HEICConverterInstaller.iss.

Important: Update the Source path in the [Files] section to point to your build_exe directory. For example:

```ini
[Files]
Source: "C:\Path\To\Your\Project\build_exe\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
```

#### Compile the Installer

1. Open HEICConverterInstaller.iss in Inno Setup Compiler.
2. Go to Build -> Compile (or press F9).

The compiled installer executable will be placed in the dist_installer directory specified in the script.

#### Test the Installer

Run the generated HEICConverterSetup.exe to ensure that the installation process works correctly and the application runs after installation.

### Project Structure

- **setup.py:** Build script for cx_Freeze to create an executable.
- **gui.py:** Main GUI application code using PyQt5.
- **converter.py:** Contains the logic for converting images and utility functions.
- **HEICConverterInstaller.iss:** Inno Setup script for creating the Windows installer.
- **requirements.txt:** List of Python dependencies.
- **README.md:** This documentation file.
- **LICENSE:** License information for the project.
- **build_exe/:** The directory where the build output is stored after running the build script.
- **dist_installer/:** The directory where the installer is output after compilation.

## Frequently Asked Questions

**Can I convert multiple HEIC files at once?**  
Yes! With HEIC Converter, you can batch convert HEIC to JPG, PNG, or WEBP formats, saving you time and effort.

**Is HEIC Converter free?**  
Absolutely. HEIC Converter is a free heic to jpg converter available for everyone. It's open-source under the MIT License.

**Does it work on Windows?**  
Yes, our converter is compatible with Windows, macOS, and Linux platforms.

**How do I ensure the best image quality?**  
You can adjust the "Quality (1-100)" setting before conversion. A higher value retains more image detail.

**Where can I get support?**  
For assistance, contact us at michael.zimmerman@versoindustries.com or visit our GitHub page.

## Enhance Your Image Workflow Today

Don't let file compatibility hinder your productivity. Convert HEIC files to JPG free of charge and enjoy seamless integration with all your devices and software. Whether you're a professional photographer or just looking to view your iPhone pictures on a PC, HEIC Converter simplifies the process.  
Download HEIC Converter now and unlock the full potential of your image library!

## Contact Us

For any questions or support, please reach out:

- **Email:** mike@versoindustries.com
- **GitHub:** VersoIndustries
- **Website:** [www.versoindustries.com](http://www.versoindustries.com)

## Note

Please ensure you have the rights to convert and use images according to their respective licenses and policies.

By choosing HEIC Converter, you're opting for a seamless, efficient, and reliable solution to manage and convert your HEIC images. Experience hassle-free conversion and enjoy your images anywhere, anytime.  
**Download Now and Start Converting!**