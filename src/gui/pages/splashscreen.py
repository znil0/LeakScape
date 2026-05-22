# SPLASHSCREEN

import flet as ft
import asyncio

from style.colors import THEME_COLORS
from style.component_styles import COMPONENT_STYLES


def view(page: ft.Page):
    page.controls.clear()
    page.bgcolor = THEME_COLORS["background"]

    # TÍTULO
    # -----------------------------------------------------------------------------------------------
    title_layout = ft.Container(
        content=ft.Text(
            value="LeakScape",
            color=ft.Colors.WHITE,
            size=55,
            weight="bold",
            font_family="Jost",
        ),
        **COMPONENT_STYLES["section_block_invisible_style"],
    )

    content = ft.View(
        expand=True,
        bgcolor=THEME_COLORS["accent"],
        padding=0,
        controls=[
            ft.Column(
                controls=[
                    ft.Image(
                        src="logo.png",
                        width=150,
                        height=150,
                    ),
                    title_layout,
                ],
                spacing=0,
                expand=True,
            ),
        ],
    )

    return content
