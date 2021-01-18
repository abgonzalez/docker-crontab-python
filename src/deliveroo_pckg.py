def cronCalculation(key, value):
    if (key == 0):
        resul=readMinutes(value)
        return ' '.join(map(str,resul))
    elif (key == 1):
        resul=readHours(value)
        return ' '.join(map(str,resul))
    elif (key == 2):
        resul=readDays(value)
        return ' '.join(map(str,resul))
    elif (key == 3):
        resul=readMonths(value)
        return ' '.join(map(str,resul))
    elif (key == 4):
        resul=readDaysOfWeek(value)
        return ' '.join(map(str,resul))
    elif (key == 5):
        return value

def getColumn(i):
    menu={
                0:'minute',
                1:'hour',
                2:'day of month',
                3:'month',
                4:'day of week',
                5:'command'
             } 
    return menu.get(i,"Error")

def readMinutes(value):
    return getMinutes(getValues(value))

def getMinutes(values):
    result=[]
    if (len(values) == 1):
        start=str(values[0])
        if ( validateValue(start, 0, 59) == False):
              return list("Error")        
        #In case it is *
        if (start == "*" ):
            return list(range(0, 60))
        #In case it is a values list
        elif (start.find(",") == True):
            return list(start.split(","))
        #In case it is a values range                        
        elif (start.find("-")== True):
            ranges= list(start.split("-"))    
            for item in range(int(ranges[0]), int(ranges[1])):
                result.append(item)
            return result
        else:
            return list(start)
                                
    if (len(values) ==2):
        start = values[0]
        step = values[1]
        if ( validateValue(start, 0, 59) == False):
              return list("Error")
        if ( validateValue(step, 0, 59) == False):
              return list("Error")
         #In case it is '*'
        if (start=="*" and step == "*"):
            return list(range(0, 60))
        elif (start == "*" and step.isdigit()):
            start="0"
            for item in range(int(start), 60,int(step)):
                result.append(item)
            return result
        #In case it isn't a range, the default is 0-60                        
        elif (start.isdigit() and step.isdigit()):
            for item in range(int(start), 60,int(step)):
                result.append(item)
            return result 
        #In case it is a values list
        elif (start.find(",")== True and step.isdigit()):
            return list("Error")
        #In case it is a values range                        
        elif (start.find("-")== True and step.isdigit()):
            ranges= list(start.split("-"))                       
            for item in range(int(ranges[0]), int(ranges[1]), int(step)):
                result.append(item)
            return result   
  
    return list("Error")

def readHours(value):
    return getHours(getValues(value))

def getHours(values):
    result=[]
    if (len(values) == 1):
        start=str(values[0])
        if ( validateValue(start, 0, 23) == False):
              return list("Error")        
        #In case it is *
        if (start == "*" ):
            return list(range(0, 24))
        #In case it is a values list
        elif (start.find(",") == True):
            return list(start.split(","))
        #In case it is a values range                        
        elif (start.find("-")== True):
            ranges= list(start.split("-"))    
            for item in range(int(ranges[0]), int(ranges[1])):
                result.append(item)
            return result
        else:
            return list(start)
                                
    if (len(values) ==2):
        start = values[0]
        step = values[1]
        if ( validateValue(start, 0, 23) == False):
              return list("Error")
        if ( validateValue(step, 0, 23) == False):
              return list("Error")
         #In case it is '*'
        if (start=="*" and step == "*"):
            return list(range(0, 24))
        elif (start == "*" and step.isdigit()):
            start="0"
            for item in range(int(start), 24,int(step)):
                result.append(item)
            return result
        #In case it isn't a range, the default is 0-60                        
        elif (start.isdigit() and step.isdigit()):
            for item in range(int(start), 24,int(step)):
                result.append(item)
            return result 
        #In case it is a values list
        elif (start.find(",")== True and step.isdigit()):
            return list("Error")
        #In case it is a values range                        
        elif (start.find("-")== True and step.isdigit()):
            ranges= list(start.split("-"))                       
            for item in range(int(ranges[0]), int(ranges[1]), int(step)):
                result.append(item)
            return result   
  
    return list("Error")

def readDays(value):
    return getDays(getValues(value))

def getDays(values):
    result=[]
    if (len(values) == 1):
        start=str(values[0])
        if ( validateValue(start, 1, 31) == False):
              return list("Error")        
        #In case it is *
        if (start == "*" ):
            return list(range(1, 32))
        #In case it is a values list
        elif (start.find(",") == True):
            return list(start.split(","))
        #In case it is a values range                        
        elif (start.find("-")== True):
            ranges= list(start.split("-"))    
            for item in range(int(ranges[0]), int(ranges[1])):
                result.append(item)
            return result
        else:
            return list(start)
                                
    if (len(values) ==2):
        start = values[0]
        step = values[1]
        if ( validateValue(start, 1, 31) == False):
              return list("Error")
        if ( validateValue(step, 1, 31) == False):
              return list("Error")
         #In case it is '*'
        if (start=="*" and step == "*"):
            return list(range(1, 32))
        elif (start == "*" and step.isdigit()):
            start="1"
            for item in range(int(start), 32,int(step)):
                result.append(item)
            return result
        #In case it isn't a range, the default is 0-60                        
        elif (start.isdigit() and step.isdigit()):
            for item in range(int(start), 32,int(step)):
                result.append(item)
            return result 
        #In case it is a values list
        elif (start.find(",")== True and step.isdigit()):
            return list("Error")
        #In case it is a values range                        
        elif (start.find("-")== True and step.isdigit()):
            ranges= list(start.split("-"))                       
            for item in range(int(ranges[0]), int(ranges[1]), int(step)):
                result.append(item)
            return result   
  
    return list("Error")

def readMonths(value):
    return getMonths(getValues(value))

def getMonths(values):
    result=[]
    if (len(values) == 1):
        start=str(values[0])
        if ( validateValue(start, 1, 12) == False):
              return list("Error")        
        #In case it is *
        if (start == "*" ):
            return list(range(1, 13))
        #In case it is a values list
        elif (start.find(",") == True):
            return list(start.split(","))
        #In case it is a values range                        
        elif (start.find("-")== True):
            ranges= list(start.split("-"))    
            for item in range(int(ranges[0]), int(ranges[1])):
                result.append(item)
            return result
        else:
            return list(start)
                                
    if (len(values) ==2):
        start = values[0]
        step = values[1]
        if ( validateValue(start, 1, 12) == False):
              return list("Error")
        if ( validateValue(step, 1, 12) == False):
              return list("Error")
         #In case it is '*'
        if (start=="*" and step == "*"):
            return list(range(1, 13))
        elif (start == "*" and step.isdigit()):
            start="1"
            for item in range(int(start), 13,int(step)):
                result.append(item)
            return result
        #In case it isn't a range, the default is 0-60                        
        elif (start.isdigit() and step.isdigit()):
            for item in range(int(start), 13,int(step)):
                result.append(item)
            return result 
        #In case it is a values list
        elif (start.find(",")== True and step.isdigit()):
            return list("Error")
        #In case it is a values range                        
        elif (start.find("-")== True and step.isdigit()):
            ranges= list(start.split("-"))                       
            for item in range(int(ranges[0]), int(ranges[1]), int(step)):
                result.append(item)
            return result   
    return list("Error")

def readDaysOfWeek(value):
    return getDaysOfWeek(getValues(value))

def getDaysOfWeek(values):
    result=[]
    if (len(values) == 1):
        start=str(values[0])
        if ( validateValue(start, 0, 7) == False):
              return list("Error")        
        #In case it is *
        if (start == "*" ):
            return list(range(0, 8))
        #In case it is a values list
        elif (start.find(",") == True):
            return list(start.split(","))
        #In case it is a values range                        
        elif (start.find("-")== True):
            ranges= list(start.split("-"))    
            for item in range(int(ranges[0]), int(ranges[1])+1):
                result.append(item)
            return result
        else:
            return list(start)
        
    if (len(values) ==2):
        start = values[0]
        step = values[1]
        if ( validateValue(start, 0, 7) == False):
              return list("Error")
        if ( validateValue(step, 0, 7) == False):
              return list("Error")
         #In case it is '*'
        if (start=="*" and step == "*"):
            return list(range(0,8))
        elif (start == "*" and step.isdigit()):
            start="0"
            for item in range(int(start), 8,int(step)):
                result.append(item)
            return result
        #In case it isn't a range, the default is 0-60                        
        elif (start.isdigit() and step.isdigit()):
            for item in range(int(start), 8,int(step)):
                result.append(item)
            return result 
        #In case it is a values list
        elif (start.find(",")== True and step.isdigit()):
            return list("Error")
        #In case it is a values range                        
        elif (start.find("-")== True and step.isdigit()):
            ranges= list(start.split("-"))                       
            for item in range(int(ranges[0]), int(ranges[1])+1, int(step)):
                result.append(item)
            return result   
  
    return list("Error")

#Validate functions
def validateValue(value, min, max):
    if (value =="*"):
        return True
    if (value.isdigit() and (int(value) >= min and int(value) <= max)):
        return True
    elif (value.find(",")== True):
        ran=value.split(",")
        if ((int(ran[0]) >= min and int(ran[0]) <= max) and  (int(ran[1]) >= min and int(ran[1]) <= max)):
            return True
        else:
            return False
    elif (value.find("-")== True):
        ran=value.split("-")
        if ((int(ran[0]) >= min and int(ran[0]) <= max) and  (int(ran[1]) >= min and int(ran[1]) <= max)):
            return True
        else:
            return False
    else:
        return False    
    
def getValues(value):
    result=[]
    if (value.find('/')):
        result=value.split('/')
    return result