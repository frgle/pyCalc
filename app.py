import services

class Main:
    def __init__(self):
        self.welcome = "Bienvenido a la calculadora \n"
        self.question_1 = "Elige el tipo de operacion: Sumar, Restar, Multiplicar, Dividir, Modulo\n"
        self.question_2 = "Proporcione los numeros: \n"
        self.goodbye = "Este fue el resultado de la operacion: \n"
        self.question_3 = "Quieres seguir usando la calculadora?: y/n " #la input da igual, se interpretara como minuscula
    
    def start(self):
        while True:
            print(self.welcome)

            operation = input(self.question_1).lower()
            response = input(self.question_2)
            response_split = services.string_to_array(response)
            numbers = services.chars_to_numbers(response_split)

            result = services.resolve(operation, numbers) #da igual
            print(f"El resultado es: {result}")
            
            is_answer_valid = False
            finish = False
            while is_answer_valid == False:
                answer = input(self.question_3)

                if answer == "n":
                    finish = True
                    is_answer_valid = True
                    print("Cerrando calculadora")
                elif answer == "y": 
                    finish = False
                    is_answer_valid = True
                else:
                    print("Ingresa una opción válida.")

            if finish == True:
                break

main = Main()
main.start()
