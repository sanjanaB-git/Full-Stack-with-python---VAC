
students={
    "Abi":80, "Bob":47, "catherine":93, "Dev":65,
    "Fayan":50, "Gugan": 83, "Hema":98,
    "ihaan":38, "Jai":76, "Kavin":61
}

grades={
    "O":[], 
    "A":[],
    "B":[], 
    "C":[],
    "D":[],
    "Under pass percentage":[]
}

for key,value in students.items():

    if value > 90:
        grades["O"].append((key,value))
      
    elif value > 80:
        grades["A"].append((key,value))
        
    elif value > 70:    
        grades["B"].append((key,value))
        
    elif value > 60:
        grades["C"].append((key,value))
        
    elif value >= 50:
        grades["D"].append((key,value))
        
    else:
        grades["Under pass percentage"].append((key,value))
        
for key,value in grades.items():
    print(f"Students with Grade {key}:")
    for i in value:
        print(i[0],i[1])
    print()    
    
    
    
    
    
    
    
    
    