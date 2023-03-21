import justpy as jp

class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the About Page!", classes="text-4xl m-2")
        jp.Div(a=div, text="Here's some text", classes="text-lg")
        return wp

