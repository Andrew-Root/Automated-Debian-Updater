# Automate Debian Updater

**Automate Debian Updater** is a terminal-based tool for easily updating Debian systems with a colorful **Airgeddon-inspired** interface. It provides an interactive menu to perform common system maintenance tasks such as updating packages, upgrading the system, and cleaning obsolete files.

## 🎨 Features

- **Colorful interface**: Visually appealing design inspired by Airgeddon for an enhanced user experience.
- **Interactive operations**: Execute commands like `update`, `upgrade`, `dist-upgrade`, and `autoclean` with a simple menu selection.
- **Real-time feedback**: Displays packages being updated directly in the terminal.
- **Intuitive menu**: Automatically returns to the main menu after completing an operation.

## 🛠️ Requirements

- Operating System: **Debian** or Debian-based distributions (e.g., Ubuntu).
- **Python 3.6+**
- Administrator privileges (required to run `apt-get` commands).

## 📥 Installation

1. ```bash
   git clone https://github.com/Andrew-Root/automate-debian-updater.git
2. ```bash
   cd automate-debian-updater
3. ```bash
   sudo python3 automate_debian_updater_gui.py

🚀 Usage

Select an option from the interactive menu:

* [1] Update package lists.
* [2] Upgrade installed packages.
* [3] Perform a full distribution upgrade.
* [4] Clean obsolete files.
* [5] Auto-remove unnecessary packages.
* [q] Quit.
Follow the on-screen instructions.


💡 Note: Make sure to run the script in a terminal compatible with Python curses.

