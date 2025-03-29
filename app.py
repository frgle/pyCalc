import services

class Main:
    def __init__(self):
        self.welcome = "Bienvenido a la calculadora"
        self.question_1 = "Elige el tipo de operacion: Sumar, Restar, Multiplicar, Dividir, Modulo\n"
        self.question_2 = "Proporcione los numeros: \n"
        self.goodbye = "Este fue el resultado de la operacion: \n"
        self.question_3 = "Quieres seguir usando la calculadora?: y/n " #la input da igual, se interpretara como minuscula
    
    def start(self):
        while True:
            print(self.welcome)

            operation = input(self.question_1).lower()

            if not services.valid_input(operation):
                println("Proporciona una operacion valida")
                continue

            numbers_string = input(self.question_2)

            if not services.valid_input(numbers_string):
                println("Proporciona una entrada valida")
                continue

            numbers_string_split = services.string_to_array(numbers_string)
            numbers = services.chars_to_numbers(numbers_string_split)
            result = services.resolve(operation, numbers) #da igual

            print(f"El resultado es: {result}")
            
            valid_answer = False
            while not valid_answer:
                answer = input(self.question_3)

                if answer == "n":
                    exit = True
                    valid_answer = True
                    print("Cerrando calculadora")
                elif answer == "y": 
                    finish = False
                    valid_answer = True
                else:
                    print("Ingresa una opción válida.")

            if finish:
                break

main = Main()
main.start()
