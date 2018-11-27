class NameEntry:
    def __init__(self,name,gender,count):
        self.name = name
        self.gender = gender
        self.count = count
    
class YearEntry:
    def __init__(self,names):
        self.entries = []
        for name_entry in names:
            self.add(name_entry)
            
    def add(self,name_entry):
        self.entries.append(name_entry)

def loadFileData(f):
    year_entry = YearEntry([]) # YearEntry() needs an argument so blank space for now
    lines = [line.strip() for line in f] # Strip whitespace from lines in file
    for line in lines:
        name,gender,count = line.split(',') # Split lines into name,gender,count
        ne = NameEntry(name,gender,int(count)) # name entry
        year_entry.add(ne)
    return year_entry

def loadAllData():
    start_year,finish_year = 1880,2016
    yr_data = dict()
    for yr in range(start_year,finish_year):
        path = 'D:\\names\\'
        filename = 'yob{}.txt'.format(yr)
        with open(path+filename,'r') as f:
            yr_data[yr] = loadFileData(f)
    return yr_data
    
    