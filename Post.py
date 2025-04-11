import tweepy
import time
import os

# Function to clear the terminal screen with error handling
def clear_screen():
    try:
        # For Windows
        if os.name == 'nt':
            _ = os.system('cls')
        # For Mac and Linux
        else:
            _ = os.system('clear')
    except Exception as e:
        print(f"Failed to clear screen: {e}")
    time.sleep(0.1)  # Small delay to ensure terminal refreshes

# Replace with your X API credentials (kept for reference, though not used here)
consumer_key = 'H0KGcwlRnHfWDhPrFmEXOEjRI'
consumer_secret = '8Ho6tub7rssfYzYKUoZdpCh26dCjKn7IFTnqfd7M8REST7eTpy'
access_token = '1813999087709986817-IXAIPEoRoRUjkYEKEnOKTV3nottoyw'
access_token_secret = 'k5xcdJSvkh3bPSDxAf7E5RcL06ZCx0kyB9aP99qVFa1NC'

# Authenticate with X API (for reference)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Complete list of handles
handles = [
    'POTUS', 'VP', 'SpeakerJohnson', 'SenSchumer', 'LeaderMcConnell', 'RepJeffries', 'SecState', 'SecDef', 'SecTreasury', 'SenWarren',
    'SenSanders', 'RepAOC', 'RepMTG', 'SenRubio', 'SenCruz', 'RepNancyMace', 'SenBooker', 'SenGillibrand', 'RepJimJordan', 'RepMaxineWaters',
    'SenMittRomney', 'SenManchin', 'RepCoriBush', 'RepBoebert', 'SenHawleyPress', 'SenTimScott', 'RepMattGaetz', 'RepRashida', 'SenRickScott',
    'SenJohnKennedy', 'RepAndyBiggsAZ', 'SenMikeLee', 'RepThomasMassie', 'SenRandPaul', 'RepChipRoy', 'SenBillCassidy', 'RepDanCrenshaw',
    'SenTomCotton', 'RepGregSteube', 'SenCoryGardner', 'RepKevinMcCarthy', 'SenPatToomey', 'RepJamesComer', 'SenChrisCoons', 'RepByronDonalds',
    'SenMarkKelly', 'RepRoKhanna', 'SenRonJohnson', 'RepMikeJohnson', 'SenSherrodBrown', 'RepEliotEngel', 'SenDickDurbin', 'RepStenyHoyer',
    'SenKamalaHarris', 'RepJerryNadler', 'SenPattyMurray', 'RepAdamSchiff', 'SenTammyBaldwin', 'RepPramila', 'SenJackyRosen', 'RepTedLieu',
    'SenBenSasse', 'RepSteveScalise', 'SenChrisMurphy', 'RepDavidScott', 'SenTinaSmith', 'RepEricSwalwell', 'SenThomTillis', 'RepMarkTakano',
    'SenJonTester', 'RepTimWalberg', 'SenElizabethWarren', 'RepPeteAguilar', 'SenSheldonWhitehouse', 'RepAlGreen', 'SenRogerWicker',
    'RepAnnWagner', 'SenCoryBooker', 'RepValDemings', 'SenMikeBraun', 'RepLaurenBoebert', 'SenJohnBoozman', 'RepKatCammack', 'SenShelleyCapito',
    'RepMikeCarey', 'SenBobCasey', 'RepTonyCardenas', 'SenBillCassidy', 'RepJudyChu', 'SenChrisCoons', 'RepEmanuelCleaver', 'SenSusanCollins',
    'RepGerryConnolly', 'SenJohnCornyn', 'RepJoeCourtney', 'SenKevinCramer', 'RepRickCrawford', 'SenMikeCrapo', 'RepCharlieCrist', 'SenTedCruz',
    'RepJasonCrow', 'SenSteveDaines', 'RepDianaDeGette', 'SenTammyDuckworth', 'RepDebbieDingell', 'SenJoniErnst', 'RepVeronicaEscobar',
    'SenDebFischer', 'RepBrianFitzpatrick', 'SenJeffFlake', 'RepJeffFortenberry', 'SenLindseyGraham', 'RepGarretGraves', 'SenChuckGrassley',
    'RepSamGraves', 'SenMaggieHassan', 'RepJoshHarder', 'SenMartinHeinrich', 'RepJaimeHerrera', 'SenJohnHickenlooper', 'RepFrenchHill',
    'SenCindyHydeSmith', 'RepAshleyHinson', 'SenJimInhofe', 'RepSaraJacobs', 'SenRonJohnson', 'RepDustyJohnson', 'SenMikeLee', 'RepTeresaLeger',
    'SenBenLujan', 'RepElaineLuria', 'SenCynthiaLummis', 'RepStephenLynch', 'SenJoeManchin', 'RepTomMalinowski', 'SenEdMarkey', 'RepRogerMarshall',
    'SenMitchMcConnell', 'RepGregoryMeeks', 'SenBobMenendez', 'RepGraceMeng', 'SenJeffMerkley', 'RepJoeMorelle', 'SenJerryMoran', 'RepSethMoulton',
    'SenLisaMurkowski', 'RepJerroldNadler', 'SenChrisMurphy', 'RepStephanieMurphy', 'SenRandPaul', 'RepNancyPelosi', 'SenGaryPeters', 'RepDeanPhillips',
    'SenRobPortman', 'RepKatiePorter', 'SenJackReed', 'RepTomReed', 'SenJeanneShaheen', 'RepMikieSherrill', 'SenKyrstenSinema', 'RepElissaSlotkin',
    'SenTinaSmith', 'RepJasonSmith', 'SenDebbieStabenow', 'RepMichelleSteel', 'SenDanSullivan', 'RepDarrenSoto', 'SenJonTester', 'RepBennieThompson',
    'SenJohnThune', 'RepMikeTurner', 'SenMarkWarner', 'RepBruceWesterman', 'SenRaphaelWarnock', 'RepJenniferWexton', 'SenSheldonWhitehouse',
    'RepSusanWild', 'SenRogerWicker', 'RepRobWittman', 'SenToddYoung', 'RepDonYoung', 'SenMariaCantwell', 'RepAndreCarson', 'SenTomCarper',
    'RepEarlCarter', 'SenBenCardin', 'RepMikeCollins', 'SenMikeRounds', 'RepDavidRouzer', 'SenMarcoRubio', 'RepBobbyRush', 'SenBernieSanders',
    'RepJohnSarbanes', 'SenBrianSchatz', 'RepSteveScalise', 'SenChuckSchumer', 'RepDavidScott', 'SenRickScott', 'RepBobbyScott', 'SenTimScott',
    'RepTerriSewell', 'SenJeanneShaheen', 'RepBradSherman', 'SenKyrstenSinema', 'RepMikieSherrill', 'RepAdrianSmith', 'SenTinaSmith', 'RepChrisSmith',
    'RepJasonSmith', 'SenDebbieStabenow', 'RepEliseStefanik', 'RepBryanSteil', 'RepGregSteube', 'RepHaleyStevens', 'RepChrisStewart', 'SenSteveStivers',
    'RepTomSuozzi', 'SenDanSullivan', 'RepEricSwalwell', 'RepMarkTakano', 'SenJonTester', 'RepBennieThompson', 'SenMikeThune', 'RepMikeTurner',
    'SenChrisVanHollen', 'RepJuanVargas', 'SenMarkWarner', 'RepMaxineWaters', 'SenElizabethWarren', 'RepBonnieWatson', 'SenRaphaelWarnock',
    'RepJenniferWexton', 'RepSusanWild', 'SenRonWyden', 'RepLeeZeldin'
]

link = 'https://shorturl.at/ulOqA'

# Function to generate a tweet with as many handles as fit under 280 chars
def generate_tweet_with_max_handles(handles_list, start_index):
    base = f"See : {link}"
    tweet = base
    used_handles = []
    remaining_handles = handles_list[start_index:]

    for handle in remaining_handles:
        test_tweet = f"{tweet} @{handle}"
        if len(test_tweet) <= 280:
            tweet = test_tweet
            used_handles.append(handle)
        else:
            break
    
    return tweet, len(used_handles)

# Loop through handles, pack max handles into each tweet, pause for input
def send_max_handle_tweets():
    index = 0
    first_iteration = True
    while index < len(handles):
        if not first_iteration:
            clear_screen()  # Clear screen before each new tweet except the first one
        tweet, handles_used = generate_tweet_with_max_handles(handles, index)
        print(tweet)
        #print("\nCopy the above tweet, send it manually, then press Enter to continue...")
        input()  # Wait for user to press Enter
        index += handles_used
        first_iteration = False
    clear_screen()  # Clear screen one last time
    print("All handles processed!")
    print("[Program finished]")

if __name__ == "__main__":
    send_max_handle_tweets()
