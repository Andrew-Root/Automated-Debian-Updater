import curses
import subprocess

# Function to execute a command and stream output to the GUI
def run_command_stream(stdscr, command, description):
    stdscr.clear()
    stdscr.addstr(1, 2, f"[INFO] {description}...", curses.color_pair(3))
    stdscr.refresh()

    try:
        process = subprocess.Popen(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        line_y = 3
        for line in process.stdout:
            stdscr.addstr(line_y, 2, line.strip(), curses.color_pair(4))
            stdscr.refresh()
            line_y += 1
            if line_y >= curses.LINES - 2:  # Handle screen overflow
                line_y = 3
                stdscr.clear()
                stdscr.addstr(1, 2, "[INFO] Scrolling output...", curses.color_pair(3))
                stdscr.refresh()

        process.wait()
        if process.returncode == 0:
            stdscr.addstr(line_y, 2, f"[SUCCESS] {description} completed!", curses.color_pair(1))
        else:
            stdscr.addstr(line_y, 2, f"[ERROR] {description} failed!", curses.color_pair(2))

    except Exception as e:
        stdscr.addstr(3, 2, f"[ERROR] {str(e)}", curses.color_pair(2))

    stdscr.addstr(curses.LINES - 2, 2, "Press any key to return to the menu.", curses.color_pair(4))
    stdscr.refresh()
    stdscr.getch()

# Function to display the main menu
def display_menu(stdscr):
    stdscr.clear()
    stdscr.border(0)
    stdscr.bkgd(curses.color_pair(3))
    stdscr.addstr(1, 2, "Automate Debian Updater", curses.A_BOLD | curses.color_pair(1))
    stdscr.addstr(2, 2, "A simple tool to keep your Debian system updated!", curses.color_pair(4))
    stdscr.addstr(4, 2, "[1] Update package lists", curses.color_pair(1))
    stdscr.addstr(5, 2, "[2] Upgrade packages", curses.color_pair(1))
    stdscr.addstr(6, 2, "[3] Full distribution upgrade", curses.color_pair(1))
    stdscr.addstr(7, 2, "[4] Clean obsolete files", curses.color_pair(1))
    stdscr.addstr(8, 2, "[q] Quit", curses.color_pair(1))
    stdscr.refresh()

# Main GUI loop
def main_gui(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    display_menu(stdscr)

    while True:
        stdscr.addstr(10, 2, "Select an option: ", curses.color_pair(3))
        key = stdscr.getch()

        if key == ord('1'):
            run_command_stream(stdscr, "sudo apt-get update", "Updating package lists")
            display_menu(stdscr)  # Return to the menu
        elif key == ord('2'):
            run_command_stream(stdscr, "sudo apt-get upgrade -y", "Upgrading packages")
            display_menu(stdscr)  # Return to the menu
        elif key == ord('3'):
            run_command_stream(stdscr, "sudo apt-get dist-upgrade -y", "Performing distribution upgrade")
            display_menu(stdscr)  # Return to the menu
        elif key == ord('4'):
            run_command_stream(stdscr, "sudo apt-get autoclean", "Cleaning obsolete files")
            display_menu(stdscr)  # Return to the menu
        elif key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main_gui)