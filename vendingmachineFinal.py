import json

class InventoryItem:
    def __init__( self, itemName ):
        self.name = itemName
        self.totalStocked = 0
        self.totalInStock = 0
        self.totalSlots = 0
  
def addToStocked( self, stockAmt ):
    self.totalStocked = self.totalStocked + stockAmt
  
def addToInStock( self, inStockAmt ):
    self.totalInStock = self.totalInStock + inStockAmt
  
def incrementSlots( self ):
    self.totalSlots = self.totalSlots + 1

def getNumberSold( self ):
    return self.totalStocked - self.totalInStock
  
def getSoldPct( self ):
    return self.getNumberSold() / self.totalStocked
  
def getStockNeed( self ):
    return 8 * self.totalSlots - self.totalInStock
  
def getName( self ):
    return self.name

def getNumberInStock( self ):
    return self.totalInStock

def __repr__( self ):
    return '{} In Stock: {}, Stocked: {}, Slots: {}'.format( self.name, self.totalInStock, self.totalStocked, self.totalSlots )
  
class Machine_status:
    def __init__(self, Machine_name):
        self.name = Machine_name
        self.previousBevStock = 0
        self.currentBevStock = 0
        self.Total_income = 0.0
  
def getPctSold(self):
    return (self.previousBevStock - self.currentBevStock) / self.previousBevStock * 100
  
def updateIncome(self, income):
    self.Total_income = self.Total_income + income
  
def updatePrevBeveragestock(self, prevBeveragestock):
    self.previousBevStock = self.previousBevStock + prevBeveragestock
  
def updateCurrentBeveragestock(self, currentBeveragestock):
    self.currentBeveragestock = self.currentBeveragestock + currentBeveragestock
  
def getName(self):
    return self.name
  
def getCurrentStock(self):
    return self.currentBevStock
  
def getPrevStock(self):
    return self.previousBevStock
  
def getTotalIncome(self):
    return self.Total_income
  
def __repr__(self):
    return "Name {}, Income {}, Sold Pct {:2f}".format(self.name, self.Total_income, self.getPctSold())
  
  
def main():
    InventoryFile_names = ["REID_1F_20171004.json", "REID_2F_20171004.json", "REID_3F_20171004.json"]
  

# amount of beverage currently stocked
Item_name_Inventory_Item = {}
Machine_status_Dictionary = {}
for inventoryFileName in InventoryFile_names:
    inventoryFile = open( inventoryFileName, 'r' )
  
Inventory_Data = json.loads( inventoryFile.read() )

Machine_name = Inventory_Data['machine_label']

Machine_status = Machine_status_Dictionary.get( Machine_name, Machine_status(Machine_name) )
  
contents = Inventory_Data['contents']
  
#seperate slots/rows for machines
for row in contents:
  for slot in row['slots']:
        itemName = slot['item_name']

Inventory_Item = Item_name_Inventory_Item.get( itemName, InventoryItem( itemName ) )
  
#update here
Inventory_Item.addToStocked( slot['last_stock'] )
Inventory_Item.addToInStock( slot['current_stock'] )
Inventory_Item.incrementSlots();
  
Machine_status.updateIncome(slot['item_price']*(slot['last_stock']-slot['current_stock']))
Machine_status.updatePrevBevStock(slot['last_stock'])
Machine_status.updateCurrentBevStock(slot['current_stock'])
  
#store results
Item_name_Inventory_Item[itemName] = Inventory_Item
Machine_status_Dictionary[Machine_name] = Machine_status

SortingDecision = input('Would you like the (m)achine report or (i)nventory report? ')
Inventory_ItemsList = list( Item_name_Inventory_Item.values() )
Machine_statusList = list(Machine_status_Dictionary.values())

if SortingDecision == 'm':
    print('{:15} {:15} {:10}'.format('Machine_Name', 'Percent Sold', 'Sales Total'))
    for item in Machine_statusList:
        print('{:10} {:10.2f}% ${:8.2f}'.format(item.getName(), item.getPctSold(), item.getTotal_income()))
elif SortingDecision == 'i':
    while SortingDecision != 'q':
        SortingDecision = input('Sort by (n)ame, (p)ct sold, (s)tocking need, or (q) to quit: ')
  
# selection to determine results
if SortingDecision == 'n':
    Inventory_ItemsList.sort( key=InventoryItem.getName )
elif SortingDecision == 'p':
    Inventory_ItemsList.sort( key=InventoryItem.getSoldPct )
    Inventory_ItemsList.reverse()
elif SortingDecision == 's':
    Inventory_ItemsList.sort( key=InventoryItem.getStockNeed )
    Inventory_ItemsList.reverse()
  
#Output the resultss
print( 'Item Name       Sold       % Sold      In Stock Stock needs')
for item in Inventory_ItemsList:
    print( '{:20} {:8} {:8.2f}% {:8} {:8}'.format( item.getName(), item.getNumberSold(), item.getSoldPct() * 100, item.getNumberInStock(), item.getStockNeed()))
print()
  
main()