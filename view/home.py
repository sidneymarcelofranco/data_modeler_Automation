import flet as ft
from menu import MenuBarTop


def main(page: ft.Page):
    app = MenuBarTop(page)


if __name__ == "__main__":
    ft.app(target=main)
