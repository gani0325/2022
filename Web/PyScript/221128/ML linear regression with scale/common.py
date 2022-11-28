def createElementDiv(document, Element, name):
    element = document.createElement('div')
    element.id = name
    document.body.append(element)
    return Element(name)