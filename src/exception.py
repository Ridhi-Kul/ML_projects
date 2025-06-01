# sys: library that will have information about the errors we will handle
import sys
import logging

def error_message_detail(error, error_detail:sys): # error detail will be present inside sis
    _, _, exc_tb = error_detail.exc_info() # return type of sis gives 3 info, first 2 are irrelevant
    # Here we will get info about which file has exception occurred in, which line number, etc
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    return error_message
    
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) # inheriting the error from exception
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message
    
## Whenever using try in any module, inside catch we can raise this custom exception that we just created
    