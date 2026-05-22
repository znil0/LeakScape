import flet as ft
from style.colors import THEME_COLORS

COMPONENT_STYLES: dict = {
    "section_block_style": {
        "expand": True,
        # "padding": ft.Padding(30, 15, 30, 15),
        "bgcolor": THEME_COLORS["background"],
        "border_radius": ft.BorderRadius(
            top_left=20,  # esquina superior izquierda sin redondear
            top_right=20,  # esquina superior derecha sin redondear
            bottom_left=20,  # esquina inferior izquierda redondeada
            bottom_right=20,  # esquina inferior derecha redondeada
        ),
        "shadow": ft.BoxShadow(
            spread_radius=1,
            blur_radius=3,
            color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
            offset=ft.Offset(2, 4),  # Desplazamiento en x, y
        ),
        "animate": ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT),
    },
    "section_block_invisible_style": {
        "expand": True,
        # "padding": 0,
        "bgcolor": ft.Colors.TRANSPARENT,
        "animate": ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT),
    },
    "side_menu_style": {
        "width": 280,
        "padding": ft.Padding(0, 30, 30, 30),
        "bgcolor": THEME_COLORS["primary"],
        "animate": ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT),
    },
    "menu_button": {
        "width": float("inf"),
        "style": ft.ButtonStyle(
            color=THEME_COLORS["accent70"],
            bgcolor=THEME_COLORS["background"],
            # side=ft.BorderSide(1, THEME_COLORS["text"]),
            shape=ft.RoundedRectangleBorder(radius=5),
            text_style=ft.TextStyle(
                size=16,
                color=THEME_COLORS["text"],
                font_family="Archivo",
                weight="bold",
            ),
        ),
        "margin": ft.Margin(30, 6, 0, 6),
    },
    "outlined_primary_button": {
        "style": ft.ButtonStyle(
            color=THEME_COLORS["text"],
            bgcolor=THEME_COLORS["background"],
            side=ft.BorderSide(2, THEME_COLORS["text"]),
            shape=ft.RoundedRectangleBorder(radius=5),
            text_style=ft.TextStyle(
                size=16,
                color=THEME_COLORS["text"],
                font_family="DM Sans 14pt",
            ),
        )
    },
    "outlined_primary_button_disabled": {
        "style": ft.ButtonStyle(
            color=ft.Colors.with_opacity(0.5, THEME_COLORS["text"]),
            bgcolor=THEME_COLORS["primary"],
            side=ft.BorderSide(2, ft.Colors.with_opacity(0.5, THEME_COLORS["text"])),
            shape=ft.RoundedRectangleBorder(radius=5),
            text_style=ft.TextStyle(
                size=16,
                color=THEME_COLORS["text"],
                font_family="DM Sans 14pt",
            ),
        )
    },
}
