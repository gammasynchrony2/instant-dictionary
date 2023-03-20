import justpy as jp

class Home:
    path = '/'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        return wp