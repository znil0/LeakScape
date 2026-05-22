# PÁGINA DE MAPAS

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
                    disabled=True,
                    **COMPONENT_STYLES["menu_button_selected"],
                ),
                ft.Button(
                    "SECTOR",
                    on_click=lambda _: asyncio.create_task(page.push_route("/sector")),
                    **COMPONENT_STYLES["menu_button"],
                ),
                ft.Button(
                    "LOCALIDAD",
                    on_click=lambda _: asyncio.create_task(page.push_route("/")),
                    disabled=True,
                    **COMPONENT_STYLES["menu_button_disabled"],
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

    segmentos = []
    segmentos_img = []
    for i in range(4, 10):
        segmentos.append(
            ft.Segment(
                value=f"{i}",
                label=ft.Text(f"S. 0{i}"),
                icon=ft.Icon(ft.Icons.NUMBERS),
            )
        )
        segmentos_img.append(f"TepicSector_S0{i}.png")

    sector_image = ft.Image(
        src="TepicSector_S04.png",
        width=350,
        height=350,
        margin=ft.Margin(80, 0, 0, 0),
    )

    def sector_changed(e: ft.Event[ft.SegmentedButton]):
        op = e.control.selected[0]
        index = int(op) - 4
        sector_image.src = segmentos_img[index]
        print(segmentos_img[index])
        page.update()

    sector_button = ft.SegmentedButton(
        selected=["4"],  # Inicialmente ninguna opción seleccionada
        on_change=sector_changed,
        allow_empty_selection=True,  # Permitir que no haya ninguna selección
        allow_multiple_selection=False,  # Selección única (solo una opción)
        segments=segmentos,
    )

    cover_layout = ft.Container(
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            value="MAPA DE TEPIC",
                            size=38,
                            weight="bold",
                            font_family="Archivo",
                            color=THEME_COLORS["accent"],
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Text(
                            value="Seleccione un sector para consultar el estado de los recursos públicos de la zona.",
                            size=16,
                            font_family="DM Sans 14pt",
                            color=THEME_COLORS["accent"],
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Container(height=35),
                        ft.Container(
                            content=sector_image,
                            expand=True,
                        ),
                        ft.Container(height=35),
                        ft.Text(
                            value="Sector:",
                            size=16,
                            font_family="DM Sans 14pt",
                            color=THEME_COLORS["accent"],
                            weight="bold",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Container(height=10),
                        sector_button,
                    ],
                    height=float("inf"),
                    spacing=0,
                    scroll=ft.ScrollMode.AUTO,
                ),
                ft.Column(
                    controls=[
                        ft.Container(height=300),
                        ft.Button(
                            content="Resumen de datos y predicciones",
                            icon=ft.Icons.ARROW_FORWARD_SHARP,
                            icon_color=THEME_COLORS["accent"],
                            style=ft.ButtonStyle(
                                bgcolor=THEME_COLORS["primary"],
                                padding=10,
                                text_style=ft.TextStyle(
                                    size=16,
                                    font_family="DM Sans 14pt",
                                ),
                            ),
                            color=THEME_COLORS["accent"],
                            margin=20,
                        ),
                    ],
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                ),
            ],
            expand=True,
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
