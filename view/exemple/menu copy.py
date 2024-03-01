import flet


class Menu:
    def __init__(self, page: flet.Page):
        self.page = page
        self.appbar_text_ref = flet.Ref[flet.Text]()
        self.setup_ui()

    def setup_ui(self):
        self.page.theme_mode = flet.ThemeMode.LIGHT
        self.page.appbar = flet.AppBar(
            title=flet.Text("Data Modeler Automation", ref=self.appbar_text_ref,
                            color=flet.colors.WHITE),
            center_title=True,
            bgcolor='#2A579A'
        )

        menubar = flet.MenuBar(
            expand=True,
            style=flet.MenuStyle(
                alignment=flet.alignment.top_left,
                bgcolor=flet.colors.RED_100,
                mouse_cursor={flet.MaterialState.HOVERED: flet.MouseCursor.WAIT,
                              flet.MaterialState.DEFAULT: flet.MouseCursor.ZOOM_OUT},
            ),
            controls=[
                flet.SubmenuButton(
                    content=flet.Text("File"),
                    on_open=self.handle_on_open,
                    on_close=self.handle_on_close,
                    on_hover=self.handle_on_hover,
                    controls=[
                        flet.MenuItemButton(
                            content=flet.Text("New"),
                            leading=flet.Icon(flet.icons.ADD),
                            style=flet.ButtonStyle(
                                bgcolor={flet.MaterialState.HOVERED: flet.colors.GREEN_100}),
                            on_click=self.handle_menu_item_click
                        ),
                        flet.MenuItemButton(
                            content=flet.Text("Save"),
                            leading=flet.Icon(flet.icons.SAVE),
                            style=flet.ButtonStyle(
                                bgcolor={flet.MaterialState.HOVERED: flet.colors.GREEN_100}),
                            on_click=self.handle_menu_item_click
                        ),
                        flet.MenuItemButton(
                            content=flet.Text("Save as"),
                            leading=flet.Icon(flet.icons.SAVE_AS),
                            style=flet.ButtonStyle(
                                bgcolor={flet.MaterialState.HOVERED: flet.colors.GREEN_100}),
                            on_click=self.handle_menu_item_click
                        ),
                        flet.MenuItemButton(
                            content=flet.Text("Print"),
                            leading=flet.Icon(flet.icons.PRINT),
                            style=flet.ButtonStyle(
                                bgcolor={flet.MaterialState.HOVERED: flet.colors.GREEN_100}),
                            on_click=self.handle_menu_item_click
                        ),
                        flet.MenuItemButton(
                            content=flet.Text("Shared"),
                            leading=flet.Icon(flet.icons.SHARE),
                            style=flet.ButtonStyle(
                                bgcolor={flet.MaterialState.HOVERED: flet.colors.GREEN_100}),
                            on_click=self.handle_menu_item_click
                        ),
                        flet.MenuItemButton(
                            content=flet.Text("Export"),
                            leading=flet.Icon(flet.icons.IMPORT_EXPORT),
                            style=flet.ButtonStyle(
                                bgcolor={flet.MaterialState.HOVERED: flet.colors.GREEN_100}),
                            on_click=self.handle_menu_item_click
                        ),
                        flet.MenuItemButton(
                            content=flet.Text("Close"),
                            leading=flet.Icon(flet.icons.CLOSE),
                            style=flet.ButtonStyle(
                                bgcolor={flet.MaterialState.HOVERED: flet.colors.GREEN_100}),
                            on_click=self.handle_menu_item_click
                        )
                    ]
                ),
                flet.SubmenuButton(
                    content=flet.Text("Insert"),
                    on_open=self.handle_on_open,
                    on_close=self.handle_on_close,
                    on_hover=self.handle_on_hover,
                    controls=[
                        flet.SubmenuButton(
                            content=flet.Text("Zoom"),
                            controls=[
                                flet.MenuItemButton(
                                    content=flet.Text("Magnify"),
                                    leading=flet.Icon(flet.icons.ZOOM_IN),
                                    close_on_click=False,
                                    style=flet.ButtonStyle(
                                        bgcolor={flet.MaterialState.HOVERED: flet.colors.PURPLE_200}),
                                    on_click=self.handle_menu_item_click
                                ),
                                flet.MenuItemButton(
                                    content=flet.Text("Minify"),
                                    leading=flet.Icon(flet.icons.ZOOM_OUT),
                                    close_on_click=False,
                                    style=flet.ButtonStyle(
                                        bgcolor={flet.MaterialState.HOVERED: flet.colors.PURPLE_200}),
                                    on_click=self.handle_menu_item_click
                                )
                            ]
                        )
                    ]
                ),
                flet.SubmenuButton(
                    content=flet.Text("Design"),
                    on_open=self.handle_on_open,
                    on_close=self.handle_on_close,
                    on_hover=self.handle_on_hover,
                    controls=[
                        flet.SubmenuButton(
                            content=flet.Text("Zoom"),
                            controls=[
                                flet.MenuItemButton(
                                    content=flet.Text("Magnify"),
                                    leading=flet.Icon(flet.icons.ZOOM_IN),
                                    close_on_click=False,
                                    style=flet.ButtonStyle(
                                        bgcolor={flet.MaterialState.HOVERED: flet.colors.PURPLE_200}),
                                    on_click=self.handle_menu_item_click
                                ),
                                flet.MenuItemButton(
                                    content=flet.Text("Minify"),
                                    leading=flet.Icon(flet.icons.ZOOM_OUT),
                                    close_on_click=False,
                                    style=flet.ButtonStyle(
                                        bgcolor={flet.MaterialState.HOVERED: flet.colors.PURPLE_200}),
                                    on_click=self.handle_menu_item_click
                                )
                            ]
                        )
                    ]
                ),
                flet.SubmenuButton(
                    content=flet.Text("Layout"),
                    on_open=self.handle_on_open,
                    on_close=self.handle_on_close,
                    on_hover=self.handle_on_hover,
                    controls=[
                        flet.SubmenuButton(
                            content=flet.Text("Zoom"),
                            controls=[
                                flet.MenuItemButton(
                                    content=flet.Text("Magnify"),
                                    leading=flet.Icon(flet.icons.ZOOM_IN),
                                    close_on_click=False,
                                    style=flet.ButtonStyle(
                                        bgcolor={flet.MaterialState.HOVERED: flet.colors.PURPLE_200}),
                                    on_click=self.handle_menu_item_click
                                ),
                                flet.MenuItemButton(
                                    content=flet.Text("Minify"),
                                    leading=flet.Icon(flet.icons.ZOOM_OUT),
                                    close_on_click=False,
                                    style=flet.ButtonStyle(
                                        bgcolor={flet.MaterialState.HOVERED: flet.colors.PURPLE_200}),
                                    on_click=self.handle_menu_item_click
                                )
                            ]
                        )
                    ]
                ),
                flet.SubmenuButton(
                    content=flet.Text("Reference"),
                    on_open=self.handle_on_open,
                    on_close=self.handle_on_close,
                    on_hover=self.handle_on_hover,
                    controls=[
                        flet.SubmenuButton(
                            content=flet.Text("Zoom"),
                            controls=[
                                flet.MenuItemButton(
                                    content=flet.Text("Magnify"),
                                    leading=flet.Icon(flet.icons.ZOOM_IN),
                                    close_on_click=False,
                                    style=flet.ButtonStyle(
                                        bgcolor={flet.MaterialState.HOVERED: flet.colors.PURPLE_200}),
                                    on_click=self.handle_menu_item_click
                                ),
                                flet.MenuItemButton(
                                    content=flet.Text("Minify"),
                                    leading=flet.Icon(flet.icons.ZOOM_OUT),
                                    close_on_click=False,
                                    style=flet.ButtonStyle(
                                        bgcolor={flet.MaterialState.HOVERED: flet.colors.PURPLE_200}),
                                    on_click=self.handle_menu_item_click
                                )
                            ]
                        )
                    ]
                ),
                flet.SubmenuButton(
                    content=flet.Text("View"),
                    on_open=self.handle_on_open,
                    on_close=self.handle_on_close,
                    on_hover=self.handle_on_hover,
                    controls=[
                        flet.SubmenuButton(
                            content=flet.Text("Zoom"),
                            controls=[
                                flet.MenuItemButton(
                                    content=flet.Text("Magnify"),
                                    leading=flet.Icon(flet.icons.ZOOM_IN),
                                    close_on_click=False,
                                    style=flet.ButtonStyle(
                                        bgcolor={flet.MaterialState.HOVERED: flet.colors.PURPLE_200}),
                                    on_click=self.handle_menu_item_click
                                ),
                                flet.MenuItemButton(
                                    content=flet.Text("Minify"),
                                    leading=flet.Icon(flet.icons.ZOOM_OUT),
                                    close_on_click=False,
                                    style=flet.ButtonStyle(
                                        bgcolor={flet.MaterialState.HOVERED: flet.colors.PURPLE_200}),
                                    on_click=self.handle_menu_item_click
                                )
                            ]
                        )
                    ]
                ),
                flet.SubmenuButton(
                    content=flet.Text("About"),
                    on_open=self.handle_on_open,
                    on_close=self.handle_on_close,
                    on_hover=self.handle_on_hover,
                    controls=[
                        flet.SubmenuButton(
                            content=flet.Text("Zoom"),
                            controls=[
                                flet.MenuItemButton(
                                    content=flet.Text("Magnify"),
                                    leading=flet.Icon(flet.icons.ZOOM_IN),
                                    close_on_click=False,
                                    style=flet.ButtonStyle(
                                        bgcolor={flet.MaterialState.HOVERED: flet.colors.PURPLE_200}),
                                    on_click=self.handle_menu_item_click
                                ),
                                flet.MenuItemButton(
                                    content=flet.Text("Minify"),
                                    leading=flet.Icon(flet.icons.ZOOM_OUT),
                                    close_on_click=False,
                                    style=flet.ButtonStyle(
                                        bgcolor={flet.MaterialState.HOVERED: flet.colors.PURPLE_200}),
                                    on_click=self.handle_menu_item_click
                                )
                            ]
                        )
                    ]
                ),

            ]
        )

        self.page.add(
            flet.Row([menubar]),
        )

    def handle_menu_item_click(self, e):
        print(f"{e.control.content.value}.on_click")
        self.page.show_snack_bar(flet.SnackBar(content=flet.Text(
            f"{e.control.content.value} was clicked!")))
        self.appbar_text_ref.current.value = e.control.content.value
        self.page.update()

    def handle_on_open(self, e):
        print(f"{e.control.content.value}.on_open")

    def handle_on_close(self, e):
        print(f"{e.control.content.value}.on_close")

    def handle_on_hover(self, e):
        print(f"{e.control.content.value}.on_hover")


def main(page: flet.Page):
    app = Menu(page)


if __name__ == "__main__":
    flet.app(target=main)
