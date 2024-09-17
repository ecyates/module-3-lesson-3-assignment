# Task 1: Flight Route Comparison 

# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
# You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# 1. Destinations that both airlines fly to.
# 2. Destinations unique to your airline.
# 3. Whether there are any destinations that neither airline shares.

def unique_destinations(my_destinations, *competitors_destinations):
    '''This function takes my airline's list of destinations plus any number of competitors' lists of destinations 
    and displays how many are unique to my list of destinations (against each competitor provided).'''
    try:
        if not isinstance(my_destinations, set):
            raise ValueError
        index = 1
        # Iterate over each competitor
        for competitor in competitors_destinations:
            # Raise error if not given a set.
            if not isinstance(competitor, set):
                raise ValueError
            else:
                # Capture the difference between my list of destinations and the competitor's
                unique = my_destinations.difference(competitor)
                # Print user-friendly version of the list
                print(f"Against Competitor #{index}, my unique destinations include: {", ".join(sorted(unique))}. \n\nTotal Unique Destinations: {len(unique)}\n")
                index += 1
    except ValueError:
        print("Invalid input. Please only input sets.\n")

def overall_unique(my_destinations, *competitors_destinations):
    '''This function takes my airline's list of destinations plus any number of competitors' lists of destinations 
    and displays how many are unique to my list of destinations overall.'''
    try:
        if not isinstance(my_destinations, set):
            raise ValueError()
        else:
            unique = my_destinations
            # Iterate over each competitor
            for competitor in competitors_destinations:
                # Raise error if not given a set.
                if not isinstance(competitor, set):
                    raise ValueError
                else:
                    # Capture the difference between my list of destinations and the competitor's
                    unique = unique.difference(competitor)
    except ValueError:
        print("Invalid input. Please only input sets.\n")
    else:
        # Print user-friendly version of the list
        print(f"These are the destinations completely unique to my airline: {", ".join(sorted(unique))}. \n\nTotal Unique Destinations: {len(unique)}\n")


def shared_destinations(my_destinations, *competitors_destinations):
    '''This function takes my airline's list of destinations plus any number of competitors' lists of destinations 
    and displays how many are share with the competitor (against each competitor provided).'''
    try:
        if not isinstance(my_destinations, set):
            raise ValueError
        index = 1
        # Iterate over each competitor
        for competitor in competitors_destinations:
            # Raise error if not given a set
            if not isinstance(competitor, set):
                raise ValueError
            else:
                # Capture the intersection between my list of destinations and the competitor's
                shared = my_destinations.intersection(competitor)
                # Print user-friendly version of the list 
                print(f"With Competitor #{index}, our shared destinations include: {", ".join(sorted(shared))}. \n\nTotal Shared Destinations: {len(shared)}\n")
                index += 1
    except ValueError:
        print("Invalid input. Please only input sets.\n")

def unshared_destinations(my_destinations, *competitors_destinations):
    '''This function takes my airline's list of destinations plus any number of competitors' lists of destinations 
    and displays how many are unique to my list of destinations and unique to the competitor (against each competitor provided).'''
    try:
        if not isinstance(my_destinations, set):
            raise ValueError
        index = 1
        # Iterate over each competitor
        for competitor in competitors_destinations:
            # Raise error if not given a set
            if not isinstance(competitor, set):
                raise ValueError
            else:
                # Capture the symmetric difference between my list of destinations and the competitor's
                unshared = my_destinations.symmetric_difference(competitor)
                # Print the user-friendly version of the list
                print(f"Against Competitor #{index}, destinations that neither airline shares include: {", ".join(sorted(unshared))}. \n\nTotal Unique Destinations for Both Airlines: {len(unshared)}\n")
                index += 1
    except ValueError:
        print("Invalid input. Please only input sets.\n")

def main():
    import random
    try:
        # Here's a list of all international airports (according to Wikipedia)
        all_destinations = "AAC, AAE, AAL, AAN, AAQ, AAR, ABA, ABB, ABD, ABJ, ABQ, ABV, ABZ, ACA, ACC, ACE, ACH, ACI, ACY, ADA, ADB, ADD, ADE, ADL, ADU, ADZ, AEP, AER, AES, AEY, AGA, AGP, AGT, AGU, AHB, AHO, AJA, AJF, AJK, AJU, AKC, AKL, AKX, ALA, ALB, ALC, ALG, ALP, ALY, AMD, AMM, AMS, ANC, ANF, ANR, ANU, AOI, AOJ, AOK, AOR, APL, APW, AQJ, AQP, ARH, ARK, ARN, ARW, ASB, ASF, ASM, ASR, ASU, ASW, ATH, ATL, ATQ, ATR, ATW, ATZ, AUA, AUH, AUS, AVP, AWZ, AXA, AXM, AXT, AYJ, AYT, AZA, AZD, AZN, AZS, BAH, BAQ, BAV, BAX, BAY, BBI, BBK, BBU, BCM, BCN, BDA, BDE, BDL, BDQ, BDS, BEF, BEG, BEL, BEN, BER, BES, BEW, BEY, BFI, BFN, BFS, BGA, BGF, BGI, BGO, BGR, BGW, BGY, BHD, BHK, BHM, BHV, BHX, BHY, BIA, BIO, BIQ, BJA, BJL, BJM, BJV, BJX, BKI, BKK, BKO, BLI, BLJ, BLL, BLQ, BLR, BLZ, BMA, BME, BNA, BND, BNE, BNX, BOC, BOD, BOG, BOH, BOI, BOJ, BOM, BON, BOO, BOS, BOY, BPE, BPN, BQN, BQS, BRC, BRE, BRI, BRN, BRO, BRQ, BRS, BRU, BRX, BSA, BSB, BSK, BSL, BSL, BSR, BTC, BTH, BTJ, BTK, BTS, BUD, BUF, BUN, BUQ, BUS, BUZ, BVA, BVB, BVC, BWA, BWI, BWK, BWN, BYJ, BZE, BZG, BZK, BZR, BZV, CAE, CAG, CAI, CAN, CAP, CAY, CBB, CBQ, CBR, CCC, CCF, CCJ, CCK, CCP, CCS, CCU, CCZ, CDG, CDT, CEB, CEE, CEI, CEK, CFG, CFK, CFU, CGB, CGH, CGK, CGN, CGO, CGP, CGQ, CGR, CHC, CHQ, CHS, CIA, CIT, CIW, CIX, CJB, CJJ, CJU, CKG, CKY, CLE, CLJ, CLO, CLT, CMB, CME, CMF, CMH, CMN, CMW, CND, CNF, CNN, CNQ, CNS, CNX, COK, COO, COR, CPH, CPT, CRA, CRD, CRK, CRL, CRP, CRZ, CSX, CSY, CTA, CTG, CTS, CTU, CUC, CUE, CUF, CUL, CUN, CUR, CUU, CUZ, CVG, CWB, CWC, CWL, CXI, CXL, CXR, CYB, CYO, CZL, CZM, CZU, CZX, DAC, DAD, DAM, DAR, DAT, DAU, DAV, DAY, DBB, DBV, DCA, DDG, DEB, DEL, DEN, DFW, DGO, DIE, DIL, DIR, DIY, DJE, DJJ, DLA, DLC, DLH, DLM, DMB, DME, DMK, DMM, DNH, DNK, DNR, DNZ, DOH, DOM, DPS, DRP, DRW, DSM, DSN, DSS, DTM, DTW, DUB, DUD, DUR, DUS, DVO, DWC, DXB, DYG, DYR, DYU, DZA, EAM, EBB, EBL, EBU, ECN, ECP, EDI, EDL, EFL, EGC, EGO, EGS, EIN, EIS, ELH, ELP, ELQ, ELS, EMA, ENH, ENU, EPA, EPU, EQS, ERI, ESB, ESL, ESM, ETM, ETR, EUN, EUX, EVN, EWR, EXT, EYP, EYW, EZE, EZS, FAE, FAI, FAO, FAT, FBM, FCO, FDF, FDH, FEG, FEZ, FIH, FKB, FKI, FLA, FLL, FLN, FLR, FMA, FMM, FNA, FNC, FNI, FNJ, FOC, FOR, FPO, FRA, FRS, FRU, FRW, FSC, FSP, FSZ, FTE, FTU, FUE, FUK, FUN, FUT, GAN, GAU, GAY, GBB, GBE, GBT, GBY, GCI, GCM, GDL, GDN, GDX, GEG, GEO, GES, GGR, GGT, GHV, GIB, GIG, GIZ, GJL, GLA, GME, GMP, GNA, GNB, GND, GOA, GOH, GOI, GOJ, GOM, GOT, GOX, GPT, GRB, GRO, GRQ, GRR, GRU, GRV, GRX, GRZ, GSM, GSO, GSV, GUA, GUM, GUW, GVA, GWD, GXF, GYD, GYE, GYN, GYY, GZP, GZT, HAH, HAJ, HAK, HAM, HAN, HAQ, HAS, HAU, HAV, HBA, HBE, HDM, HDY, HEA, HEK, HEL, HER, HET, HFA, HFE, HGA, HGH, HGU, HHN, HIA, HID, HIJ, HIR, HKD, HKG, HKT, HLD, HLE, HLP, HMB, HMO, HND, HNL, HOF, HOG, HOU, HPH, HRB, HRE, HRG, HRI, HRK, HSK, HSV, HTA, HUI, HUN, HUX, HUY, HYD, HZO, IAD, IAG, IAH, IAR, IAS, IBE, IBZ, ICN, IDR, IEV, IFN, IFO, IGR, IGU, IIL, IKA, IKT, IKU, ILD, ILM, ILO, ILZ, IMF, INC, IND, INH, INI, INL, INN, INU, INV, IOM, IPC, IPH, IPI, ISB, ISM, IST, ISU, ITO, IUE, IXA, IXB, IXE, IXM, IXR, JAF, JAI, JAN, JAV, JAX, JCL, JED, JER, JFK, JHB, JHG, JIB, JJN, JKH, JMK, JMU, JNB, JNU, JPA, JRO, JSI, JTR, JUB, JUJ, JWR, KAC, KAN, KAO, KBL, KBP, KBR, KBV, KCH, KDH, KEF, KER, KFZ, KGD, KGF, KGL, KGS, KHH, KHI, KHN, KHV, KIH, KIJ, KIN, KIR, KIS, KIV, KIX, KJA, KJT, KKJ, KLO, KLU, KLV, KLX, KMG, KMQ, KMS, KMU, KNO, KOA, KOJ, KOS, KOV, KOW, KQT, KRK, KRR, KRS, KRT, KRW, KSA, KSC, KSH, KSN, KSQ, KSU, KTM, KTN, KTT, KTW, KUA, KUF, KUL, KUN, KUO, KUT, KVA, KVD, KVO, KWA, KWE, KWG, KWI, KWL, KXK, KYA, KZN, KZO, KZR, LAD, LAL, LAN, LAO, LAS, LAX, LBA, LBB, LBC, LBD, LBJ, LBU, LBV, LCA, LCE, LCG, LCJ, LCK, LCY, LDY, LED, LEI, LEJ, LET, LFM, LFW, LGA, LGG, LGK, LGW, LHE, LHR, LHW, LIG, LIL, LIM, LIN, LIR, LIS, LIT, LJG, LJU, LKE, LKO, LLA, LLC, LLK, LLW, LNZ, LOP, LOS, LPA, LPB, LPL, LPP, LPQ, LRH, LRM, LRR, LSZ, LTK, LTN, LTO, LUG, LUM, LUN, LUX, LUZ, LVI, LWN, LWO, LXA, LXR, LYA, LYG, LYI, LYP, LYS, MAA, MAD, MAF, MAH, MAJ, MAK, MAN, MAO, MAR, MBA, MBJ, MBX, MCI, MCJ, MCO, MCT, MCX, MCY, MCZ, MDC, MDE, MDG, MDL, MDQ, MDT, MDW, MDZ, MEC, MED, MEL, MEM, MEX, MFM, MFU, MGA, MGQ, MHD, MHH, MHQ, MIA, MID, MIR, MJI, MJN, MJT, MKE, MLA, MLB, MLE, MLM, MLX, MME, MMK, MMX, MNI, MNL, MPM, MPN, MQF, MQP, MRS, MRU, MRV, MSP, MSQ, MST, MSU, MSY, MTR, MTY, MUB, MUC, MUH, MUX, MVB, MVD, MVP, MWX, MWZ, MXL, MXP, MXZ, MYP, MYR, MZL, MZR, MZT, NAG, NAJ, NAL, NAN, NAP, NAS, NAT, NAV, NBC, NBE, NBO, NCE, NCL, NCU, NDB, NDG, NDJ, NDR, NGB, NGO, NGS, NIM, NJC, NJF, NKC, NKG, NLA, NLK, NLV, NMA, NMF, NNG, NOC, NOS, NOU, NOZ, NQN, NQY, NQZ, NRK, NRN, NRT, NSI, NTE, NTG, NTL, NUE, NVA, NVI, NWI, NYI, NYO, NYT, NZH, OAK, OAX, ODS, OGZ, OHD, OHS, OIT, OKA, OKC, OKJ, OLB, OMA, OMH, OMO, OMR, OMS, ONQ, ONT, OOL, OPO, ORD, ORF, ORK, ORN, ORY, OSD, OSI, OSL, OSM, OSR, OSS, OST, OSW, OTP, OUA, OUD, OUL, OVB, OVD, OXB, OZH, PAC, PAE, PAP, PBC, PBH, PBI, PBM, PDG, PDL, PDP, PDV, PDX, PED, PEE, PEG, PEI, PEK, PEN, PER, PES, PEW, PFO, PGF, PGU, PHC, PHE, PHF, PHL, PHX, PIE, PIK, PIS, PIT, PKC, PKR, PKU, PKV, PKX, PKZ, PLQ, PLS, PLV, PLX, PMC, PMF, PMI, PMO, PNA, PNH, PNI, PNQ, PNR, PNS, PNZ, POA, POG, POL, POM, POP, POS, POW, POZ, PPG, PPK, PPN, PPS, PPT, PQC, PRG, PRN, PSA, PSO, PSP, PSR, PSS, PTG, PTP, PUF, PUJ, PUQ, PUS, PUY, PVA, PVD, PVG, PVH, PVK, PVR, PVS, PWM, PWQ, PXM, PXO, PZU, PZY, QGY, QPJ, QRO, QSF, RAC, RAI, RAK, RAR, RAS, RBA, RBR, RCH, RDO, RDU, RDZ, REC, REL, REN, REP, RES, REU, REX, RFD, RGA, RGL, RGN, RHD, RHO, RIC, RIH, RIX, RJK, RKT, RKV, RLO, RMF, RMI, RML, RMQ, RMU, RNI, RNO, ROB, ROC, ROP, ROR, ROS, ROV, RSD, RST, RSW, RTB, RTM, RUA, RUH, RUN, RVN, RVY, RYK, RZE, SAB, SAH, SAL, SAN, SAP, SAT, SAV, SAW, SBD, SBH, SBM, SBZ, SCL, SCO, SCQ, SCT, SCU, SCV, SCW, SDD, SDF, SDJ, SDL, SDQ, SDR, SDU, SEA, SEB, SEN, SEZ, SFA, SFB, SFJ, SFO, SFS, SGC, SGN, SHA, SHE, SHJ, SHO, SID, SIN, SIP, SJC, SJD, SJJ, SJO, SJU, SJW, SKB, SKD, SKG, SKO, SKP, SKT, SKU, SKV, SLA, SLC, SLL, SLP, SLW, SLZ, SMF, SMI, SMR, SNA, SNN, SNU, SOB, SOF, SON, SOU, SPC, SPN, SPU, SPX, SQQ, SRQ, SRY, SSA, SSG, SSH, STI, STL, STN, STR, STT, STV, STW, STX, SUB, SUF, SUI, SUJ, SUV, SVD, SVG, SVL, SVO, SVQ, SVX, SWA, SWF, SXB, SXM, SXR, SYD, SYR, SYX, SYZ, SZB, SZF, SZG, SZX, SZY, SZZ, TAB, TAE, TAG, TAM, TAO, TAS, TAT, TAY, TAZ, TBJ, TBS, TBU, TBZ, TCO, TCP, TER, TET, TFN, TFS, TFU, TGD, TGG, TGM, TGT, TGU, TGZ, THE, THR, TIA, TIF, TIJ, TIP, TIQ, TIR, TIV, TJM, TJU, TKD, TKK, TKU, TLC, TLE, TLH, TLL, TLM, TLN, TLS, TLU, TLV, TMJ, TML, TMM, TMP, TMS, TNA, TNG, TNN, TNR, TOE, TOF, TOS, TPA, TPE, TPS, TQO, TRC, TRD, TRF, TRN, TRS, TRU, TRV, TRW, TRZ, TSA, TSN, TSR, TTU, TUA, TUC, TUF, TUK, TUL, TUN, TUS, TUU, TXN, TYN, TYS, TZL, TZX, UAK, UBN, UCB, UDI, UDJ, UET, UFA, UGC, UIB, UIO, UKK, ULU, ULV, UME, UPG, UPN, URA, URC, URS, URT, USH, USM, UTH, UTP, UUD, UUS, UVF, VAA, VAM, VAR, VAV, VBS, VBY, VCA, VCE, VCL, VCP, VDO, VER, VFA, VGA, VGO, VIE, VIL, VIT, VIX, VKO, VLC, VLI, VLL, VLN, VNO, VNS, VNT, VNX, VOG, VOL, VOZ, VRA, VRN, VSA, VST, VTE, VTZ, VUP, VVC, VVI, VVO, VXE, VXO, WAW, WDH, WEH, WLG, WLS, WMI, WNZ, WRO, WSI, WUH, WUS, WUT, WUX, WVB, WXN, WZA, XBJ, XCH, XCR, XIY, XMN, XNH, XNN, XPL, XRY, XSP, XUZ, YAP, YCU, YEG, YEI, YFC, YHM, YHZ, YIA, YIH, YIW, YKF, YKS, YNB, YNJ, YNT, YNY, YNZ, YOW, YQB, YQG, YQM, YQR, YQT, YQX, YSJ, YTY, YTZ, YUL, YVR, YWG, YXU, YXX, YXY, YYC, YYJ, YYT, YYZ, ZAD, ZAG, ZAH, ZAM, ZAZ, ZBR, ZCL, ZHA, ZIA, ZIH, ZLO, ZNZ, ZQN, ZRH, ZTH, ZTU, ZUH, ZVK, ZYI, ZYL"
        all_destinations = all_destinations.split(',')
        # Let's say my airline has three competitors. 
        # Let's prompt the user for the number of destinations in my set plus each of my competitors.
        # Remember: Because these sets are generated randomly, it is possible to choose the same destination twice 
        # and because it's a set, it will be removed. 
        mine = int(input("Enter how many destinations are in my list:\n"))
        comp1 = int(input("Enter how many destinations are in Competitor #1's list:\n"))
        comp2 = int(input("Enter how many destinations are in Competitor #2's list:\n"))
        comp3 = int(input("Enter how many destinations are in Competitor #3's list:\n"))
        # If input is 0 or negative, raise error
        if mine<1 or comp1<1 or comp2<1 or comp3<1:
            raise ValueError()
        # Now lets create the sets of destinations choosing randomly from all international destinations
        # We use while loops to ensure that our list contains the correct number of destinations.
        my_destinations = set()
        while len(my_destinations) < mine:
            my_destinations.add(random.choice(all_destinations))
        competitor1 = set()
        while len(competitor1) < comp1:
            competitor1.add(random.choice(all_destinations))
        competitor2 = set()
        while len(competitor2) < comp2:
            competitor2.add(random.choice(all_destinations))
        competitor3 = set()
        while len(competitor3) < comp3:
            competitor3.add(random.choice(all_destinations))

        # Let's find out how many are unique to my set as compared to each competitor

        unique_destinations(my_destinations, competitor1, competitor2, competitor3)
        # Let's test invalid inputs.
        unique_destinations(['Not a set', ['testing']], {'This one is a set',})
        # Let's find out how many are shared with my set as compared to each competitor
        shared_destinations(my_destinations, competitor1, competitor2, competitor3)
        # Let's test invalid inputs
        shared_destinations("This is a string", ["List", "List"])
        # Let's find out how many are unique to both my set and my competitor's for each competitor
        unshared_destinations(my_destinations, competitor1, competitor2, competitor3)
        # Let's test invalid inputs
        unshared_destinations(1234, 5678)
        overall_unique(my_destinations, competitor1, competitor2, competitor3)
        
        # Here it is again on a smaller scale
        my_set = {"A", "B", "C", "D", "E", "F", "G", "H", "I"}
        set1 = {"A", "C", "J", "K"}
        set2 = {"E", "C", "L", "M", "D"}
        set3 = {"C", "F"}
        unique_destinations(my_set, set1, set2, set3)
        shared_destinations(my_set, set1, set2, set3)
        unshared_destinations(my_set, set1, set2, set3)
        overall_unique(my_set, set1, set2, set3)
    except ValueError:
        print("Please input a positive integer.")
    
if __name__ == "__main__":
    main()



