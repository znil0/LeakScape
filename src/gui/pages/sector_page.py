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

    # TABLAS

    dtable_local = ft.DataTable(
        bgcolor=THEME_COLORS["primary20"],
        columns=[
            ft.DataColumn(
                label=ft.Text(
                    "Localidad",
                    font_family="DM Sans 14pt",
                    weight="bold",
                    color=THEME_COLORS["accent"],
                )
            ),
            ft.DataColumn(
                label=ft.Text(
                    "Tuberías Principales",
                    font_family="DM Sans 14pt",
                    weight="bold",
                    color=THEME_COLORS["accent"],
                )
            ),
            ft.DataColumn(
                label=ft.Text(
                    "Tuberías Secundarias",
                    font_family="DM Sans 14pt",
                    weight="bold",
                    color=THEME_COLORS["accent"],
                )
            ),
            ft.DataColumn(
                label=ft.Text(
                    "Coeficiente de Importancia",
                    font_family="DM Sans 14pt",
                    weight="bold",
                    color=THEME_COLORS["accent"],
                )
            ),
        ],
        rows=[],
        horizontal_lines=ft.BorderSide(width=1, color=THEME_COLORS["accent40"]),
        vertical_lines=ft.BorderSide(width=1, color=THEME_COLORS["accent40"]),
        margin=ft.Margin(10, 30, 10, 30),
        width=float("inf"),
    )

    def add_to_table(localidad, c_principales, c_secundarias, importancia):
        dtable_local.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Text(
                            localidad,
                            color=THEME_COLORS["text"],
                            font_family="DM Sans 14pt",
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            c_principales,
                            color=THEME_COLORS["text"],
                            font_family="DM Sans 14pt",
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            c_secundarias,
                            color=THEME_COLORS["text"],
                            font_family="DM Sans 14pt",
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            importancia,
                            color=THEME_COLORS["text"],
                            font_family="DM Sans 14pt",
                        )
                    ),
                ],
            ),
        )
        page.update()

    for i in range(0, 7):
        add_to_table('Colonia "Las Brisas"', "13", "71", f"{5 + i} (Baja importancia)")
        add_to_table('Colonia "Las Brisas"', "13", "71", f"{31 + i} (Alta importancia)")

    cover_layout = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    value=f"SECTOR S0{page.sector_index + 4}",
                    size=38,
                    weight="bold",
                    font_family="Archivo",
                    color=THEME_COLORS["accent"],
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=50),
                ft.Row(
                    controls=[
                        ft.Text(
                            value="LOCALIDADES EN EL SECTOR",
                            size=18,
                            font_family="Archivo",
                            color=THEME_COLORS["accent"],
                            weight="bold",
                        ),
                        ft.Divider(
                            expand=True, thickness=1, color=THEME_COLORS["accent40"]
                        ),
                    ]
                ),
                ft.Text(
                    value="La siguiente tabla muestra las localidades en el sector y la cantidad de tuberías que la abastecen. Se ordenan por orden de importancia según el estado de las tuberías.",
                    size=14,
                    font_family="DM Sans 14pt",
                    color=THEME_COLORS["accent"],
                ),
                dtable_local,
            ],
            height=float("inf"),
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
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
