import sys
import deliveroo_pckg

if (len(sys.argv[1:]) != 6):
    print("Error missing input parameters")
    exit()
    
for index ,value in enumerate(sys.argv[1:]):
    menu=deliveroo_pckg.getColumn(index)
    resul= deliveroo_pckg.cronCalculation(index, value)
    print(f"{menu: <14}{resul}")
