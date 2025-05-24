from gui.dashboard import DashboardApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
