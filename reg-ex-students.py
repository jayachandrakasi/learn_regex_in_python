import re

nextcase = 'y'
print ("\n\n =====================START of Test case (HOW TO READ)===================\n \
=====================================================================\n\
step1: Please read SCENARIO and \n\
step2: Read Search pattern, \n\
step3: Read Main string, \n\
step4: Read Python Command to search\n\
step5: Read OUTPUT of command \n\
step6: Read Python command to find location of match\n\
step7: Read OUTPUT\n\
=====================================================================")
while (nextcase == 'y' or \
       nextcase == 'Y' or \
       nextcase == 'yes' or \
       nextcase  == 'Yes' or \
       nextcase == 'YES'):
 testcase = input ("To Test $ (dollar) Sign (Search in End of a line or before new line character) in RegEx Enter 1B \n\
 To test search all occurances of a search pattern in the end of main string, RegEx Enter 2B = \n\
 To test search mutiple Road or ROAD or Rd or road in the end of main string, RegEx Enter 2C = \n\
 To test use of ^ (caret) sign (Search in the Start of the line), Enter 2D = \n\
 To Find numbers in the String, RegEx Enter 2E = \n\
 To Find Roman numbers in the main String, RegEx enter 2F = ")

 if (testcase == '1B' or \
    testcase == '1b'):
    print ("How to use $ dollar in RegEx")
    print ("SCENARIO = Search for an address that ends with \'ROAD\' in main String")
    print ("Search pattern = r\'[R][O][A][D]$\' \nmainString = \'100 NORTH MAIN ROAD\'")
    search_pattern=r'[R][O][A][D]$'
    mainString = "100 NORTH MAIN ROAD"
    print("Python Command to find all search patters in mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ")
    print (re.findall(search_pattern, mainString))
    print("Python Command to find location of search pattern in mainString = re.search(search_pattern, mainString) = \n  (Location found) OUTPUT = ")
    print (re.search(search_pattern, mainString))
    
 elif (testcase == '2B' or \
    testcase == '2b'):
    print ("SCENARIO = Search for an address that ends with any of these strings \'Road\' or \'road\' in main String\n\
case 1. 100 NORTH MAIN Road\n\
case 2. 100 NORTH MAIN road")
    print("=================================================================================")
    
    print ("case1: \nSearch pattern = r\'[Rr]oad$\' \nmainString = \'100 NORTH MAIN Road\'")
  
    search_pattern=r'[Rr]oad$' 
    mainString = "100 NORTH MAIN Road"
    print("Python Command to find all search patters in mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ")
    print (re.findall(search_pattern, mainString))
    print("Python Command to find location of search pattern in mainString = re.search(search_pattern, mainString) = \n  (Location found) OUTPUT = ")
    print (re.search(search_pattern, mainString))
    print("=================================")
    mainString1 = "100 NORTH MAIN road"
    print("=================================")
    print ("case2: \nSearch pattern = r\'[Rr]oad$\' \nmainString1 = \'100 NORTH MAIN road\' ")
    print("Python Command to find all search patters in mainString = re.findall(search_pattern, mainString1) = \n  OUTPUT = ")
    print (re.findall(search_pattern, mainString1))
    print("Python Command to find location of search pattern in mainString = re.search(search_pattern, mainString1) = \n  (Location found) OUTPUT = ")
    print (re.search(search_pattern, mainString1))
    print("=================================")
 elif (testcase == '2C' or \
    testcase == '2c'):
    print ("SCENARIO = Search for an address that ends with any of these strings \'Road\' or \'road\' or \'ROAD\' or \'Rd\'  in main String \n\
case 1. 100 NORTH MAIN Rd\n\
case 2. 100 NORTH MAIN Road\n\
case 3. 100 NORTH MAIN ROAD\n\
case 4. 100 NORTH MAIN road")
    print("=================================================================================")
    print("=================================")
    print ("case 1.\nSearch pattern = r\'([Rr]oad|[R][O][A][D]|Rd)$\' \nmainString = \'100 NORTH MAIN Rd\'")
    search_pattern=r'([Rr]oad|[R][O][A][D]|Rd)$' 
    mainString = "100 NORTH MAIN Rd"
    print("Python Command to find all search patters in mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ")
    print (re.findall(search_pattern, mainString))
    print("Python Command to find location of search pattern in mainString = re.search(search_pattern, mainString) = \n  (Location found) OUTPUT = ")
    print (re.search(search_pattern, mainString))
    print("=================================")
    print ("case 2.\nSearch pattern = r\'([Rr]oad|[R][O][A][D]|Rd)$\' \nmainString = \'100 NORTH MAIN Road\'")
    search_pattern=r'([Rr]oad|[R][O][A][D]|Rd)$' 
    mainString = "100 NORTH MAIN Road"
    print("Python Command to find all search patters in mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ")
    print (re.findall(search_pattern, mainString))
    print("Python Command to find location of search pattern in mainString = re.search(search_pattern, mainString) = \n  (Location found) OUTPUT = ")
    print (re.search(search_pattern, mainString))
    print("=================================")

    print ("case 3.\nSearch pattern = r\'([Rr]oad|[R][O][A][D]|Rd)$\' \nmainString = \'100 NORTH MAIN ROAD\'")
    search_pattern=r'([Rr]oad|[R][O][A][D]|Rd)$' 
    mainString = "100 NORTH MAIN ROAD"
    print("Python Command to find all search patters in mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ")
    print (re.findall(search_pattern, mainString))
    print("Python Command to find location of search pattern in mainString = re.search(search_pattern, mainString) = \n  (Location found) OUTPUT = ")
    print (re.search(search_pattern, mainString))
    print("=================================")

    print ("case 4. \nSearch pattern = r\'([Rr]oad|[R][O][A][D]|Rd)$\' \nmainString = \'100 NORTH MAIN road\'")
    search_pattern=r'([Rr]oad|[R][O][A][D]|Rd)$' 
    mainString = "100 NORTH MAIN Rd"
    print("Python Command to find all search patters in mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ")
    print (re.findall(search_pattern, mainString))
    print("Python Command to find location of search pattern in mainString = re.search(search_pattern, mainString) = \n  (Location found) OUTPUT = ")
    print (re.search(search_pattern, mainString))
    print("=================================")


 elif (testcase == '2D' or \
    testcase == '2d'):
    print ("===============================================")
    print ("SCENARIO: How to use ^(caret) i.e Find matching string pattern in start of the String\n\
case1: \'Mango Fruit has many varieties namesly Benisha, Himayat, Alphonso and many more\'\n\
case2: \'mango Fruit has many varieties namesly Benisha, Himayat, Alphonso and many more\'\n")           
    print ("===============================================")
    search_pattern=r'^[Mm]ango' 
    mainString = "Indian Farmers grows 2300 varieties of Mangoes but only few varieties become famous Benisha, Himayat, Alphonso and many more"
    print (f"case 1. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
    print ('Python Command to find search patter in the starting of the mainString = = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
    print(re.findall(search_pattern, mainString))
    print("Python Command to find location of search pattern in mainString = re.search(search_pattern, mainString) = \n  (Location found) OUTPUT = ")
    print (re.search(search_pattern, mainString))
    print ("====================================")    
    mainString = "mango Fruit has many varieties namesly Benisha, Himayat, Alphonso and many more"
    print (f"case 2. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
    print ('Python Command to find search patter in the starting of the mainString = = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
    print(re.findall(search_pattern, mainString))
    print("Python Command to find location of search pattern in mainString = re.search(search_pattern, mainString) = \n  (Location found) OUTPUT = ")
    print (re.search(search_pattern, mainString))
    print ("====================================")

 elif (testcase == '2E' or \
    testcase == '2e'):
    print ("===============================================")
    print ("SCENARIO: Find numbers in the main String\n\
case1: Find all numerial numbrs in mainString = \'Margaret Alphonso lives in Street 1 and her secretary lives in street 2\'\n\
case2: Find Mobile number in mainString = \'Student Mobile = 1234567890, Address Pin= 22222\'\n\
case3: Mobile number cann't start from 0 SHOULD NOT BE FOUND in mainString = \'Student Mobile = 0234567891, Address Pin= 22222")           
    print ("===============================================")

    search_pattern=r'\d' 
    mainString = "Margaret Alphonso lives in Street 1 and her secretary lives in street 2"
    print (f"case 1. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
    print ('Python Command to find search patter in the starting of the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
    print(re.findall(search_pattern, mainString))
    print("Python Command to find location of search pattern in mainString = re.search(search_pattern, mainString) = \n  (Location found) OUTPUT = ")
    print (re.search(search_pattern, mainString))
    print ("====================================")    

    search_pattern=r'[1-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]' 
    mainString = "Student Mobile = 1234567890, Address Pin= 22222"
    print (f"case 2. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
    print ('Python Command to find search patter in the starting of the mainString = = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
    print(re.findall(search_pattern, mainString))
    print("Python Command to find location of search pattern in mainString = re.search(search_pattern, mainString) = \n  (Location found) OUTPUT = ")
    print (re.search(search_pattern, mainString))
    print ("====================================")

    search_pattern=r'[1-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]' 
    mainString = "Student Mobile = 0234567891, Address Pin= 22222"
    print (f"case 2. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
    print ('Python Command to find search patter in the starting of the mainString = = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
    print(re.findall(search_pattern, mainString))
    print("Python Command to find location of search pattern in mainString = re.search(search_pattern, mainString) = \n  (Location found) OUTPUT = ")
    print (re.search(search_pattern, mainString))
    print ("====================================")

 elif (testcase == '2F' or \
    testcase == '2f'):
    print ("===============================================")
    print ("SCENARIO: Find Roman numbers in the main String\n\
Roman Thousands are represented as : \n1000 = M or m\n 2000 = MM or mm\n 3000 = MMM or mmm\n\
case1: VALIDATE Roman Thousands in a given String \n    Valid Roman Thousands strings are \'M\' or \'MM\' or \'MMM\'\n\n\
    Roman Hundred are represented as :\n    100 = C\n\
    200 = CC\n\
    300 = CCC\n\
    400 = CD\n\
    500 = D\n\
    600 = DC\n\
    700 = DCC\n\
    800 = DCCC\n\
    900 = CM\n\
    1100 = MC\n\
    1900 = MCM\n\
    1500 = MD\n\
    3300 = MMMCCC\n\
    MCMC = no such value\n\
case2: VALIDATE Roman Hundreds in a given String \n    Valid Roman Hundred Strings are \'C\' or  \'CC\' or  \'CCC\' or  \'CD\' or  \'D\' or  \'DC\' or \'DCC\' or  \'DCCC\' or  \'CM\' or \'M\' \n\
case3: Find all Roman Thousands in given string \n ,\
    Search Patterns should recognize any given string has Roman Thousand(s).\n\
    mainString can contain any or all of these Roman characters = \'M or m or MM or mm or MMM or mmm\'\n\
case4: Find all Roman Hundreds in given mainString \n\
    Search Patterns should recognize any given mainString has any Roman hundred(s). \n\
    mainString can contain any or all of these Roman Characters \'C or CC or CCC or CD or D or DC or DCC or DCCC or CM\'\n \
case 5: Find all Roman Numerals in Tens and Ones \n\
    1940 = MCMXL\n\
    1950 = MCML\n\
    1960 = MCMLX\n\
    1980 = MCMLXXX\n\
    MCMLXXXX This should not match")       
    print ("===============================================")
    roman_numeral = 'y'
    while (roman_numeral  == 'y' or \
       roman_numeral  == 'Y' or \
       roman_numeral  == 'yes' or \
       roman_numeral  == 'Yes' or \
       roman_numeral  == 'YES'):
        num = int(input ("Enter Which Test case Number [1-5] to try =   "))
        if (num == 1): 
            search_pattern=r'^M?M?M?$' 
            mainString = "M"
            print (f"case 1a. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            print(re.findall(search_pattern, mainString))
            print ("=========")
            mainString = "MM"
            print (f"case 1b. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            print(re.findall(search_pattern, mainString))
            print ("=========")
            mainString = "MMM"
            print (f"case 1c. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            print(re.findall(search_pattern, mainString))
            print ("=========")
            print ("====================================")    
        elif (num == 2):
            search_pattern=r'^M?M?M?(CM|CD|D?C?C?C?)$' 
            mainString = "C"
            print (f"case 2a. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            print(re.findall(search_pattern, mainString))
            print ("=========")
            mainString = "CC"
            print (f"case 2b. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            print(re.findall(search_pattern, mainString))
            print ("=========")
            mainString = "CCC"
            print (f"case 2c. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            print(re.findall(search_pattern, mainString))
            print ("=========")
            mainString = "CD"
            print (f"case 2d. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            print(re.findall(search_pattern, mainString))
            print ("=========")
            mainString = "D"
            print (f"case 2e. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            print(re.findall(search_pattern, mainString))
            print ("=========")
            mainString = "DC"
            print (f"case 2f. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            print(re.findall(search_pattern, mainString))
            print ("=========")
            mainString = "DCC"
            print (f"case 2g. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            print(re.findall(search_pattern, mainString))
            print ("=========")
            mainString = "DCCC"
            print (f"case 2h. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            print(re.findall(search_pattern, mainString))
            print ("=========")
            mainString = "CM"
            print (f"case 2i. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            print(re.findall(search_pattern, mainString))
            print ("=========")
            mainString = "MC"
            print (f"case 2j. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            for match in re.finditer(search_pattern, mainString):
                s = match.start()
                e = match.end()
                print ('String match "%s" at %d:%d' % (mainString[s:e], s, e))
            print ("=========")
            mainString = "MCM"
            print (f"case 2k. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            for match in re.finditer(search_pattern, mainString):
                s = match.start()
                e = match.end()
                print ('String match "%s" at %d:%d' % (mainString[s:e], s, e))
            print ("=========")
            mainString = "MD"
            print (f"case 2l. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            for match in re.finditer(search_pattern, mainString):
                s = match.start()
                e = match.end()
                print ('String match "%s" at %d:%d' % (mainString[s:e], s, e))
            print ("=========")
            mainString = "MMMCCC"
            print (f"case 2m. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            for match in re.finditer(search_pattern, mainString):
                s = match.start()
                e = match.end()
                print ('String match "%s" at %d:%d' % (mainString[s:e], s, e))
            print ("=========")
            mainString = "MCMC"
            print (f"case 2n. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('This Pattern is NOT A VALID ROMAN HUNDREDS NUMBER mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            for match in re.finditer(search_pattern, mainString):
                s = match.start()
                e = match.end()
                print ('String match "%s" at %d:%d' % (mainString[s:e], s, e))
            print ("=========")    
            print ("====================================")
        elif (num == 3):    
            search_pattern=r'([M|m]){1,3}' 
            mainString = "Leo has One Thousand = M,  DaVinci has 2 Thousands = mm and Finocci has 3 Thousands = MmM"
            print (f"case 3. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the starting of the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            print(re.findall(search_pattern, mainString))
            print("Python Command to find location of search pattern in mainString = re.finditer(search_pattern, mainString) = \n  (Location found) OUTPUT = ")
            for match in re.finditer(search_pattern, mainString):
             s = match.start()
             e = match.end()
             print ('String match "%s" at %d:%d' % (mainString[s:e], s, e))        
            print ("====================================")    
        elif (num == 4):
            search_pattern=r'M?M?M?(CM|CD|D?C?C?C?)'
            search_pattern = r'([M|m]){1,3}|(CM|CD)|(D|DC|DCC|DCCC)'
            mainString = "Italian foot ball squad and their salaries: \n\
        Player1 Salvatore Sirigu = C\n\
        Player2 Alessandro Bastoni  = CC\n\
        Player3 Leonardo Bonucci = CCC\n\
        Player4 Giorgio Chiellini = CD\n\
        Player5 Emerson Palmieri = DC\n\
        Player6 Florenzi = DCC\n\
        Player7 Spinazzola = DCCC\n\
        Player8 Toloi = CM\n\
        Player9 Barella = D\n\
        Player10 Cristante = M"
            print (f"case 4. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find search patter in the starting of the mainString = = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            print(re.findall(search_pattern, mainString))
            print("Python Command to find location of search pattern in mainString = re.finditer(search_pattern, mainString) = \n  (Location found) OUTPUT = ")
            for match in re.finditer(search_pattern, mainString):
             s = match.start()
             e = match.end()
             print ('String match "%s" at %d:%d' % (mainString[s:e], s, e))        
            print ("====================================")
        elif(num == 5):
            search_pattern = r'^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)$'
            mainString = "MCMXL"
            print (f"case 5a. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            for match in re.finditer(search_pattern, mainString):
                s = match.start()
                e = match.end()
                print ('String match "%s" at %d:%d' % (mainString[s:e], s, e))
            print ("=========")            
            mainString = "MCML"
            print (f"case 5b. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            for match in re.finditer(search_pattern, mainString):
                s = match.start()
                e = match.end()
                print ('String match "%s" at %d:%d' % (mainString[s:e], s, e))
            print ("=========")            
            mainString = "MCMLX"
            print (f"case 5c. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            for match in re.finditer(search_pattern, mainString):
                s = match.start()
                e = match.end()
                print ('String match "%s" at %d:%d' % (mainString[s:e], s, e))
            print ("=========")            
            mainString = "MCMLXXX"
            print (f"case 5d. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python Command to find all search patter in the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            for match in re.finditer(search_pattern, mainString):
                s = match.start()
                e = match.end()
                print ('String match "%s" at %d:%d' % (mainString[s:e], s, e))
            print ("=========")            
            mainString = "MCMLXXXX"
            print (f"case 5e. \nSearch pattern = r\'{search_pattern}\' \nmainString = \'{mainString}\'")
            print ('Python SHOULD NOT DETECT THIS PATTERN in the the mainString = re.findall(search_pattern, mainString) = \n  OUTPUT = ')
            for match in re.finditer(search_pattern, mainString):
                s = match.start()
                e = match.end()
                print ('String match "%s" at %d:%d' % (mainString[s:e], s, e))
            print ("=========")            

        roman_numeral = input("To continue run next test case of Roman Numerals enter [y] or [Y] or [yes] or [Yes] or [YES]")

    
 nextcase = input("To continue run next test case enter [y] or [Y] or [yes] or [Yes] or [YES]")
quit()    