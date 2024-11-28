from Logo.logo import Logo


class MainPage:
    def __init__(self):
        self.logo = Logo()
        self.title = "Main Page"

    def show(self):
        print(self.title)

if __name__ =="__main__":
    main_page = MainPage()
    main_page.logo.draw()
    main_page.show()

