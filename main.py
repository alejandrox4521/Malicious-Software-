import keyboard

print("Registrando letras de (a-z) y espacios. ESC para salir.")

with open("log.txt", "w") as f:
    while True:
        e = keyboard.read_event()
        if e.event_type == keyboard.KEY_DOWN:
            if e.name == "esc":
                break
            if e.name == "space":
                f.write(" ")
            elif len(e.name) == 1 and e.name.isalpha():
                f.write(e.name)