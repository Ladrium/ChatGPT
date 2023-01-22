from flet import (
    flet as ft,
    Page,
    border,
    Stack,
    icons,
    ElevatedButton,
    Row,
    ButtonStyle,
    Container,
    Icon,
)
from flet.buttons import RoundedRectangleBorder


def main(page: Page):
    page.title = "ChatGPT"
    page.icon = Icon(icons.CHAT)
    page.window_max_height = 650
    page.window_title_bar_hidden = False
    page.add(
        Container(
            Stack(
                [Container(bgcolor="#232A31", width=188, height=612, top=7, left=6, border_radius=25, border=border.all(5, "#00000")),
                 ElevatedButton("+ New Chat", top=544, left=23, width=155, height=58,
                                style=ButtonStyle(bgcolor="#10141B", shape=RoundedRectangleBorder(radius=15)))]),
            bgcolor="#446074",
            padding=0,
            margin=0,
            width=700,
            height=650
        ))
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
