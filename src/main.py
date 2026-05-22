# SCRIPT PRINCIPAL
# Este script se encarga de enrutar las demás páginas.

import flet as ft
import asyncio

# Imports: Aquí se importan las páginas para su indexado.
from gui.pages.main_page import view as main_view
from gui.pages.map_page import view as map_view
from gui.pages.sector_page import view as sector_view
from gui.pages.local_page import view as local_view
from gui.pages.splashscreen import view as splashscreen_view

sector_index = 0
local_index = 0


async def main(page: ft.Page):

    ## SPLASHSCREEN

    def route_change():
        page.views.clear()

        page.views.append(ft.View(route="/", controls=[]))

        ## PÁGINA PRINCIPAL
        page.views.append(main_view(page))

        if page.route == "/":
            page.views.append(main_view(page))

        if page.route == "/map":
            page.views.append(map_view(page))

        if page.route == "/sector":
            page.views.append(sector_view(page))

        if page.route == "/sector/desc":
            page.views.append(main_view(page))

        if page.route == "/local":
            page.views.append(local_view(page))

        if page.route == "/local/desc":
            page.views.append(main_view(page))

        page.update()

    page.on_route_change = route_change
    route_change()


ft.run(main, assets_dir="assets")
