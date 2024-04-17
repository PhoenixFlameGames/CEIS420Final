from IPython import get_ipython

class Salesman:
    def __init__(self,name,title):
        self.name = name
        self.title = title
        self.sales = []
    
    def addSale(self,sale):
        self.sales.append(sale)
        
    def iterate(self):
        return iter(self.sales)
    
    def getTotalSales(self):
        return sum(self.sales)
    
    def getMinSales(self):
        return min(self.sales)
    
    def getMaxSales(self):
        return max(self.sales)
    
    def getAverageSales(self):
        return sum(self.sales)/len(self.sales)

if __name__ == "__main__":
    salesman = []
    
    names = True
    #Enter in Sales Man
    while names:
        name = input("Enter name of salesman:")
        if not name:
            break
        
        title = input("Enter salesman title:")
        sales = []
        values = True
        
        while values:
            value = input("Enter sales value:")
            if not value:
                break
            sales.append(float(value))
            
        salesPerson = Salesman(name,title)
        for i in sales:
            salesPerson.addSale(i)
        
        salesman.append(salesPerson)
        
    #Sales Report
    get_ipython().magic('clear')
    
    for i in salesman:
        print(f"Salesman Name: {i.name}, Title: {i.title}")
        print(f"Total Sales: {Salesman.getTotalSales(i)}")
        print(f"Min Sales: {Salesman.getMinSales(i)}")
        print(f"Max Sales: {Salesman.getMaxSales(i)}")
        print(f"Average Sales: {Salesman.getAverageSales(i)}")
        print("\n")
        
    #Company Report
    totalSales = sum(i.getTotalSales() for i in salesman)
    minSales = min(i.getMinSales() for i in salesman)
    maxSales = max(i.getMaxSales() for i in salesman)
    averageSales = sum(i.getTotalSales() for i in salesman)/len(salesman)
    
    print("Company Sales Report")
    print(f"Total Company Sales {totalSales}")
    print(f"Minimum Company Sales {minSales}")
    print(f"Maximum Company Sales {maxSales}")
    print(f"Average Company Sales {averageSales}")