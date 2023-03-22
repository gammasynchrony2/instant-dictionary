import justpy as jp
from webapp.layout import DefaultLayout
from webapp.page import Page

class Home(Page):
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = DefaultLayout(a=wp)
        container =jp.QPageContainer(a=layout)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the Home Page!",
               classes="text-4xl m-2")

        return wp