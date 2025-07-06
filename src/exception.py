import sys 

def error_massage_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name= exc_tb.tb_frame.f_code.co_filename
    error_massage="Error occured in python script name [{0}] line number [{1}] error massage [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_massage
    

class CustomException(Exception):
    def __init__(self, error_massage,error_detail:sys):
        super().__init__(error_massage)
        self.error_massage=error_massage_detail(error_massage,error_detail=error_detail)
    
    def __str__(self):
        return self.error_massage
    
if __name__ == "__main__":
    
    try:
        a=1/0
        
    except Exception as e:
        
        raise CustomException(e,sys)
        logging.info("Divide by zero")