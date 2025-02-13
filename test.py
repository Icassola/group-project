import argparse, json, logging, csv, re, sys, codecs
'''
floatre = re.compile("^\d+\.\d+$")
intre = re.compile("^\d+$")

def read_header(file="header.csv"):
    header=[]
    for line in open(file):
        header.append(line.strip())
    logging.info("%d lines in header", len(header))
    return header

def process_csv(file, header):
    out=[]
    stdin = file == "-"
    fd = sys.stdin if stdin else codecs.open(file, "r", "UTF-8")
    reader = csv.reader(fd)
    for nr, row in enumerate(reader):
        logging.debug("%d fields in line %d", len(row), nr)
        d = dict()
        out.append(d)
        for i, field in enumerate(row):
            if field != "NULL":
                if floatre.match(field):
                    d[header[i]] = float(field)
                elif intre.match(field):
                    d[header[i]] = int(field)
                else:
                    d[header[i]] = field
    if not stdin:
        fd.close()
    return out

if __name__ == "__main__":
    p =argparse.ArgumentParser()
    p.add_argument("raw", nargs="*", default=["-"])
    p.add_argument("--header", type=str, default="header.csv")
    p.add_argument("--debug", action="store_true")
    args = p.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.INFO)
    header = read_header(args.header)
    out = []
    for file in args.raw:
        out += process_csv(file, header)
    print(json.dumps(out, indent=4, ensure_ascii=False)) '''

with open('withyears_headers.csv', 'w', encoding="utf8", newline='') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["Year", "URI","rdf-schema#label","rdf-schema#comment","timeInSpace","wheelbase","length","width","height","weight","runtime","academicAdvisor_label","academicAdvisor","activeYearsEndDate","activeYearsEndYear","activeYearsStartDate","activeYearsStartYear","album_label","album","alias","allegiance","almaMater_label","almaMater","appointer_label","appointer","artist_label","artist","associate_label","associate","associatedAct_label","associatedAct","associatedBand_label","associatedBand","associatedMusicalArtist_label","associatedMusicalArtist","author_label","author","automobileModel","award_label","award","background","battingSide","battle_label","battle","beatifiedBy_label","beatifiedBy","beatifiedDate","beatifiedPlace_label","beatifiedPlace","bestFinish","bibsysId","billed_label","billed","birthDate","birthName","birthPlace_label","birthPlace","birthYear","block","bnfId","board_label","board","bodyDiscovered_label","bodyDiscovered","bowlRecord","bpnId","buriedPlace_label","buriedPlace","bustSize","callSign","canonizedBy_label","canonizedBy","canonizedDate","canonizedPlace_label","canonizedPlace","careerPoints","careerPrizeMoney","careerStation_label","careerStation","centuryBreaks","chairman_label","chairman","championships","chancellor_label","chancellor","child_label","child","choreographer_label","choreographer","citizenship_label","citizenship","club_label","club","coach_label","coach","coachedTeam_label","coachedTeam","coachingRecord","college_label","college","committee","commonName","configuration","country_label","country","creator_label","creator","currentMember_label","currentMember","currentPartner_label","currentPartner","currentRank","currentRecord","dateOfBurial","deathCause_label","deathCause","deathDate","deathPlace_label","deathPlace","deathYear","debut","debutTeam_label","debutTeam","depictionDescription","deputy_label","deputy","discipline_label","discipline","doctoralAdvisor_label","doctoralAdvisor","doctoralStudent_label","doctoralStudent","draft","draftPick","draftRound","draftTeam_label","draftTeam","draftYear","education_label","education","electionDate","electionMajority","employer_label","employer","endYearOfInsertion","engine_label","engine","era_label","era","espnId","ethnicity_label","ethnicity","event_label","event","eyeColor","fastestLap","feastDay","field_label","field","firstAppearance","firstRace_label","firstRace","firstWin_label","firstWin","format_label","format","formerChoreographer_label","formerChoreographer","formerCoach_label","formerCoach","formerHighschool_label","formerHighschool","formerPartner_label","formerPartner","formerTeam_label","formerTeam","garrison_label","garrison","gender_label","gender","genre_label","genre","governor_label","governor","governorGeneral_label","governorGeneral","hairColor","hallOfFame","height","heir_label","heir","highestBreak","highestRank","highschool_label","highschool","hipSize","hometown_label","hometown","honours_label","honours","incumbent_label","incumbent","individualisedGnd","influenced_label","influenced","influencedBy_label","influencedBy","institution_label","institution","instrument_label","instrument","isniId","knownFor_label","knownFor","language_label","language","lastAppearance_label","lastAppearance","lastPosition","lastRace_label","lastRace","lastWin_label","lastWin","lccnId","league_label","league","length","lieutenant_label","lieutenant","location_label","location","mainInterest_label","mainInterest","majorShrine_label","majorShrine","majorityLeader","manager_label","manager","managerClub_label","managerClub","manufacturer_label","manufacturer","mbaId","militaryBranch_label","militaryBranch","militaryCommand","militaryRank_label","militaryRank","militaryUnit_label","militaryUnit","mission_label","mission","monarch_label","monarch","movement_label","movement","mythology_label","mythology","nationalTeam_label","nationalTeam","nationality_label","nationality","network_label","network","networth","nlaId","nominee_label","nominee","notableIdea_label","notableIdea","notableStudent_label","notableStudent","notableWork_label","notableWork","number","numberBuilt","numberOfEpisodes","numberOfFilms","occupation_label","occupation","office","opponent_label","opponent","orcidId","orderInOffice","origin_label","origin","otherParty_label","otherParty","otherWins","overallRecord","parent_label","parent","partner_label","partner","party_label","party","personFunction_label","personFunction","philosophicalSchool_label","philosophicalSchool","picture_label","picture","placeOfBurial_label","placeOfBurial","plays","podiums","poles","portfolio","portrayer_label","portrayer","position_label","position","predecessor_label","predecessor","presenter_label","presenter","president_label","president","previousWork_label","previousWork","priceMoney","primeMinister_label","primeMinister","producer_label","producer","productionEndYear","productionStartYear","profession_label","profession","prospectLeague_label","prospectLeague","prospectTeam_label","prospectTeam","pseudonym","publisher_label","publisher","race_label","race","raceHorse_label","raceHorse","races","rankingWins","rating","recordDate","recordLabel_label","recordLabel","recordedIn_label","recordedIn","region_label","region","relation_label","relation","relative_label","relative","releaseDate","religion_label","religion","residence_label","residence","restingPlace_label","restingPlace","restingPlacePosition","ridId","royalAnthem_label","royalAnthem","runningMate_label","runningMate","runtime","salary","school_label","school","selection_label","selection","selibrId","seniority","series_label","series","serviceEndYear","serviceNumber","serviceStartYear","shoeNumber","shoots","significantBuilding_label","significantBuilding","significantDesign_label","significantDesign","significantProject_label","significantProject","speaker","species_label","species","spike","sport_label","sport","sportCountry_label","sportCountry","spouse_label","spouse","squadNumber","starring_label","starring","startYearOfInsertion","stateDelegate_label","stateDelegate","stateOfOrigin_label","stateOfOrigin","statisticLabel_label","statisticLabel","statisticValue","statisticYear","status","subsequentWork_label","subsequentWork","successor_label","successor","supplementalDraftRound","supplementalDraftYear","suppreddedDate","team_label","team","televisionSeries_label","televisionSeries","termPeriod_label","termPeriod","throwingSide","thumbnail_label","thumbnail","timeInSpace","title","tournamentRecord","trackNumber","trainer_label","trainer","training_label","training","transmission","type_label","type","ulanId","undraftedYear","unitCost","university_label","university","veneratedIn_label","veneratedIn","viafId","vicePresident_label","vicePresident","vicePrimeMinister_label","vicePrimeMinister","voice_label","voice","voiceType_label","voiceType","waistSize","weight","whaDraft","whaDraftTeam_label","whaDraftTeam","wheelbase","width","wikiPageDisambiguates_label","wikiPageDisambiguates","wikiPageID","wikiPageRedirects_label","wikiPageRedirects","wikiPageRevisionID","wins","winsAtAsia_label","winsAtAsia","winsAtAus_label","winsAtAus","winsAtChallenges_label","winsAtChallenges","winsAtChampionships_label","winsAtChampionships","winsAtJapan_label","winsAtJapan","winsAtLET_label","winsAtLET","winsAtLPGA_label","winsAtLPGA","winsAtMajors_label","winsAtMajors","winsAtNWIDE_label","winsAtNWIDE","winsAtOtherTournaments_label","winsAtOtherTournaments","winsAtPGA_label","winsAtPGA","winsAtProTournaments_label","winsAtProTournaments","winsInEurope_label","winsInEurope","worldChampionTitleYear","writer_label","writer","year","years","description","point","22-rdf-syntax-ns#type_label","22-rdf-syntax-ns#type","owl#sameAs_label","owl#sameAs","wgs84_pos#lat","wgs84_pos#long","core#broader_label","core#broader","core#prefLabel","core#related_label","core#related","core#subject_label","core#subject"])
    with open('withyears.csv', 'r', encoding="utf8") as incsv:
        reader = csv.reader(incsv)
        writer.writerows(row + [0.0] for row in reader)

import csv
with open('withyears_headers.csv', encoding="utf8") as withyears:
    reader = csv.DictReader(withyears)
    list_gold=[]
    list_silver=[]
    list_bronze=[]
    
    for entry in reader:
        if 'OlympicGoldMedalist' in entry["22-rdf-syntax-ns#type_label"]:
            athlete_list = []
            athlete_list.append(entry['Year'])
            athlete_list.append(entry['rdf-schema#label'])
            athlete_list.append(entry['birthPlace_label'])
            athlete_list.append(entry['nationality_label'])
            athlete_list.append(entry['description'])
            athlete_list.append(entry['22-rdf-syntax-ns#type_label'])
            athlete_list.append("Gold Medalist")
            list_gold.append(athlete_list)
            
        if 'OlympicSilverMedalist' in entry["22-rdf-syntax-ns#type_label"]:
            athlete_list = []
            athlete_list.append(entry['Year'])
            athlete_list.append(entry['rdf-schema#label'])
            athlete_list.append(entry['birthPlace_label'])
            athlete_list.append(entry['nationality_label'])
            athlete_list.append(entry['description'])
            athlete_list.append(entry['22-rdf-syntax-ns#type_label'])
            athlete_list.append("Silver Medalist")
            list_silver.append(athlete_list)
            
        if 'OlympicBronzeMedalist' in entry["22-rdf-syntax-ns#type_label"]:
            athlete_list = []
            athlete_list.append(entry['Year'])
            athlete_list.append(entry['rdf-schema#label'])
            athlete_list.append(entry['birthPlace_label'])
            athlete_list.append(entry['nationality_label'])
            athlete_list.append(entry['description'])
            athlete_list.append(entry['22-rdf-syntax-ns#type_label'])
            athlete_list.append("Bronze Medalist")
            list_bronze.append(athlete_list)
            

with open ('data_cleaned.csv', 'w', encoding="utf8", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Year', 'Name', 'Birthplace', 'Nationality', 'Sport','Labels', 'Medal'])
    for line in list_gold:
        writer.writerow(line)
    for line in list_silver:
        writer.writerow(line)
    for line in list_bronze:
        writer.writerow(line)