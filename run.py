import pprint
import facebook_events_scraper as fes
import firebase_admin
from firebase_admin import credentials, firestore, db
from datetime import datetime
cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://penhwonders-8818a.firebaseio.com"
        # "databaseURL": "https://penhwonders-8818a-default-rtdb.asia-southeast1.firebasedatabase.app"
    },
)

db = firestore.client()
def delete_collection(coll_ref, batch_size):
    docs = coll_ref.limit(batch_size).stream()
    deleted = 0

    for doc in docs:
        print(f'Deleting doc {doc.id} => {doc.to_dict()}')
        doc.reference.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)

driver = fes.driver("/Users/munyoudoum/Downloads/chromedriver", True)
fes.login(driver, "pavdom666@gmail.com", "oudompav6666")
driver.save_screenshot("login.png")
all_events = []
pages = [
    "https://www.facebook.com/FactoryPhnomPenh/events",
    "https://www.facebook.com/Phnomclimb/events",
    "https://www.facebook.com/Nerdnightphnompenh/events",
    "https://www.facebook.com/AmatakFitness/events",
    "https://www.facebook.com/runningbongs/events",
    "https://www.facebook.com/alchemygastro/events",
    "https://www.facebook.com/longafterdarkcambodia/events",
    "https://www.facebook.com/petanquebar/events",
    "https://www.facebook.com/topazrestaurant/events",
    "https://www.facebook.com/FarmToTablePP/events",
    "https://www.facebook.com/botanicowineandbeergarden/events",
    "https://www.facebook.com/friendsfuturesfactorykh/events",
    "https://www.facebook.com/STEMCambodia/events",
    "https://www.facebook.com/moeys.gov.kh/events",
    "https://www.facebook.com/AzurePP/events",
    "https://www.facebook.com/lanternrooftopbar.asia/events",
    "https://www.facebook.com/hardrockcafephnompenh/events",
    "https://www.facebook.com/tangocambo/events/",
    "https://www.facebook.com/TwoBirdsCraftBeer/events/",
    "https://www.facebook.com/Theboxofficephnompenh/events",
    "https://www.facebook.com/flyphnompenh/events",
    "https://www.facebook.com/sraartstudio/events",
    "https://www.facebook.com/TheMentorOfficial/events",
    "https://www.facebook.com/tworiversale/events",
    "https://www.facebook.com/BlaBlaCambodia/events",
    "https://www.facebook.com/StartupGrindPP/events",
    "https://www.facebook.com/Ubiquestphnompenh/events",
    "https://www.facebook.com/phnompenhsinging/events",
    "https://www.facebook.com/plantationurbanresortspa/events",
    "https://www.facebook.com/phnompenhmeditation1/events",
    "https://www.facebook.com/SamaiRumDistillery/events",
    "https://www.facebook.com/CeramikArtStudio/events",
    "https://www.facebook.com/backstreetbarphnompenh/events",
    "https://www.facebook.com/blockbassac/events",
    "https://www.facebook.com/margaritacocktailbar/events",
    "https://www.facebook.com/liquorsocialaffairs/events",
    "https://www.facebook.com/opccambodia/events",
    "https://www.facebook.com/AIESECinCambodia/events",
    "https://www.facebook.com/highgroundskybar/events",
    "https://www.facebook.com/PalaceGateHotelPhnomPenh/events",
    "https://www.facebook.com/SofitelPhnomPenhPhokeethra/events",
    "https://www.facebook.com/IkigaiArtsCenter/events",
    "https://www.facebook.com/cambodian.country.club/events",
    "https://www.facebook.com/crookedbrew/events",
    "https://www.facebook.com/seekersspirits/events",
    "https://www.facebook.com/MetaHousePhnomPenh/events",
    "https://www.facebook.com/Cshapefitness/events",
    "https://www.facebook.com/allfitcambodia/events",
    "https://www.facebook.com/PhnomPenhPlayers/events",
    "https://www.facebook.com/SpeakEasyTheater/events",
    "https://www.facebook.com/cloudcambodia/events",
    "https://www.facebook.com/odomfarmersmarket/events",
    "https://www.facebook.com/findmehome.digital/events",
    "https://www.facebook.com/happinessprojectcambodia/events",
    "https://www.facebook.com/KhmerProductsFairs/events/",
    "https://www.facebook.com/CoconutParkPhnomPenh/events",
    "https://www.facebook.com/SuzyTimeCafe/events",
    "https://www.facebook.com/seashortsmy/events",
]
# db.reference("events").set(all_events)
for p in pages:
    page_events = fes.events_upcoming(driver, p)
    # driver.save_screenshot("hello.png")
    print(page_events)

    all_events += page_events
# all_events=[{'_id': '591802405885118', 'hosts': ['META HOUSE'], 'title': 'Tribute to the late film composer: "Ennio" Morricone (Documentary)', 'time': '19:30 12/08/2022', 'description': "From Oscar®-winning director Giuseppe Tornatore (Cinema Paradiso), From Oscar®-winning director Giuseppe Tornatore (Cinema Paradiso), ENNIO (2021, 167 min) celebrates the life and legacy of the legendary Italian composer Ennio Morricone, who passed away on 6 July 2020.\nThe documentary retraces the life and works of the cinema’s most popular and prolific 20th century composer - who wrote over 500 scores for film & television and sold over 70 million records - from his cinema debut with Sergio Leone, to winning an Academy Award for Tarantino's The Hateful Eight in 2016.\nEnglish subs. FREE ENTRANCE.\nMeta House screens\nthe best films set in Italy\nevery Sunday, 7.30PM\n\n", 'location': 'META HOUSE', 'link': 'https://www.facebook.com/events/591802405885118', 'image': 'https://scontent.fpnh8-2.fna.fbcdn.net/v/t39.30808-6/296753431_5556170927737785_4916021944943363053_n.jpg?stp=dst-jpg_p180x540&_nc_cat=100&ccb=1-7&_nc_sid=340051&_nc_eui2=AeGPWn3Qf4HBG2cAB9vAXkBsHPIxAqf8AuIc8jECp_wC4hLXrvCRUg1zfmFYXzwOLXFdAKEx1Yjg4Qq5jM7k5ZPK&_nc_ohc=RQHF6ktkmr8AX8BRmif&_nc_pt=1&_nc_zt=23&_nc_ht=scontent.fpnh8-2.fna&oh=00_AT-CIH8uE3mneZGprJgGolxieRFAxBpKi26V6sBvwmiEFg&oe=62FA8F34', 'categories': ['Visual arts'], 'start_time': '2022-08-12T19:30:00Z', 'end_time': '2022-08-12T19:30:00Z', 'ticket': ''}, {'_id': '3234653323474927', 'hosts': ['META HOUSE'], 'title': 'Modern Chinese Cinema: A FAMILY TOUR from Hongkong to Taiwan', 'time': '19:30 14/08/2022', 'description': 'A mainland Chinese filmmaker, exiled to Hong Kong for her politically-charged work, reunites with her mother on a trip to Taiwan.\nMixing its political and personal themes with passionate urgency, A FAMILY TOUR (2018, 107 min) somehow manages to convey desperation and hopefulness simultaneously\nEnglish subs. FREE ENTRANCE.\nMeta House screens the best films set in Asia every Sunday, 7.30PM', 'location': 'META HOUSE', 'link': 'https://www.facebook.com/events/3234653323474927', 'image': 'https://scontent.fpnh8-2.fna.fbcdn.net/v/t39.30808-6/296484062_5556199801068231_7047982578010165526_n.jpg?stp=dst-jpg_p180x540&_nc_cat=108&ccb=1-7&_nc_sid=340051&_nc_eui2=AeHy8WqmfyFxU37ZCA5PlBlDTcqXlVl4MLtNypeVWXgwu5FxKbn7oz9d4JRUqScJ0NPrKmy-wK3fWc7Xv9ET84Q9&_nc_ohc=UmgxNsiluRAAX9-6C6K&_nc_pt=1&_nc_zt=23&_nc_ht=scontent.fpnh8-2.fna&oh=00_AT-8F67koXLFa03ufyliX2En77cL2kj-DHV9wxjHylL2ww&oe=62F9B7B9', 'categories': ['Visual arts'], 'start_time': '2022-08-14T19:30:00Z', 'end_time': '2022-08-14T19:30:00Z', 'ticket': ''}]
delete_collection(db.collection("events"), 100)
for e in all_events:
    db.collection("events").document(e["_id"]).set(e)


driver.close()
driver.quit()
"""
db = client.penhtest1
main = db["main"]
added_events = db["added_events"]
pages = db["facebook_pages"].find()[0]["pages"]
temp = db["temp"]
all_events = []

for p in pages:
    page_events = fes.events_upcoming(driver, p)
    driver.save_screenshot("hello.png")
    print(page_events)
    all_events += page_events
import pprint
    
for e in all_events:
    pprint.pprint(e)

try:
    time7h = datetime.now()
    added_events.delete_many(
        {"end_time": {"$lte": time7h.strftime("%Y-%m-%dT%H:%M:%SZ")}}
    )
    temp.delete_many({})
    # will have errors because it can get duplicate events from many pages
    try:
        temp.insert_many(all_events + [i for i in added_events.find()], ordered=False)
    except Exception as e:
        print("ERROR temp:", e)
    if [i for i in temp.find()]:
        main.delete_many({})
        main.insert_many([i for i in temp.find().sort("start_time", ASCENDING)])
    else:
        print("temp is empty")
except Exception as e:
    print("ERROR: ", e)

driver.close()
driver.quit()
"""
