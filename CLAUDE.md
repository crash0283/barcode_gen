# CLAUDE.md - AI Assistant Guide for Barcode Generator

## Project Overview

This is a **Barcode PDF Generator** application built with Python. It provides a GUI interface for generating Code39 barcodes and exporting them as both individual JPEG images and a combined PDF document.

**Primary Use Case**: Generate printable barcode labels from user-provided codes (up to 10 at a time).

## Repository Structure

```
barcode_gen/
├── main.py           # Main application (GUI + barcode generation logic)
├── main.spec         # PyInstaller spec file for building Windows executable
├── output/           # Pre-built executable distribution
│   └── glBarcodeGen.exe
├── .idea/            # PyCharm/IntelliJ project configuration
└── CLAUDE.md         # This file
```

## Key Technologies & Dependencies

| Library | Purpose |
|---------|---------|
| `PySimpleGUI` | GUI framework for the application interface |
| `python-barcode` | Barcode generation (Code39 format) |
| `img2pdf` | Converting JPEG images to PDF |
| `Pillow` | Image handling (dependency of python-barcode ImageWriter) |

### Installation

```bash
pip install PySimpleGUI python-barcode img2pdf Pillow
```

## Code Architecture

### Single-File Application (`main.py`)

The application follows a simple procedural structure:

1. **Configuration** (lines 12-14): Render options for barcode font
2. **Core Functions**:
   - `process_images()` (line 17): Generates barcode images and compiles PDF
   - `create_barcodes()` (line 31): Entry point for barcode creation
3. **GUI Layout** (lines 36-54): PySimpleGUI window definition
4. **Event Loop** (lines 58-76): Main application flow handling Submit/Cancel

### Data Flow

```
User Input (10 barcode fields)
    → create_barcodes()
    → process_images()
    → [Code39 barcode images]
    → img2pdf.convert()
    → PDF output
```

## Development Workflows

### Running the Application

```bash
python main.py
```

**Note**: The application requires a display (GUI). It will not run in headless environments.

### Building Executable (Windows)

The project uses PyInstaller for creating standalone executables:

```bash
pyinstaller main.spec
```

Or to rebuild from scratch:

```bash
pyinstaller --name=glBarcodeGen --onefile main.py
```

## Important Code Conventions

### Barcode Format
- Uses **Code39** barcode format (alphanumeric, variable length)
- Previously may have used EAN13 (import exists but unused)

### File Output
- Individual barcode images: `{prefix}_{barcode_number}.jpeg`
- Combined PDF: User-specified path via Save dialog

### Hardcoded Configuration
- Font path is Windows-specific: `C:/Windows/fonts/Arial.ttf`
- This will need modification for cross-platform support

## Known Limitations & Technical Debt

1. **Platform Dependency**: Font path hardcoded for Windows
2. **No Error Handling**: Missing validation for:
   - Invalid barcode inputs
   - File write permissions
   - Missing font file
3. **GUI Key Indexing**: Uses magic numbers for accessing form values (e.g., `values[11]`, `values[14]`)
4. **No CLI Mode**: Requires GUI; no headless/batch processing option

## Testing Considerations

- No automated tests exist
- Manual testing requires GUI interaction
- Consider adding unit tests for `process_images()` and `create_barcodes()`

## When Making Changes

### Do
- Maintain the simple single-file structure for small enhancements
- Test barcode output with barcode scanner/reader
- Consider cross-platform font handling if modifying render options
- Preserve existing GUI layout structure

### Avoid
- Breaking changes to the PDF output format
- Adding dependencies without clear necessity
- Removing PySimpleGUI (it's the core UI framework)

## Git Workflow

- Main development happens on feature branches prefixed with `claude/`
- Keep commits atomic and focused
- The repository has minimal history (initialized recently)

## Quick Reference

| Task | Command/Location |
|------|------------------|
| Run application | `python main.py` |
| Build executable | `pyinstaller main.spec` |
| Output directory | `./output/` |
| Main logic | `main.py:17-33` |
| GUI definition | `main.py:36-54` |
