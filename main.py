from frames.container import TkApp

def main():
    root = TkApp()
    root.geometry("500x200")
    root.grid_columnconfigure((0, 1), weight=1)
    root.grid_rowconfigure((1, 2, 3, 4, 5, 6), weight=1)

    root.mainloop()


if __name__ == "__main__":
    main()
