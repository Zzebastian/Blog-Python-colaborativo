from reactpy import component, html, run
contador = 1

@component
def accion(texto, mensaje):
    def handle_event(event):
        global contador
        contador+=1
        print(contador)
        return html.button({"on_click": handle_event}, f"ahora vale {contador}")

    return html.button({"on_click": handle_event}, f"ahora vale {contador}")



def lazo():
    return html.div(accion(f"ahora vale {contador}", "se guardó"))
    


run(lazo)
