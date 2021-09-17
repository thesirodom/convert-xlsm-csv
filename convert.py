import pandas as pd
import time
import glob

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"Function {func.__name__!r} executed in {(end-start):.4f}s")
        return result
    return wrapper
        
@timer        
def convert_excel_csv():
    for f in glob.glob("*"):
        if f.endswith(".xlsm"):
            f_name = f.split('.xlsm')[0]
            read_file = pd.read_excel (f'{f_name}.xlsm')
            read_file.to_csv (f'{f_name}.csv', index = None, header=True)          

if __name__ == "__main__":
    convert_excel_csv()