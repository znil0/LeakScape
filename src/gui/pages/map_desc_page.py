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
                ft.Button(
                    content="Regresar",
                    icon=ft.Icons.ARROW_BACK_SHARP,
                    icon_color=THEME_COLORS["text"],
                    style=ft.ButtonStyle(
                        bgcolor=THEME_COLORS["background"],
                        padding=10,
                        text_style=ft.TextStyle(
                            size=16,
                            font_family="DM Sans 14pt",
                        ),
                    ),
                    color=THEME_COLORS["accent"],
                    margin=20,
                    on_click=lambda _: asyncio.create_task(page.push_route("/map")),
                ),
            ]
        ),
        **COMPONENT_STYLES["side_menu_style"],
    )

    # TABLAS

    dtable_principal = ft.DataTable(
        bgcolor=THEME_COLORS["primary20"],
        columns=[
            ft.DataColumn(
                label=ft.Text(
                    "Ubicación",
                    font_family="DM Sans 14pt",
                    weight="bold",
                    color=THEME_COLORS["accent"],
                )
            ),
            ft.DataColumn(
                label=ft.Text(
                    "Última reparación",
                    font_family="DM Sans 14pt",
                    weight="bold",
                    color=THEME_COLORS["accent"],
                )
            ),
            ft.DataColumn(
                label=ft.Text(
                    "Estado",
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

    def add_to_principal(ubicacion, ultima_reparacion, estado):
        dtable_principal.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Text(
                            ubicacion,
                            color=THEME_COLORS["text"],
                            font_family="DM Sans 14pt",
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            ultima_reparacion,
                            color=THEME_COLORS["text"],
                            font_family="DM Sans 14pt",
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            estado,
                            color=THEME_COLORS["text"],
                            font_family="DM Sans 14pt",
                        )
                    ),
                ],
            ),
        )
        page.update()

    dtable_secundario = ft.DataTable(
        bgcolor=THEME_COLORS["primary20"],
        columns=[
            ft.DataColumn(
                label=ft.Text(
                    "Ubicación",
                    font_family="DM Sans 14pt",
                    weight="bold",
                    color=THEME_COLORS["accent"],
                )
            ),
            ft.DataColumn(
                label=ft.Text(
                    "Última reparación",
                    font_family="DM Sans 14pt",
                    weight="bold",
                    color=THEME_COLORS["accent"],
                )
            ),
            ft.DataColumn(
                label=ft.Text(
                    "Estado",
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

    def add_to_secundario(ubicacion, ultima_reparacion, estado):
        dtable_secundario.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Text(
                            ubicacion,
                            color=THEME_COLORS["text"],
                            font_family="DM Sans 14pt",
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            ultima_reparacion,
                            color=THEME_COLORS["text"],
                            font_family="DM Sans 14pt",
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            estado,
                            color=THEME_COLORS["text"],
                            font_family="DM Sans 14pt",
                        )
                    ),
                ],
            ),
        )
        page.update()

    for i in range(0, 15):
        add_to_principal(
            "Calle Lebesgue", f"Miércoles, {i} Mayo 2026, 05:{i + 10}", "Sin desgaste"
        )

        add_to_secundario(
            "Calle Timbuktu", f"Jueves, {i} Mayo 2026, 05:{i + 10}", "Desgaste leve"
        )

    sector_title = f"Sector S0{page.sector_index + 4}"

    cover_layout = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    value=sector_title,
                    size=38,
                    weight="bold",
                    font_family="Archivo",
                    color=THEME_COLORS["accent"],
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    value="En esta sección puede consultar los datos recabados y una proyección del tiempo de vida esperado de los recursos.",
                    size=16,
                    font_family="DM Sans 14pt",
                    color=THEME_COLORS["accent"],
                ),
                ft.Container(height=35),
                ft.Row(
                    controls=[
                        ft.Text(
                            value="ABASTECIMIENTO DE AGUA",
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
                    value="Según los datos recopilados, se tiene la siguiente información respecto a la condición de los recursos relacionados con el abastecimiento de agua.",
                    size=14,
                    font_family="DM Sans 14pt",
                    color=THEME_COLORS["accent"],
                ),
                ft.Container(height=50),
                ft.Text(
                    value="Tuberías Principales",
                    size=22,
                    font_family="DM Sans 14pt",
                    color=THEME_COLORS["accent"],
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    value="Las tuberías primarias son aquellas que traen el agua desde lugares lejamos y surten a la ciudad. Son las más importantes y requieren de mantenimiento continuo.",
                    size=14,
                    font_family="DM Sans 14pt",
                    color=THEME_COLORS["accent"],
                ),
                dtable_principal,
                ft.Container(height=50),
                ft.Text(
                    value="Tuberías Secundarias",
                    size=22,
                    font_family="DM Sans 14pt",
                    color=THEME_COLORS["accent"],
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    value="Las tuberías secundarias son aquellas que se encargan de distribuir al agua que llega de las tuberías primarias a sitios localizados.",
                    size=14,
                    font_family="DM Sans 14pt",
                    color=THEME_COLORS["accent"],
                ),
                dtable_secundario,
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
