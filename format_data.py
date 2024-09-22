# Formata a data, voce recebe a data no seguinte formato: dd/MM/yyyy 
# Imprime nos formatos MM/dd/yyyy e yyyy/MM/dd

from datetime import datetime

def format_data(data_str):
    data = datetime.strptime(data_str, "%d/%m/%Y")

    format_mm_dd_yyyy = data.strftime("%m/%d/%Y")
    format_yyyy_mm_dd = data.strftime("%Y/%m/%d")

    print("Formato MM/dd/yyyy:", format_mm_dd_yyyy)
    print("Formato yyyy/MM/dd:", format_yyyy_mm_dd)

data = "25/12/2024"
format_data(data)
