import justpy as jp

class Home:
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout, elevated=True, classes="bg-primary text-white")
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=layout, show_if_above=True, v_modal="left",
                            side="left", bordered=True)

        scroll_area = jp.QScrollArea(a=drawer, classes="fit")
        scroll_list = jp.QList(a=scroll_area)
        a_classes = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=scroll_list, text="Home", href="/", classes=a_classes)
        jp.Br(a=scroll_list)
        jp.A(a=scroll_list, text="Dictionary", href="/dictionary", classes=a_classes)
        jp.Br(a=scroll_list)
        jp.A(a=scroll_list, text="About", href="/about", classes=a_classes)
        jp.Br(a=scroll_list)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True,
                         icon="menu", click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")
        container =jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the Home Page!",
               classes="text-4xl m-2")

        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True