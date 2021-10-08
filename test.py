import pandas as p
import datetime
import yfinance as y #new dependency

data = p.read_excel('List of Stocks.xlsx')
stocks=data

print(stocks)

def stock_close(stock):
    end=datetime.date.today()
    date=end-datetime.timedelta(days=90)
    stock_detail=y.Ticker(f'{stock}.NS')	#for Indian Stocks
    # stock_detail=y.Ticker(stock) 		#for Foriegn Stocks
    view=stock_detail.history(start=date,end=end)
    
    print(view['Close'])
    # for i in view:
    #     print(i)

# with open("stock_view.txt",'w') as file:
#     #modification can be done
#     file.write(view) 		#for text


# with open("stock_view.txt/xlsx",'r') as file:
#     #modification can be done
#     file.read() 

# 	print(p.read_excel('stock_view.xlsx'))
    
if __name__=="__main__":
    stock=input("Enter Symbol of Stock: ")

    stock_close(stock)