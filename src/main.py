# SCRIPT PRINCIPAL
# Este script se encarga de enrutar las demás páginas.

import flet as ft

# Imports: Aquí se importan las páginas para su indexado.
from gui.pages.main_page import view as main_view


async def main(page: ft.Page):

    def route_change():
        page.views.clear()

        page.views.append(ft.View(route="/", controls=[]))

        ## PÁGINA PRINCIPAL
        page.views.append(main_view(page))

        ## PÁGINA DEL NCL
        if page.route == "/ncl":
            page.views.append(main_view(page))  # TODO: Poner aquí los zooms

        page.update()

    page.on_route_change = route_change
    route_change()


ft.run(main)
