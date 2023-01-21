from flet import (
    flet,
    Page,
    Column,
    Row
)


class ChatBotApp(Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.page.update()


def main(page: Page):

    page.title = "ChatGPT Desktop"
    page.padding = 0
    app = ChatBotApp()
    page.add(app)
    page.update()


if __name__ == "__main__" :

    flet.app(target=main)
