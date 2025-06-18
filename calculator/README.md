
---

## 🧠 Tips prácticos y buenas prácticas

| ✅ Buenas prácticas | ✨ Detalles |
|--------------------|------------|
| **Funciones puras** | `add()`, `subtract()`... no tienen efectos secundarios |
| **Evita lógica dentro del input()** | Usa funciones como `read_number(prompt)` |
| **Tipado explícito** | Mejora autocompletado y legibilidad: `-> float` |
| **Usa `Callable` para funciones como datos** | `Callable[[float, float], float]` te permite pasar operaciones fácilmente |
| **No abuses del `try/except` global** | Maneja errores donde tengan sentido (por ejemplo, división por cero solo en `main()`) |
| **Entrada validada con bucles** | `print_menu()` se repite hasta que el usuario introduzca una opción válida |
| **Separación lógica/UI** | Las funciones de cálculo no saben nada del usuario |
| **Control de salida claro** | `if __name__ == "__main__":` te permite importar el código sin que se ejecute |
| **Diccionario de operaciones** | `OPERATIONS = {1: ("Sumar", add, "+")}` evita duplicación de código |
| **Mensajes claros para el usuario** | Muestra errores, menús y resultados con formato y separación |

---

## ⚙️ ¿Cómo funciona internamente?

- `OPERATIONS` contiene las operaciones como funciones:
  ```python
  OPERATIONS = {
      1: ("Sumar", add, "+"),
      2: ("Restar", subtract, "-"),
      3: ("Multiplicar", multiply, "*"),
      4: ("Divide", divide, "/"),
  }
- `add` `subtract` `multiply` `divide` funciones puras que reciben dos `float` y devuelven un `float`. En`divide` se lanza `ZeroDivisionError` si `b == 0`
  ```python
  def add(a: float, b: float) -> float:
    """Return *a + b*."""
    return a + b
- `MenuAction` *Type alias* de `Callable[[float, float], float]`. Indica que cualquier operación válida debe aceptar dos `float`y devolver un`float`
  ```python
  MenuAction = Callable[[float, float], float]
- `read_two_numbers` pide los dos números y permite cancelar con una letra:
  ```python
  def read_two_numbers() -> Tuple[float, float] | None:
    """Prompt the user for two numbers.  Return *None* to signal cancellation."""
    print("(Insert a letter to go back to menu)")

    first = read_number("Insert the first number: ")
    if first is None:
        return None

    second = read_number("Insert the second number: ")
    if second is None:
        return None

    return first, second
- `print_menu()` Renderiza dinámicamente el menú usando `OPERATIONS`. Valida la opción introducida en un bucle hasta recibir un número entre 0 y 4.
  ```python
  def print_menu() -> int:
    """Display the menu and return the chosen option as an *int*."""
    while True:
        print("\n------- Menu -------")
        for key, (name, _, _) in OPERATIONS.items():
            print(f"{key}. {name}")
        print("0. Exit")
        print("--------------------")

        choice = input("Type the number of your option: ")
        if choice.isdigit():
            choice_int = int(choice)
            if 0 <= choice_int <= len(OPERATIONS):
                return choice_int
        print("Option is invalid, try again…\n")
- `main` Bucle principal: muestra menú, lee números, ejecuta la operación elegida y gestiona errores (`ZeroDivisionError`). El bucle termina cuando la opción es 0.
  ```python
  def main() -> None:
    """Run the interactive calculator until the user chooses to exit."""
    while True:
        option = print_menu()
        if option == 0:
            break

        numbers = read_two_numbers()
        if numbers is None:  # user cancelled number entry
            continue

        a, b = numbers
        name, func, symbol = OPERATIONS[option]
        print(f"\n---- {name} ----")
        try:
            result = func(a, b)
        except ZeroDivisionError as exc:
            print(exc)
        else:
            print(f"{a} {symbol} {b} = {result}")

    print("Saliendo…")
- *Entry-point guard*`if __name__=="__main__":` Permite que el script se ejecute solo cuando se llama desde la terminal y no al importarlo; facilita pruebas y reutilización como módulo.
  ```python
  if __name__ == "__main__":
    main()
- `Separación lógica/UI` Las funciones de cálculo no conocen `input()` ni `print()`. Toda la interacción con el usuario reside en helpers (`read_*`, `print_menu`). Esto mejora legibilidad y testabilidad.
