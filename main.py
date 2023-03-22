import justpy as jp
from webapp.home import Home
from webapp.about import About
from webapp.dictionary import Dictionary
from webapp.page import Page
import inspect

imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj) and issubclass(obj, Page) and hasattr(obj, "path"):
        jp.Route(obj.path, obj.serve)

jp.justpy(port=8001)