# Mobile Agent

A cross-platform desktop application to simplify the installation of Appium-based mobile testing dependencies.

## Overview

This application aims to provide a streamlined experience for test automation engineers and mobile developers to set up their environment for Appium-based tests on real Android and iOS devices. It bundles predefined versions of all necessary Appium dependencies (Node.js, Android SDK, Appium Server + drivers, etc.) to ensure version compatibility and ease of updates.

For dependencies that cannot be automatically installed (e.g., Xcode), the application provides user setup documentation via a locally hosted Material for MkDocs site.

## Features

- **Automated Dependency Installation:** One-click installation of core Appium dependencies.
- **Bundled Dependencies:** All dependencies are bundled within the application for consistency and offline installation.
- **Guided Manual Setup:** For complex installations, the app links to comprehensive, locally hosted documentation.
- **Cross-Platform:** Available for Windows, macOS, and Linux.

## How to Use

1.  **Download:** Get the latest release for your operating system from the [Releases page](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/releases).
2.  **Launch:** Run the executable for your platform.
3.  **Install Dependencies:** Click the "Install Dependencies" button to begin the automated setup.
4.  **Complete Manual Steps:** Follow the instructions for any remaining manual setup steps, using the "View Docs" button to access detailed guides.

## Development

### Setup

1.  Clone the repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
    cd py-mobile-agent
    ```
2.  Create and activate a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Build the documentation:
    ```bash
    source .venv/bin/activate
    mkdocs build -d docs/site
    ```
5.  Run the application:
    ```bash
    source .venv/bin/activate
    python3 src/main.py
    ```

### CI/CD and Releases

This project uses GitHub Actions for continuous integration and delivery. The workflow is configured to build and package the application for Windows, macOS, and Linux on every push to the `main` branch.

To create a new release and attach the built executables:

1.  Ensure all your changes are committed and pushed to the `main` branch.
2.  Create a new Git tag with the format `vX.Y.Z` (e.g., `v0.1.0`):
    ```bash
    git tag v0.1.0
    ```
3.  Push the tag to GitHub:
    ```bash
    git push origin v0.1.0
    ```

This will trigger the GitHub Actions workflow, which will build the application and then create a new release on your GitHub repository with the packaged executables attached as assets.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
