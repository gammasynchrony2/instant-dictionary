import justpy as jp
from webapp.layout import DefaultLayout
from webapp.page import Page

class About(Page):
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        layout = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=layout)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the About Page!", classes="text-4xl m-2")
        jp.Div(a=div, text="Here's some text", classes="text-lg")
        return wp

