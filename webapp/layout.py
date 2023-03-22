import justpy as jp
class DefaultLayout(jp.QLayout):

    def __init__(self, view="hHh lpR fFf", **kwargs):
        super().__init__(view=view, **kwargs)

        header = jp.QHeader(a=self, elevated=True, classes=view)
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=self, show_if_above=True, v_modal="left",
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
                         icon="menu", click=self.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True