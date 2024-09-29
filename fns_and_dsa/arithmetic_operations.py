


def perform_operation(operation, num1, num2): #function definition
  #body

  result = 'Invalid'
   
  match operation: #(+ * - /)

    case 'add':
      return num1 + num2
      
    
    case 'subtract':
      return num1 - num2

    case 'multiply':
      return num1 * num2
    
    case 'divide':

      if num2 == 0:
        print("You cannot divide by zero.")
        return Null
      
      else:
        return num1 / num2

    case _:
      print('Invalid operation')
      return Null



