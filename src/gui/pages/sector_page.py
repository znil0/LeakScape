# PÁGINA PRINCIPAL

import flet as ft
import asyncio

from style.colors import THEME_COLORS
from style.component_styles import COMPONENT_STYLES


def view(page: ft.Page):
    page.controls.clear()
    page.bgcolor = THEME_COLORS["background"]

    # MENU
    # -----------------------------------------------------------------------------------------------

    menu_sidebar = ft.Container(
        content=ft.Column(
            [
                ft.Container(height=30),
                ft.Text(
                    value="MENÚ",
                    color=THEME_COLORS["text"],
                    font_family="Archivo",
                    weight="bold",
                    size=34,
                    margin=ft.Margin(30, 0, 0, 0),
                ),
                ft.Divider(
                    color=THEME_COLORS["text50"],
                ),
                ft.Container(height=20),
                ft.Button(
                    "INICIO",
                    on_click=lambda _: asyncio.create_task(page.push_route("/")),
                    **COMPONENT_STYLES["menu_button"],
                ),
                ft.Button(
                    "MAPA",
                    on_click=lambda _: asyncio.create_task(page.push_route("/map")),
                    **COMPONENT_STYLES["menu_button"],
                ),
                ft.Button(
                    "SECTOR",
                    disabled=True,
                    **COMPONENT_STYLES["menu_button_selected"],
                ),
                ft.Button(
                    "LOCALIDAD",
                    on_click=lambda _: asyncio.create_task(page.push_route("/local")),
                    **COMPONENT_STYLES["menu_button"],
                ),
                ft.Button(
                    "CERRAR",
                    **COMPONENT_STYLES["menu_button"],
                ),
            ],
            spacing=0,
            expand=True,
        ),
        **COMPONENT_STYLES["side_menu_style"],
    )

    # TÍTULO
    # -----------------------------------------------------------------------------------------------
    title_layout = ft.Container(
        content=ft.Text(
            value="LeakScape",
            color=THEME_COLORS["accent"],
            size=55,
            weight="bold",
            font_family="Jost",
        ),
        **COMPONENT_STYLES["section_block_invisible_style"],
    )

    cover_layout = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    value="Sector",
                    size=26,
                    weight="bold",
                    color=THEME_COLORS["accent"],
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=100),
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=40,
        **COMPONENT_STYLES["section_block_invisible_style"],
    )

    # ------------------------- FINAL LAYOUT --------------------------------------
    content = ft.View(
        expand=True,
        bgcolor=THEME_COLORS["background"],
        padding=0,
        controls=[
            ft.Row(
                controls=[
                    menu_sidebar,
                    cover_layout,
                ],
                spacing=0,
                expand=True,
            ),
        ],
    )

    return content
