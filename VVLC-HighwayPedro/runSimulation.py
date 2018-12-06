import os

numIniFiles = [1]
#videoScenario = ["Drive-Vlc-akio-bus","Drive-Vlc-city-container","Drive-Vlc-crew-football","Drive-Vlc-foreman-hall","Drive-Vlc-highway_300-husky","Drive-Vlc-ice-news","Drive-Vlc-paris-sign","Drive-Vlc-silent-soccer","Drive-Vlc-tempete-waterfall"]

#videoScenario = ["Drive-Vlc-akio","Drive-Vlc-bus","Drive-Vlc-city","Drive-Vlc-container","Drive-Vlc-crew","Drive-Vlc-football","Drive-Vlc-foreman","Drive-Vlc-hall","Drive-Vlc-highway_300","Drive-Vlc-ice","Drive-Vlc-news","Drive-Vlc-paris","Drive-Vlc-sign","Drive-Vlc-silent","Drive-Vlc-soccer","Drive-Vlc-tempete","Drive-Vlc-waterfall"]

#videoScenario = ["Drive-Vlc-highway_300","Drive-Vlc-ice","Drive-Vlc-news","Drive-Vlc-sign","Drive-Vlc-waterfall"]
videoScenario = ["Drive-Vlc-news"]

for n in numIniFiles:
    for v in videoScenario:
        os.system("opp_run_release -m -u Cmdenv -c "+v+" -n ../veins:../../src/veins --image-path=../../images -l ../../src/veins --cmdenv-stop-batch-on-error=false omnetpp"+str(n)+".ini")
        #os.system("opp_run_release -m -c "+v+" -n ../veins:../../src/veins --image-path=../../images -l ../../src/veins --cmdenv-stop-batch-on-error=false omnetpp"+str(n)+".ini")
        pasta = v
        os.system("mkdir "+pasta)
        os.system("mv $(ls|grep rd) /home/well/veins-vlc/examples/VVLC-Video/"+pasta)
        os.system("mv $(ls|grep sd) /home/well/veins-vlc/examples/VVLC-Video/"+pasta)
        os.system("mv $(ls|grep results) /home/well/veins-vlc/examples/VVLC-Video/"+pasta)
