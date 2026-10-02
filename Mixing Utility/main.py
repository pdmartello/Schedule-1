import sys
from gui.gui import run_app

def main():
    # Your program's logic goes here
    print("Starting Schedule I Mixing Utilty...")
    
    # Optional: Return an exit code (0 for success)
    # Start the GUI
    run_app()

if __name__ == "__main__":
    # Executes main() only when run directly, not when imported
    sys.exit(main())