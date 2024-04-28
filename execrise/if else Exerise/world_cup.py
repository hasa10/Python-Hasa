print('Point Table')
print('Pak = 7 \nNew =8 \nAfg =7')
print('There are three matches between them.')
pak_vs_nZ =input('pakistan vs New zealand match =')
pak_vs_afg =input('pakistan vs afganistan match =')
NZ_vs_afg =input('afganistan vs New zealand match =')

pak_net_rate=input('Pakistan net run rate=')
afg_net_rate=input('afganistan net run rate=')
NZ_net_rate=input('NewZealand net run rate=')
#print the

if NZ_vs_afg == "afgWon" and pak_vs_afg == "afgWon" and pak_vs_nZ == "pakWon" :    #a=9  p=8
    print("Afganistan is selected to semi")
if NZ_vs_afg == "afgWon" and pak_vs_afg == "afgWon" and pak_vs_nZ == "nZWon" :      #a=9 n=9
    if afg_net_rate >NZ_net_rate :
        print("Afganistan is selected to semi")
    else :
        print("New Zealand is selected to semi")
if NZ_vs_afg == "afgWon" and pak_vs_afg == "pakWon" and pak_vs_nZ == "pakWon" :    #a=8 p=9
    print("pakistan is selected to semi")
if NZ_vs_afg == "afgWon" and pak_vs_afg == "pakWon" and pak_vs_nZ == "nZWon" :   #a=8 p=8 n=9
    print("New zealand is selected to semi")
if NZ_vs_afg == "nZWon" and pak_vs_afg == "afgWon" and pak_vs_nZ == "pakWon" :    #n=9 a=8 p=8
    print("New zealand is selected to semi")
if NZ_vs_afg == "nZWon" and pak_vs_afg == "afgWon" and pak_vs_nZ == "nZWon" :     #n=10 a=8
    print("New Zealand is selected to semi")
if NZ_vs_afg == "nZWon" and pak_vs_afg == "pakWon" and pak_vs_nZ == "pakWon" :     #n=9 p=9
    if NZ_net_rate > pak_net_rate :
        print("New Zealand is selected to semi")
    else:
        print("pakistan is selected to semi")
    print("Afganistan is selected to semi")
if NZ_vs_afg == "nZWon" and pak_vs_afg == "pakWon" and pak_vs_nZ == "nZWon" :   #n=10 a=8
    print("New Zealand is selected to semi")
if pak_vs_nZ=="NZwon" or NZ_vs_afg=="NZwon" :
    print("new zealand is selected to semi ")
else :
    print("New zealand is not selected to semi")




