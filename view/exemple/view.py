import flet
from flet import (
    Column,
    Container,
    ElevatedButton,
    IconButton,
    Page,
    Row,
    Slider,
    Switch,
    Text,
    alignment,
    border,
    border_radius,
    colors,
    icons,
    padding,
)


def main(page: Page):
    # set page properties
    page.title = "Model Automation"
    # page.width = 300
    # page.height = 200
    # page.window_top = 100
    # page.window_left = 100
    # page.window_always_on_top = False
    # page.window_maximized = False
    # page.window_minimized = False
    # page.window_full_screen = False
    # page.window_resizable = True
    page.horizontal_alignment = "center"
    page.vertical_alignment = "spaceBetween"

    top = Text(f"Top: {page.window_top}")
    left = Text(f"Left: {page.window_left}")
    display_width = Text(f"Width: {page.width}")
    display_height = Text(f"Height: {page.height}")

    def always_on_top_changed(e):
        page.window_always_on_top = always_on_top.value
        page.update()

    def maximize_clicked(e):
        page.window_maximized = True
        page.update()

    def minimize_clicked(e):
        page.window_minimized = True
        page.update()

    def full_screen_changed(e):
        page.window_full_screen = full_screen.value
        maximize.disabled = full_screen.value
        minimize.disabled = full_screen.value
        width.disabled = full_screen.value
        height.disabled = full_screen.value
        page.update()

    def resizable_changed(e):
        page.window_resizable = resizable.value
        maximize.disabled = not resizable.value
        minimize.disabled = not resizable.value
        width.disabled = not resizable.value
        height.disabled = not resizable.value
        page.update()

    always_on_top = Switch(
        label="Always on top", value=False, on_change=always_on_top_changed
    )

    full_screen = Switch(
        label="Full screen", value=False, on_change=full_screen_changed
    )

    resizable = Switch(label="Resizable", value=True,
                       on_change=resizable_changed)

    maximize = ElevatedButton(text="Maximize", on_click=maximize_clicked)
    minimize = ElevatedButton(text="Minimize", on_click=minimize_clicked)

    def width_changed(e):
        page.window_width = e.control.value
        window_changed(e)
        page.update()

    def height_changed(e):
        page.window_height = e.control.value
        window_changed(e)
        page.update()

    width = Slider(
        min=750,
        max=1400,
        value=page.window_width,
        on_change=width_changed,
    )

    height = Slider(
        min=500, max=900, value=page.window_height, on_change=height_changed
    )

    def update_coordinates():
        top.value = f"Top: {page.window_top}"
        leflet.value = f"Left: {page.window_left}"

    def window_changed(e):
        update_coordinates()

        display_width.value = f"Width: {page.window_width:.2f}"
        display_height.value = f"Height: {page.window_height:.2f}"
        page.update()

    def move_up(e):
        page.window_top = page.window_top - 10
        update_coordinates()
        page.update()

    def move_down(e):
        page.window_top = page.window_top + 10
        update_coordinates()
        page.update()

    def move_left(e):
        page.window_left = page.window_left - 10
        update_coordinates()
        page.update()

    def move_right(e):
        page.window_left = page.window_left + 10
        update_coordinates()
        page.update()

    def menubar():
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
        return flet.Row([menubar])

    page.on_window_event = window_changed

    # add controls on Page
    # page.add(menubar)
    page.add(

        Row(
            controls=[
                Container(
                    expand=1,
                    content=always_on_top,
                ),
                Container(expand=1,
                          alignment=alignment.center_left,
                          content=maximize
                          ),
                Container(expand=1,
                          content=full_screen
                          ),
            ],
        ),
        Row(
            alignment="spaceBetween",
            controls=[
                Column(expand=1, controls=[Text()]),
                Column(
                    expand=1,
                    controls=[
                        Container(
                            bgcolor=colors.AMBER_200,
                            width=300,
                            height=300,
                            border=border.all(1, colors.BLACK),
                            padding=padding.all(10),
                            content=Column(
                                alignment="spaceBetween",
                                controls=[
                                    Row(
                                        alignment="center",
                                        controls=[
                                            Container(
                                                bgcolor=colors.LIGHT_BLUE_500,
                                                border_radius=border_radius.all(
                                                    30),
                                                content=IconButton(
                                                    icon=icons.KEYBOARD_ARROW_UP,
                                                    on_click=move_up,
                                                ),
                                            ),
                                        ],
                                    ),
                                    Row(
                                        alignment="spaceBetween",
                                        controls=[
                                            Container(
                                                bgcolor=colors.LIGHT_BLUE_500,
                                                border_radius=border_radius.all(
                                                    30),
                                                content=IconButton(
                                                    icon=icons.KEYBOARD_ARROW_LEFT,
                                                    on_click=move_left,
                                                ),
                                            ),
                                            Container(
                                                bgcolor=colors.LIGHT_BLUE_500,
                                                border_radius=border_radius.all(
                                                    30),
                                                content=IconButton(
                                                    icon=icons.KEYBOARD_ARROW_RIGHT,
                                                    on_click=move_right,
                                                ),
                                            ),
                                        ],
                                    ),
                                    Row(
                                        alignment="center",
                                        controls=[
                                            Container(
                                                bgcolor=colors.LIGHT_BLUE_500,
                                                border_radius=border_radius.all(
                                                    30),
                                                content=IconButton(
                                                    icon=icons.KEYBOARD_ARROW_DOWN,
                                                    on_click=move_down,
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        )
                    ],
                ),
                Column(expand=1, controls=[resizable]),
            ],
        ),
        Row(
            controls=[
                Container(
                    expand=1,
                    alignment=alignment.center,
                    content=Column(
                        controls=[
                            Row(controls=[top]),
                            Row(controls=[left]),
                            Row(controls=[display_width]),
                            Row(controls=[display_height]),
                        ],
                    ),
                ),
                Container(
                    expand=1,
                    content=minimize,
                    alignment=alignment.center_left,
                ),
                Container(
                    expand=1,
                    content=Column(
                        controls=[
                            Row(controls=[Text("Width:"), width]),
                            Row(controls=[Text("Height:"), height]),
                        ]
                    ),
                ),
            ],
        ),
    )

    window_changed(None)


if __name__ == "__main__":
    app = flet.app(target=main, view=flet.AppView.WEB_BROWSER)
