import flet
from flet import Column, Container, Page, Row, Text


def main(page: Page):

    main_content = Column(scroll="auto")

    for i in range(100):
        main_content.controls.append(Text(f"Line {i}"))

    page.padding = 0
    page.spacing = 0
    page.horizontal_alignment = "stretch"
    page.add(
        Container(main_content, padding=10, expand=True),
        Row([Container(Text("Footer"), bgcolor="black", padding=5, expand=True)]),
    )

    menubar = flet.MenuBar(
        expand=True,
        style=flet.MenuStyle(
            alignment=flet.alignment.top_left,
            bgcolor=flet.colors.RED_100,
            mouse_cursor={
                flet.MaterialState.HOVERED: flet.MouseCursor.WAIT,
                flet.MaterialState.DEFAULT: flet.MouseCursor.ZOOM_OUT,
            },
        ),
        controls=[
            flet.SubmenuButton(
                content=flet.Text("File"),
                # on_open=handle_on_open,
                # on_close=handle_on_close,
                # on_hover=handle_on_hover,
                controls=[
                    flet.MenuItemButton(
                        content=flet.Text("About"),
                        leading=flet.Icon(flet.icons.INFO),
                        style=flet.ButtonStyle(
                            bgcolor={
                                flet.MaterialState.HOVERED: flet.colors.GREEN_100}
                        ),
                        # on_click=handle_menu_item_click
                    ),
                    flet.MenuItemButton(
                        content=flet.Text("Save"),
                        leading=flet.Icon(flet.icons.SAVE),
                        style=flet.ButtonStyle(
                            bgcolor={
                                flet.MaterialState.HOVERED: flet.colors.GREEN_100}
                        ),
                        # on_click=handle_menu_item_click
                    ),
                    flet.MenuItemButton(
                        content=flet.Text("Quit"),
                        leading=flet.Icon(flet.icons.CLOSE),
                        style=flet.ButtonStyle(
                            bgcolor={
                                flet.MaterialState.HOVERED: flet.colors.GREEN_100}
                        ),
                        # on_click=handle_menu_item_click
                    ),
                ],
            ),
            flet.SubmenuButton(
                content=flet.Text("View"),
                # on_open=handle_on_open,
                # on_close=handle_on_close,
                # on_hover=handle_on_hover,
                controls=[
                    flet.SubmenuButton(
                        content=flet.Text("Zoom"),
                        controls=[
                            flet.MenuItemButton(
                                content=flet.Text("Magnify"),
                                leading=flet.Icon(flet.icons.ZOOM_IN),
                                close_on_click=False,
                                style=flet.ButtonStyle(
                                    bgcolor={
                                        flet.MaterialState.HOVERED: flet.colors.PURPLE_200
                                    }
                                ),
                                # on_click=handle_menu_item_click
                            ),
                            flet.MenuItemButton(
                                content=flet.Text("Minify"),
                                leading=flet.Icon(flet.icons.ZOOM_OUT),
                                close_on_click=False,
                                style=flet.ButtonStyle(
                                    bgcolor={
                                        flet.MaterialState.HOVERED: flet.colors.PURPLE_200
                                    }
                                ),
                                # on_click=handle_menu_item_click
                            ),
                        ],
                    )
                ],
            ),
        ],
    )


def main(page: Page):

    main_content = Column(scroll="auto")

    for i in range(100):
        main_content.controls.append(Text(f"Line {i}"))

    page.padding = 0
    page.spacing = 0
    page.horizontal_alignment = "stretch"
    page.add(Row(controls=[flet.MenuBar]))
    page.add(
        Container(main_content, padding=10, expand=True),
        Row([Container(Text("Footer"), bgcolor="black", padding=5, expand=True)]),
    )


flet.app(target=main, view=flet.app)
