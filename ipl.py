from PIL import Image
img = Image.open('ipl.jpg')

#Get basic details about the image

#show the image
img.show()
from pydub import AudioSegment
from pydub.playback import play
song = AudioSegment.from_mp3("IPL.mp3")
play(song)


      

print("********************* THIS IS MADE BY HARSH RANA *****************\n")
print("********** NMASKAR AAPKA SWAGAT HAI HMARE PROGRAM MAI JISKA NAAM HAI HOME OF CRICKET ***********\n")
print("\n")
def team(list):
	list=['RCB','DC','CSK','RR','KKR','PUNJAB','HYDERABAD','MUMBAI']
	return list

def player(list):
	list=['VIRAT','ROHIT','DHONI','KANE WILLAMSON','SMITH']
	return list

def schedule(list):
	list=['INDIA','AUSTRALIA','NEWZELAND','ENGLAND','PAKISTAN']
	return list

def ranking(list):
	list=['ODI','T20','TEST']
	return list

print(" 1. ******* agar aap team ke bare mai janana chate hai to press 'T' ********* \n")
print(" 2. ******* agar aap player ke bare mai janna chate hai to press 'P' ****************\n")
print(" 3. ******* agar aap kisi team ka schedule dekhna chate hai to press 'S'**************\n ")
print(" 4. ******* agar aap ranking dekna chate hai to press 'R' ***************\n")

while True:
	choice =input("TO KYA KARNA CHAIYENGE AAP   JALDI SELECT KARO IAM BORE")
	print("\n")

	if choice == 'T':
		print("this is a list of team  ",team(list))
		n=input("enter the team name")
		print("\n")
		if n=='RCB':
			img = Image.open('rcb.jpg')
			img.show()

			print("kholi is the captain of ",n,"team ",)
			print("\n")
			print("list of MATCHES \n **************")
			print(" MATCHES", " WON ", " LOSE ","    TIE "    , " POINT ")
			print(   '  14  ', '  9 ', '   4   ','      1  '  ,   ' 18 ' )
			print("\n")
			print("PLAYING 11 OF RCB TEAM \n ")
			print('VIRAT KHOLI','C  ')
			print('AB DEVILIERS','BAT ')
			print('PARTHIV PATEL','WK')
			print('MOEEN ALI','ALL ROUNDER')
			print('STOINIS','BAT')
			print('CHAHAL','BOW')
			print('SOUTHEE','BOW')
			print('SIRAZ','BOW')
			print('MANDEEP','BAT')
			print('SARFRAZ','BAT')
			print('NAVDEEP SANI','BOW')
			print("\n")
			print(" ********  THIS TEAM IS NOT WON THE IPL TROPHY BUT PLAY TO 2 TIME FINAL 2010,2016 ************ ")
			print("\n")
		

		elif n=='DC':
			img = Image.open('dc.jpg')
			img.show()
			print("SHREYAS is the captain of ",n,"team ")
			print("\n")
			print("list of MATCHES \n ***************")
			print("MATCHES", " WON ", " LOSE ","    TIE " , " POINT ")
			print('  14   ', '  12  ', '  2  ','     0  ' , '   24  ')
			print("\n")
			print("PLAYING 11 OF DC TEAM  ")
			print('IYYER','C')
			print('SHIKHAR','BAT')
			print('RISABH PANT','WK')
			print('MORRIS','ALL ROUNDER')
			print('BOULT','BOW')
			print('COLIN INGRAM','BAT')
			print('ISHANT SHARMA','BOW')
			print('RAHUL','ALL ROUNDER')
			print('RAHERFORD','ALL ROUNDER')
			print('KEMO PAUL','ALL ROUNDER')
			print('RABADA','BOW')
			print("\n")
			print(" ********** THIS TEAM IS NOT WON THE IPL TROPHY ******* ")
			print("\n")


		elif n=='CSK':
			img = Image.open('csk.jpg')
			img.show()
			print("DHONI is the captain of ",n,"team  ")
			print("\n")
			print("list of MATCHES \n ****************")
			print("MATCHES", " WON ", " LOSE ","    TIE " , " POINT ")
			print('  14   ', '  13  ', '  1  ','     0  ' , '   26  ')
			print("\n")
			print("PLAYING 11 OF CSK TEAM ")
			print('DHONI','WC')
			print('WATSON','BAT')
			print('FAF DU PLESSIS')    
			print('JADEJA','ALL ROUNDER')
			print('DEEPAK','BOW')
			print('JADAHAV','BAT')
			print('HARBAZAN','BOW')
			print('IMRAN THAIR','BOW')
			print('RAYADU','BAT')
			print('NGIDI','BOW')
			print('RAINA','BAT')
			print("\n")
			print(" *********  THIS TEAM IS WON 3 TIME IPL TROPHY 2010,2013,2018 AND PLAY THE 5 TIME IPL FINAL ************ ")
			print("\n")

		elif n=='RR':
			img = Image.open('rr.jpg')
			img.show()
			print("RAHANE is the captain of ",n,"team ")
			print("\n")
			print("list of MATCHES \n *****************")
			print("MATCHES", " WON ", " LOSE ","    TIE " , " POINT ")
			print('  14   ', '  7  ', '  6  ','       1  ' , '   14  ')
			print("\n")
			print("PLAYING 11 OF RR TEAM  ")
			print('RAHANE','C')
			print('BUTTLER','BAT')
			print('SAMSON','WK')
			print('STOKES','ALL ROUNDER')
			print('JOFRA','BOW')
			print('GOUTHAM','ALL ROUNDER')
			print('GOPAL','BOW')
			print('SMITH','BAT')
			print('RIYAN PRAG','BAT')
			print('KULKARNI','BOW')
			print('THOMAS','BOW')
			print("\n")
			print(" ********* THIS TEAM IS WON 1ST IPL TROPHY IN 2008  ************ ")
			print("\n")

		elif n=='KKR':
			img = Image.open('kkr.jpg')
			img.show()
			print("DINESH is the captain of ",n,"team  ")
			print("\n")
			print("list of MATCHES \n ********************")
			print("MATCHES", " WON ", " LOSE ","    TIE " , " POINT ")
			print('  14   ', '  11  ', '  3  ','     0  ' , '   22  ')
			print("\n")
			print("PLAYING 11 OF KKR TEAM ")
			print('DINESH','WC')
			print('LYNN','BAT')
			print('ROBIN','BAT')
			print('NARINE','ALL ROUNDER')
			print('KULDEEP','BOW')
			print('FERGUSON','BOW')
			print('NITISH RANA','BAT')
			print('RUSSEL','ALL ROUNDER')
			print('KRISHNA','BOW')
			print('CHAWALA','BOW')
			print('VINAY KUMAR','BOW')
			print("\n")
			print(" **************  THIS TEAM IS WON 2 TIME IPL TROPHY 2012, 2014 ************** ")
			print("\n")

		elif n=='PUNJAB':
			img = Image.open('kxip.jpg')
			img.show()
			print("RAHUL is the captain of ",n,"team ",)
			print("\n")
			print("list of MATCHES \n **************")
			print(" MATCHES", " WON ", " LOSE ","    TIE "    , " POINT ")
			print(   '  14  ', '  9 ', '   4   ','      1  '  ,   ' 18 ' )
			print("\n")
			print("PLAYING 11 OF PUNJAB TEAM \n ")
			print('LOKESH RAHUL','C  ')
			print('CHRIS GAYLE','BAT ')
			print('SARFRAZ','WK')
			print('SAM CURREN','ALL ROUNDER')
			print('MILLER','BAT')
			print('RAHAMAN','BOW')
			print('ANKIT','BOW')
			print('ASWIN','BOW')
			print('MANDEEP','BAT')
			print('MAYANK','BAT')
			print('FINCH','BOW')
			print("\n")
			print(" ********  THIS TEAM IS NOT WON THE IPL TROPHY BUT PLAY 1 TIME FINAL 2014 AGAINST KKR ************ ")
			print("\n")

		elif n=='HYDERABAD':
			img = Image.open('srh.jpg')
			img.show()
			print("DAVID WARNER is the captain of ",n,"team ",)
			print("\n")
			print("list of MATCHES \n **************")
			print(" MATCHES", " WON ", " LOSE ","    TIE "    , " POINT ")
			print(   '  14  ', '  9 ', '   4   ','      1  '  ,   ' 18 ' )
			print("\n")
			print("PLAYING 11 OF HYDERABAD TEAM \n ")
			print('DAVID WARNER','C  ')
			print('WILLAMSON','BAT ')
			print('BAIRSTOW','WK')
			print('YUSUF PATHAN','ALL ROUNDER')
			print('MANISH PANDEY','BAT')
			print('BHUVNESHWAR','BOW')
			print('RASHID KHAN','BOW')
			print('MOHHAMAD NABI','BOW')
			print('WRIDDIHMAN SHAH','BAT')
			print('DEEPAK HODDA','BAT')
			print('VIJAY SHANAKR','BOW')
			print("\n")
			print(" ********  THIS TEAM IS  WON THE IPL TROPHY IN 2016 AND GOING TO 2018 FINAL AGAINST CSK************ ")
			print("\n")

		elif n=='MUMBAI':
			img = Image.open('mumbai.jpg')
			img.show()
			print(" ROHIT SHARMA is the captain of ",n,"team ",)
			print("\n")
			print("list of MATCHES \n **************")
			print(" MATCHES", " WON ", " LOSE ","    TIE "    , " POINT ")
			print(   '  14  ', '  9 ', '   4   ','      1  '  ,   ' 18 ' )
			print("\n")
			print("PLAYING 11 OF MUMBAI TEAM \n ")
			print('ROHIT SHARMA','C  ')
			print('DECOCK','BAT ')
			print('ISHAN KISAN ','WK')
			print('HARDIK PANDYA','ALL ROUNDER')
			print('SURYAKUMAR','BAT')
			print('BHUMHRA','BOW')
			print('MARKNDE','BOW')
			print('MALINGA','BOW')
			print('POLLARD','BAT')
			print('KRUNAL','BAT')
			print('MECHLENGAN','BOW')
			print("\n")
			print(" ********  THIS TEAM IS  WON THE IPL TROPHY 4 TIME 2013,2015,2017,2019 **************** ")
			print("\n")

		else:
			print("unknown")
	

	elif choice == 'P':
		print("this is a list of player",player(list))
		n=input("enter the player name")
		if n=='VIRAT':
			img = Image.open('virat.jpg')
			img.show()
			song = AudioSegment.from_mp3("Virat.mp3")
			play (song)

			print("\n")
			print("*******  VIRAT IS A CAPTAIN OF INDIAN CRICKET TEAM &&&& CAPTAIN OF RCB TEAM  *********")
			print("\n")
			print(" **********ALL DETAILS OF VIRAT KHOLI *********")
			print("\n")
			print("Virat Kohli is an Indian cricketer who currently captains the India national team")
			print("A right-handed top-order batsman, Kohli is regarded as one of the best batsmen in the world")
			print("He plays for Royal Challengers Bangalore in the Indian Premier League, and has been the team's captain since 2013")
			print("\n")
			print("Born: 5 November 1988 (age 31 years), Delhi")
			print("    HEIGHT=1.75m")
			print("ODI debut : 18 August 2008 v Sri Lanka")
			print("Test debut : 20 June 2011 v West Indies")
			print("Last ODI: 11 February 2020 v New Zealand")
			print("T20I debut : 12 June 2010 v Zimbabwe")
			print("\n")
         
            
			print("********  MATCHES LIST OF VIRAT RUN MACHINE KHOLI    *******************")
			print("\n")
			print('      [MATCHES',       'ODI','    T20',        'TEST]         ')
			print('      [  460  ',       '248' ,    '82 ',        ' 86]         ')
			print('      [ RUNS' ,        '11867',  '2794',       ' 7240]        ')
			print('      [ BEST SCORE',   '183',     '92',         '254]         ')
			print('      [ 100/50',      '43/58',   '0/24',       '27/22]        ')
			print('      [ AVERAGE',     '59.34',   '51.22',      '53.43]        ')
			print('      [ RANKING',       '1',       '6',          '2]          ')



		elif n=='ROHIT':
			img = Image.open('rohit.jpg')
			img.show()
			song = AudioSegment.from_mp3("rohit.mp3")
			play (song)

			print("\n")
			print("*******  ROHIT IS A VISE CAPTAIN OF INDIAN CRICKET TEAM &&&& CAPTAIN OF MUMBAI TEAM  *********")
			print("\n")
			
			print("********** ALL DETAILS OF ROHIT SHARMA ********")
			print("\n")
			print("Rohit Gurunath Sharma is an Indian international cricketer who plays for Mumbai in domestic cricket and captains Mumbai Indians in the Indian Premier League")
			print(" as a right-handed batsman and an occasional right-arm off break bowler")
			print(" He is the vice-captain of the Indian national team in limited-overs formats")
			print("\n")
			print("Born: 30 April 1987 (age 33 years), Nagpur")
			print("ODI debut : 23 June 2007 v Ireland")
			print("Test debut : 6 November 2013 v West Indies")
			print("Last ODI: 19 January 2020 v Australia")
			print("T20I debut : 19 September 2007 v England")
			print("Last T20I: 2 February 2020 v New Zealand")
			print("\n")
			print("**********    MATCHES LIST OF ROHIT SHARAM  ***********")
			print("\n")
			print('      [MATCHES',       'ODI','    T20',        'TEST]         ')
			print('      [  460  ',       '248' ,    '82 ',        ' 86]         ')
			print('      [ RUNS' ,        '11867',  '2794',       ' 7240]        ')
			print('      [ BEST SCORE',   '183',     '92',         '254]         ')
			print('      [ 100/50',      '43/58',   '0/24',       '27/22]        ')
			print('      [ AVERAGE',     '59.34',   '51.22',      '53.43]        ')
			print('      [ RANKING',       '1',       '6',          '2]          ')


			

		elif n=='DHONI':
			img = Image.open('dhoni.jpg')
			img.show()
			song = AudioSegment.from_mp3("aakash.mp3")
			play (song)
			print("\n")
			print("*******  DHONI IS A EX CAPTAIN OF INDIAN CRICKET TEAM &&&& CAPTAIN OF CHENNAI TEAM  *********")
			print("\n")
			print("***********  MATCHES LIST OF MAHENDER SINGH DHONI  **********")
			print("\n")
			print('      [MATCHES',       'ODI','    T20',        'TEST]         ')
			print('      [  460  ',       '248' ,    '82 ',        ' 86]         ')
			print('      [ RUNS' ,        '11867',  '2794',       ' 7240]        ')
			print('      [ BEST SCORE',   '183',     '92',         '254]         ')
			print('      [ 100/50',      '43/58',   '0/24',       '27/22]        ')
			print('      [ AVERAGE',     '59.34',   '51.22',      '53.43]        ')
			print('      [ RANKING',       '1',       '6',          '2]          ')

			

		elif n=='KANE WILLAMSON':
			img = Image.open('willamson.jpg')
			img.show()
			print("\n")
			print("*******  KANE IS A  CAPTAIN OF NEWZELAND CRICKET TEAM &&&& CAPTAIN OF HYDERABAD TEAM  *********")
			print("\n")
			print("***********  MATCHES LIST OF KANE WILLAMSON  **********")
			print("\n")
			print('      [MATCHES',       'ODI','    T20',        'TEST]         ')
			print('      [  460  ',       '248' ,    '82 ',        ' 86]         ')
			print('      [ RUNS' ,        '11867',  '2794',       ' 7240]        ')
			print('      [ BEST SCORE',   '183',     '92',         '254]         ')
			print('      [ 100/50',      '43/58',   '0/24',       '27/22]        ')
			print('      [ AVERAGE',     '59.34',   '51.22',      '53.43]        ')
			print('      [ RANKING',       '1',       '6',          '2]          ')


		elif n=='SMITH':
			img = Image.open('smith.jpg')
			img.show()
			print("\n")
			print("*******  SMITH IS A EX CAPTAIN OF AUSTRALIA CRICKET TEAM &&&& CAPTAIN OF RAJASTHAN ROYALS TEAM  *********")
			print("\n")
			print("***********  MATCHES LIST OF STEVE SMITH  **********")
			print("\n")
			print('      [MATCHES',       'ODI','    T20'              ,'TEST]         ')
			print('      [  460  ',       '248' ,    '82 '              ,' 86]         ')
			print('      [ RUNS' ,        '11867',  '2794'             ,' 7240]        ')
			print('      [ BEST SCORE',   '183',     '92'               ,'254]         ')
			print('      [ 100/50',      '43/58',   '0/24'             ,'27/22]        ')
			print('      [ AVERAGE',     '59.34',   '51.22'            ,'53.43]        ')
			print('      [ RANKING',       '1',       '6'                ,'2]          ')


            
   
		else:
			print("INVALID PLAYER")


	elif choice =='S':
		print("WELCOME TO SCHEDULE DATA OF A TEAM")
		print("SELECTING THE TEAM")
		print("THIS IS A LIST OF TEAM",schedule(list))
		n=input("enter the team name")
		if n=='INDIA':
			img = Image.open('india.jpg')
			img.show()
			print("***** ISME  AAPKO ALL FORMAT MATCH KA SCHEDULE DEKHNE KO MILEGA ****************")
			print("\n")
			print("INDIA TOUR OF AUSTRALIA")
			print('1.ODI MATCH')
			print("\n")
			print('SUN 10 OCT 1.30PM')
			print('VENUE -----BRISBANE')
			print("\n")
			print('2.ODI MATCH')
			print("\n")
			print('WED 13 OCT 1.30PM')
			print('VENUE -----ADILADE')
			print("\n")
			print('3.ODI MATCH')
			print("\n")
			print('SAT 16 OCT 1.40PM')
			print('VENUE -----SYDENY')
			print("\n")
			print('4.ODI MATCH')
			print("\n")
			print('MON 18 OCT 1.30PM')
			print('VENUE -----MELBURNE')
			print("\n")
			print('5.ODI MATCH')
			print("\n")
			print('THUR 21 OCT 1.30PM')
			print('VENUE -----PERTH')
			print("\n")

		elif n=='AUSTRALIA':
			img = Image.open('aus.jpg')
			img.show()
			print("\n")
			print("AUSTRALIA TOUR OF ENGLAND")
			print('1.TEST MATCH')
			print("\n")
			print('SUN 10 OCT 1.30PM')
			print('VENUE -----MANCHASTER')
			print("\n")
			print('2.TEST MATCH')
			print("\n")
			print('WED 13 OCT 1.30PM')
			print('VENUE -----LEEDS')
			print("\n")
			print('3.TEST MATCH')
			print("\n")
			print('SAT 16 OCT 1.30PM')
			print('VENUE -----LONDON')
			print("\n")
			print('4.TEST MATCH')
			print("\n")
			print('MON 18 OCT 1.30PM')
			print('VENUE -----SOUTHHAMPTON')
			print("\n")
			print('5.TEST MATCH')
			print("\n")
			print('THUR 21 OCT 1.30PM')
			print('VENUE -----BRISTOL')
			print("\n")

		elif n=='NEWZELAND':
			img = Image.open('new.jpg')
			img.show()
			print("\n")
			print("NEWZELAND TOUR OF BANGLADESH")
			print('1.ODI MATCH')
			print("\n")
			print('SUN 10 OCT 1.30PM')
			print('VENUE -----DHAKA')
			print("\n")
			print('2.ODI MATCH')
			print("\n")
			print('WED 13 OCT 1.30PM')
			print('VENUE -----COLOMBO')
			print("\n")
			print('3.ODI MATCH')
			print("\n")
			print('SAT 16 OCT 1.30PM')
			print('VENUE -----COLOMBO')
			print("\n")
			print('4.ODI MATCH')
			print("\n")
			print('MON 18 OCT 1.30PM')
			print('VENUE -----DHAKA')
			print("\n")
			print('5.ODI MATCH')
			print("\n")
			print('THUR 21 OCT 1.30PM')
			print('VENUE -----YYSAL')
			print("\n")

		elif n=='ENGLAND':
			img = Image.open('eng.jpg')
			img.show()
			print("\n")
			print("AFRICA TOUR OF ENGLAND")
			print('1.T20 MATCH')
			print("\n")
			print('SUN 10 OCT 1.30PM')
			print('VENUE -----MANCHASTER')
			print("\n")
			print('2.T20 MATCH')
			print("\n")
			print('WED 13 OCT 1.30PM')
			print('VENUE -----LEEDS')
			print("\n")
			print('3.T20 MATCH')
			print("\n")
			print('SAT 16 OCT 1.30PM')
			print('VENUE -----LONDON')
			print("\n")
			print('4.T20 MATCH')
			print("\n")
			print('MON 18 OCT 1.30PM')
			print('VENUE -----SOUTHHAMPTON')
			print("\n")
			print('5.T20 MATCH')
			print("\n")
			print('THUR 21 OCT 1.30PM')
			print('VENUE -----BRISTOL')
			print("\n")

		elif n=='PAKISTAN':
			img = Image.open('pak.jpg')
			img.show()
			print("\n")
			print("ZIMBABE TOUR OF PAKISTAN")
			print('1.ODI MATCH')
			print("\n")
			print('SUN 10 OCT 1.30PM')
			print('VENUE -----KARACHI')
			print("\n")
			print('2.ODI MATCH')
			print("\n")
			print('WED 13 OCT 1.30PM')
			print('VENUE -----RAWALPINDI')
			print("\n")
			print('3.ODI MATCH')
			print("\n")
			print('SAT 16 OCT 1.30PM')
			print('VENUE -----ISLMABAD')
			print("\n")
			print('4.ODI MATCH')
			print("\n")
			print('MON 18 OCT 1.30PM')
			print('VENUE -----KARACHI')
			print("\n")
			print('5.ODI MATCH')
			print("\n")
			print('THUR 21 OCT 1.30PM')
			print('VENUE -----ISLMABAD')
			print("\n")
	
		else:
			Print("CHOOSE INVALID TEAM")

	elif choice=='R':
		print("ICC Cricket Rankings - Men's Batting")
		print(ranking(list))
		n=input("CHOOSE 1 ODI BATTING RANKING,T20 RANKING OR TEST RANKING---")
		if n=='ODI':
			print("***** WELCOME TO THE ODI RANKING ********")
			print("\n")
			print('POSITION',         'PLAYER',                'RATING'                     , 'COUNTRY'       )
			print('    1.',          ' VIRAT ',                '869'                        ,' INDIA'         )
			print('    2.',          ' ROHIT',                ' 855'                        ,' INDIA'         )
			print('    3.',          ' BABAR',                ' 829'                        ,' PAKISTAN'      )
			print('    4.',          ' TAYOLR',                '828'                        ,' NEWZELAND'     )
			print('    5.',          ' DUPLESI',               '791'                        ,' SOUTH AFRICA'  )
			print('    6.',          ' WARNER',                '781'                        ,' AUSTRALIA'     )
			print('    7.',          ' KANE',                  '773'                        ,' NEWZELAND '    )
			print('    8.',          ' JOEROOT',               '770',                        ' ENGLAND'       )
			print('    9.',          ' FINCH',                 '758'                        ,' AUSTRALIA'     )
			print('   10.',          ' DE COCK',               '754'                        ,' SOUTH AFRICA'  )
			print('   11.',          ' J ROY',                ' 753'                        ,' ENGLAND'       )


		elif n=='T20':
			print("***** WELCOME TO THE T20 RANKING ********")
			print("\n")
			print('POSITION',         'PLAYER',                'RATING'                     , 'COUNTRY'       )
			print('    1.',          ' BABAR ',                '879'                        ,' PAKISTAN'      )
			print('    2.',          ' RAHUL',                ' 823'                        ,' INDIA'         )
			print('    3.',          ' FINCH',                ' 820'                        ,' AUSTRALIA'     )
			print('    4.',          ' MUNRO',                ' 785'                        ,' NEWZELAND'     )
			print('    5.',          ' MAXWELL',               '721'                        ,'AUSTRALIA'      )
			print('    6.',          ' MALAN',                ' 718'                        ,' ENGLAND'       )
			print('    7.',          ' MORGAN',                '687'                       'ENGLAND '         )
			print('    8.',          ' HAZRAT',               ' 676',                        ' AFGANISTAN'    )
			print('    9.',          ' LEWIS',                 '674'                        ,'WESTINDIES'     )
			print('   10.',          ' VIRAT',               '  673'                        ,'  INDIA'        )
			print('   11.',          ' ROHIT',                ' 662'                        , 'INDIA'         )


		elif n=='TEST':
			print("***** WELCOME TO THE TEST RANKING ********")
			print("\n")
			print('POSITION',         'PLAYER',                'RATING'                     , 'COUNTRY'        )
			print('    1.',          ' SMITH ',                '911'                        ,' AUSTRALIA'      )
			print('    2.',          ' KHOLI',                 '886'                        ,' INDIA'          )
			print('    3.',          ' LABU',                  '827'                        ,' AUSTRALIA'      )
			print('    4.',          ' KANE',                  '813'                        ,' NEWZELAND'      )
			print('    5.',          ' BABAR',                 '800'                        ,'PAKISTAN'        )
			print('    6.',          ' WARNER',                '793'                        ,' AUSTRALIA'      )
			print('    7.',          ' PUJARA',                '766'                          'INDIA'          )
			print('    8.',          ' JOEROOT',               '764',                         ' ENGLAND'       )
			print('    9.',          ' RAHANE',                '726'                          ,'INDIA'         )
			print('   10.',          ' STOKES',                '718'                         ,'ENGLAND'        )
			print('   11.',          ' MAYANK',                '714'                         , 'INDIA'         )




			

		else:
			print("invalid")


	else:
		print("invalid operation")

