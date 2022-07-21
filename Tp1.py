import matplotlib.pyplot as plt
import scipy.fftpack as sy  
import scipy.signal as sg
import sympy as sp
import numpy as np

# Potencial de membrana [mV]
calamar_pda = [-64.4907177054792,-43.1868695968303,-71.9755563688403,-54.9805967396872,-70.0098105938952,-65.0480559669944,-67.6202139042626,-60.5208074081377,-38.1801859564565,-76.8214176738476,-55.3668288320444,-56.6555477207035,-71.3196340415498,-51.3393956312019,-59.4742817455048,-45.3447659854498,-67.8725745215527,-54.2525067521925,-44.6447328679501,-77.1676093815174,-45.2238288680508,-53.3529955874676,-53.1374372715688,-49.2225221391132,-55.7717472754119,-45.5608363077575,-75.490693209132,-42.5864256724869,-39.4568841831031,-58.960755357012,-37.0469885353179,-59.2524287992614,-53.5051747087989,-58.3843499143616,-40.1111054744188,-30.237728749473,-63.5664429524686,-35.6462916570623,-54.6338897871626,-57.7685520064238,-35.290400441857,-42.094095983494,-33.3409308072477,-58.3934972922888,-36.6865087363229,-41.8049799575285,-58.4837347741447,-22.075614313567,-43.9981579534238,-39.4178699104809,-38.8226288236359,-38.1932659171655,-33.5103167164899,-55.2607706374616,-18.6096428836045,-34.9723739787896,-39.6990831645632,-17.5212340204685,-42.0198268275261,-32.624891648911,-38.6936591581234,-15.3813805098686,-17.5760102853261,-35.5103360125072,-6.41578029619291,-38.44062749949,-27.1253375608997,-7.26357162602732,-10.399467294251,-2.74697457252804,-22.87967569105,1.27730526219536,-15.8135779575628,-10.1069357897,25.5265373557859,-1.54171601387982,11.6346815146381,8.11691421627863,15.0821901029561,18.3121351839953,13.1013073551083,47.8059178068227,17.8281695267119,29.7153156450231,45.3113681043441,24.4338719373853,39.8821249908557,32.7439024796341,53.4209539307453,39.1850183934554,38.0918631400125,59.5466600983453,20.7457363446406,42.7984958363552,49.5088727014798,46.4685545109095,50.9003816290935,35.2927552580046,51.6707303755212,22.2337380230851,42.8631795236109,63.4736075670263,33.978487413018,50.2558577858913,34.4992173792857,38.7246524299011,35.4079673337098,41.7551454602998,63.336219057261,23.9284138644077,44.6096342943684,42.5409360122936,27.090407422892,46.2778600605238,37.343939855689,50.6682469998744,27.3291092830632,40.131762119751,48.916051023945,15.5636156277084,46.6717391006235,37.7007713662821,37.0683158770934,40.1289109122211,32.7189392784395,42.0625284903345,11.2585945984161,43.2818162182824,45.5230926238496,25.1234473226377,46.1335981047906,23.0163203780001,27.8430854578709,22.0342846313681,39.3682221226402,48.2920010466783,14.0027182205156,40.9505734733019,20.9781118670405,16.845087836354,38.3103492313792,30.4780969308181,38.1857822772197,12.0694270524658,32.6927904695716,26.4691749623856,8.66190364479679,43.9160953449731,20.8119652683319,24.1805381347056,23.5312163191561,22.8801773140044,26.2435954910323,3.13086386900004,38.3729915916752,20.5501720952478,14.3074962826781,34.908253234364,8.76570530044702,16.4435656283754,8.57780403102568,30.0058140667915,25.8317331129278,5.81433990788339,32.7133142801785,-1.62887868469946,7.23787562698007,24.5105837160893,18.6362534244682,23.3930888942233,0.201376672235046,21.1324788277184,0.649057165963146,2.80171166473102,34.7313439475409,3.82872745912536,13.0684111501079,5.54917765614625,8.49501738157742,7.74217234056223,-1.35496370392527,29.6210643488362,-3.86954596905823,4.77033175501705,17.4221755442818,-6.07433625005395,7.08585807449373,-2.01909535361001,16.9902120774091,1.35422202131223,-0.907474910983753,19.5729664536821,-20.0436719447755,1.3201981601717,7.44142645886997,3.8895835328752,7.87006763426179,-8.14208091862307,7.86820016510098,-21.9069909453459,-1.59155854703836,18.7252457244458,-11.0458310098747,4.97130322138287,-11.0312596363585,-7.03846601509088,-10.5752868279715,-4.43633757537638,16.9479360358128,-22.6456351462911,-2.1394842717579,-4.37285341496281,-19.9779240408673,-0.93513482937942,-10.0040761020008,3.19462605885817,-20.2609196687594,-7.56569182916328,1.11994484277197,-32.3225776008806,-1.29618165223336,-10.3407216688835,-11.0387974788674,-8.03607334391675,-15.4963684301324,-6.19575673127043,-37.0355232925508,-5.04119019452425,-2.82205844396618,-23.2373043617055,-2.23640948198424,-25.3567971562894,-20.5271941961673,-26.3274067407244,-8.97932722214473,-0.036048345961369,-34.3006682180426,-7.32318097835117,-27.261234530731,-31.3552663611632,-9.84661946098396,-17.6312826884659,-9.87199331692721,-35.9329170515571,-15.2504810388467,-21.4115680869945,-39.1530392255045,-3.8299586982651,-26.8622933360951,-23.4191994629977,-23.9914548062743,-24.5630610925354,-21.1180223501886,-44.1471232128077,-8.81953151765812,-26.5552302199934,-32.7093043050042,-12.018640167477,-38.0701506132038,-30.3002974279293,-38.0732856078475,-16.5518963795631,-20.6321672274893,-40.5554944522069,-13.562373541381,-47.8105151009399,-38.8499806791888,-21.4839404996663,-27.2655640943278,-22.4168254253859,-45.5176168547881,-24.4967560921129,-44.8917620362602,-42.6522163827685,-10.6374001807662,-41.4567236721791,-32.1358226040096,-39.5761000259462,-36.5537521605978,-37.2327244903739,-46.2588115173988,-15.2147470407589,-48.6405228924,-39.939202276491,-27.2294967822002,-50.671917358254,-37.4615909252383,-46.5205588739945,-27.4695985125047,-43.0684519355892,-45.2977094548989,-24.7897032480438,-64.383824309187,-43.0026519367689,-36.8694975677385,-40.4149441167144,-36.4337378697458,-52.4509726197343,-36.4517081416865,-66.2439545116912,-45.9517085138484,-25.6642964080821,-55.4710255619137,-39.4958359155365,-55.5466422529928,-51.6083697927246,-55.205937387776,-49.1338746046691,-27.8225042175742,-67.4948322571699,-47.073085351669,-49.3962524697077,-65.0962122938828,-46.1530481150433,-55.3259395745147,-42.2350444381183,-65.8017261718927,-53.2203745758864,-44.6507040748801,-78.2105708555863,-47.3021252243432,-56.4643909806119,-57.279082201818,-54.3909265979156,-61.962761643205,-52.7696414564459,-83.7118012635223,-51.8136928431439,-49.6835369934441,-70.1794314479446,-49.249793041923,-72.4310070600999,-67.6508017964349,-73.4880371768112,-56.1637239651457,-47.2301491148553,-81.4896910581332,-54.4917189862029,-74.3933574519883,-78.4346270926411,-56.8565633664831,-64.5549575946802,-56.6924580923329,-82.6332467833258,-61.813867002043,-67.8214109345132,-85.3930341018717,-49.8841712796666,-72.7152261071831,-69.0558478433719,-69.397353023563,-69.7243179545195,-66.0213472884589,-88.7798431506372,-53.1695992537496,-70.6112251182048,-76.4604261408568,-55.4546970090968,-81.1815416123015,-73.0779913706081,-80.5087960308181,-58.6372539996272,-62.3598903655369,-81.9185580613126,-54.554177375292,-88.4248514867949,-79.0810022888888,-61.326128449253,-66.7136966411152,-61.4659474788738,-84.1630104699606,-62.7339120724471,-82.7163527385151,-80.0600697860727,-47.6244752581721,-78.0190870833733,-68.2696267126618,-75.2775622338248,-71.8191355426459,-72.058319709916,-80.6409199982588,-49.1496653728474,-82.1245284490931,-72.9685400254594,-59.8003672761778,-82.7804658982511,-69.1038978957545,-77.6926312577957,-58.1673626012911,-73.2877472622975,-75.0342839834355,-54.0392098666954,-93.1418186848374,-71.2645917981641,-64.6307434972849,-67.6707619415952,-63.1793027541244,-78.6813749705506,-62.1619614505075,-91.4290052641554,-70.6064483059239,-49.7835764143551,-79.0496735047563,-62.5286756848887,-78.0285163237904,-73.5341645800923,-76.5706116681685,-69.9324911131754,-48.0502645069292,-87.1471148714539,-66.1454873264989,-67.8846341200159,-82.9967451894612,-63.4622660724645,-72.0407924115655,-58.3529541439282,-81.3206450430856,-68.1388447579475,-58.9679178306789,-91.9264307625855,-60.417303382676,-68.9803862006594,-69.1982740380737,-65.7166250123813,-72.6992510233343,-62.9222176869356,-93.2868005650465,-60.8185111503072,-58.1266387534407,-78.0703468829507,-56.5991031319242,-79.2503157649229,-73.9526953396223,-79.2860305489304,-61.4721951570619,-52.0642619463139,-85.8653078066882,-58.4253043284315,-77.9018754868907,-81.5354334122389,-59.5672942606268,-66.8934185203585,-58.676513501332,-84.2807132900868,-63.1424116945167,-68.8484563967653,-86.1356714426987,-50.3590821624459,-72.9386144681771,-69.0433816835741,-69.1641163753859,-69.2847728693415,-65.3893054712628,-87.9684466880323,-52.1913097430226,-69.4778204068685,-75.1830038258357,-54.0436838181325,-79.646707792678,-71.4284692364021,-78.753101864621,-56.7833125628213,-60.415061338332,-79.8896638059872,-52.4475314899708,-86.2462876901808,-76.8359032465664,-59.0194542179856,-64.350012468121,-59.0494507477191,-81.6975566332351,-60.223039453905,-80.1633061239457,-77.467822753251,-44.9957512222308,-75.3563790553531,-65.5752157862232,-72.553534828824,-69.0673994447709,-69.280618953453,-77.8388486446331,-46.3246802412881,-79.2779608578447,-70.1016066028819,-56.9141799008264,-79.8760408261606,-66.1821641314631,-74.7544382236912,-55.2134871574353,-70.3189001263258,-72.0511155974131,-51.0423157549759,-90.1317443442379,-68.2418371589751,-61.5957669909488,-64.6239842082858,-60.1211100209861,-75.6121221289873,-59.0819748586608,-88.3385852986343,-67.5058716848773,-46.6730983121012,-75.9295294765624,-59.3990834188256,-74.889677235178,-70.3862652626924,-73.4138252150172,-66.7669783188643,-44.8761749620146,-83.9645879587994,-62.9546531284234,-64.6856142443381,-79.7896535218073,-60.247209461499,-68.8178712932709,-55.122263110423,-78.0822733610158,-64.8928768410253,-55.7144336704845,-88.6655063214199,-57.1490109518996,-65.7047947275781,-65.9154494242412,-62.4266303858412,-69.4021469871778,-59.6180625462386,-89.9756505341518,-57.5004205421772,-54.8016601526719,-74.7385313039067,-53.2605001632617,-75.9049737017576,-70.6006613043771,-75.9273506018748,-58.106914397424,-48.6924246048053,-82.486957330155,-55.0404834573371,-74.5106263262297,-78.1377974964432,-56.163312612988,-63.4831317074202,-55.2599616826755,-80.85793626391,-59.713448939348,-65.4133471096361,-82.6944545740789,-46.9117964481858,-69.4852984587275,-65.5840737706933,-65.6988548165447,-65.8135958100059,-61.9122509652238,-84.4855527159457,-48.7026142293084,-65.9833612350722,-71.6828188525979,-50.5378108858719,-76.1351847410684,-67.9113339127641,-75.230392133285,-53.2550663135576,-56.8813164939076,-76.3504583289294,
-48.9029033885594,-82.6962750237758,-73.2805441302834,-55.4587868267748,-60.7840750402983,-55.4782815879717,-78.1211941151618,-56.6415220221029,-76.5766722956811,-73.8761111197396,-41.3990004495642,-71.754627885073,-61.9685030355877,-68.9418993907734,-65.450880287608,-65.6592551202704,-74.2126792524931,-42.693744480153,-75.6422979893141,-66.4612559587001,-53.2691808812211,-76.2264328979649,-62.5279868260806,-71.0957311348983,-51.5502899390184,-66.6512524895731,-68.3790573084567,-47.3658866320083,-86.4509842545941,-64.5567860160868,-57.9064647511882,-60.9304708676894,-56.4234256118729,-71.9103067164742,-55.3760685370763,-84.6286281878295,-63.7919039264548,-42.9551600655485,-72.2076609153025,-55.6733247261716,-71.1600686002228,-66.6528468761125,-69.6766372648021,-63.0260609859691,-41.1315684159426,-80.2163323531243,-59.202788596222,-60.9301808935875,-76.0306914306762,-56.4847586736295,-65.0519718129545,-51.3529548977381,-74.3095963269026,-61.1168708423002,-51.935138504807,-84.8829617222036,-53.3632565831586,-61.9158701787299,-62.1233942048647,-58.6314839203777,-65.6039486095743,-55.8168514945596,-86.1714659451337,-53.6933014457364,-50.9916454663757,-70.9256598273739,-49.4448105725597,-72.0865045437267,-66.7794509909167,-72.1034374041918,-54.2803364402431,-44.8632198605212,-78.6551636129801,-51.2061384173694,-70.67376744351,-74.2984620749536,-52.3215377746344,-59.6389543859682,-51.413418617642,-77.0090639944285,-55.862283797996,-61.5599252162225,-78.8388118294111,-43.0539685277881,-65.6253208065293,-61.7219815926943,-61.8346830744239,-61.9473792147307,-58.0440239706021,-80.6153495121555,-44.8304687363957,-62.1093070964148,-67.8068894283489,-46.6600392463622,-72.2556036601822,-64.0299758612854,-71.347289272219,-49.3702504874156,-52.9948192239727,-72.4623108064705,-45.0131364680581,-78.8049192160873,-69.3876295957832,-51.5643433684818,-56.888132096962,-51.5808682271348,-74.222339026201,-52.7412535092311,-72.6750182709302,-69.973099095915,-37.494657533162,-67.8489807691893,-58.0615779927804,-65.0337222659089,-61.5414764906693,-61.7486496191477,-70.3008965657416,-38.7808086697225,-71.7282326532437,-62.546084223807,-49.3529253957112,-72.3091158240771,-58.6096298326527,-67.1763553899253,-47.629916102167,-62.7299007046736,-64.4567471959663,-43.4426372814324,-82.5268142168718,-60.6317132959632,-53.9805067995167,-57.0036445737411,-52.4957472955817,-67.9817921206452,-51.4467328195657,-80.6984859136928,-59.8609690600313,-39.0234459625323,-68.2751803147402,-51.7400897424608,-67.2260907150193,-62.718136930222,-65.7412054500177,-59.0899168368501,-37.1947208015628,-76.2787894687547,-55.2645579549628,-56.9912693179473,-72.0911050441049,-52.5445028919613,-61.1110513358324,-47.4113736999476,-70.36735764965,-57.1739771844371,-47.9915916139473,-80.9387625858258,-49.4184054195878,-57.970366428078,-58.1772365198642,-54.6846701571484,-61.656475818313,-51.8687159101358,-82.2226629775882,-49.743825670709,-47.0414906154089,-66.9748187781576,-45.4932753390282,-68.1342662660754,-62.8264999255163,-68.1497629133684,-50.3259269819565,-40.90806297793,-74.6992459238429,-47.2494456033701,-66.7162842394104,-70.3401722576306,-48.3624241519583,-55.6789987855374,-47.4526018753726,-73.047365942981,-51.8996832550387,-57.5963999725308,-74.8743386367892,-39.0885230867959,-61.6588777540569,-57.7545144893071,-57.8661643915532,-57.9777803216072,-54.0733151210107,-76.6434998309777,-40.8574462058886,-58.1350785423009,-63.831420505639,-42.6832944249138,-68.2775462100471,-60.050567837752,-67.3664915005938,-45.388022547522,-49.0111194343525,-68.4770962082987,-41.0263628087181,-74.8165409324479,-65.397599797138,-47.5726138191315,-52.8946531984723,-47.585589000205,-70.2252070921506,-48.7422150711234,-68.6740180942702,-65.9700804889438,-33.4895623267332,-63.8417492961745,-54.0521490670521,-61.0220331608289,-57.5274629171114,-57.7322457030056,-66.2820348249318,-34.75941999064,-67.7042462666882,-58.5194276803095,-45.3235245403351,-68.2768947705439,-54.5745109368879,-63.1382592229515,-43.58876142234,-58.6856044292258,-60.4092243718396,-39.3918010553875,-78.4725758048648,-56.5739819517027,-49.9191897822751,-52.9386471152832,-48.4269725662757,-63.909141194691,-47.3701046393014,-76.6177772529677,-55.7760744866205,-34.9342577995301,-64.1815886009585,-47.6419821917139,-63.1233526743489,-58.6106513369736,-61.6288527877308,-54.9725750899592,-33.0722654088393,-72.1510932754419,-51.1314911636145,-52.852699437842,-67.9468968392711,-48.3945183277243,-56.9551495238225,-43.2494108415686,-66.1991869779014,-52.9994489040586,-43.810552839877,-76.7510572797809,-45.2238743248664,-53.7688470024137,-53.968562866301,-50.4686729528905,-57.4329822414291,-47.6375495640747,-77.9836438134505,-45.4967699071438,-42.7862106561196,-62.7111231268602,-41.2209685118228,-63.8531487011562,-58.5363678900453,-63.8504084075141,-46.0171376399181,-36.5896219658581,-70.3709318346036,-42.9110323479397,-62.3675409348592,-65.9808631115419,-43.9923083431375,-51.2978303409166,-43.0601295429235,-68.6433330605262,-47.4838276147937,-53.1684536812041,-70.4340279711073,-34.6355683442739,-57.192993098778,-53.2754077926244,-53.373537067409,-53.4713271563642,-49.5527240975189,-72.1084519466798,-36.3076152847126,-53.570131040126,-59.2510153090555,-38.0870826430556,-63.6651709591452,-55.4216640182007,-62.7206855661842,-40.7249322665419,-44.3303536422298,-63.7782545514099,-36.3090354790561,-70.0803083927444,-60.6420324960243,-42.797271895988,-48.0990861774622,-42.7693354730894,-65.387794389415,-43.8831589208816,-63.7928222684593,-61.0662364362649,-28.5625487917395,-58.8910319239537,-49.0771799928282,-56.0222505838721,-52.5022906582299,-52.6810927449096,-61.2042948347046,-29.6544708235473,-62.5714494504195,-53.3581278788623,-40.1330489965143,-63.0565527261977,-49.3235930298203,-57.8560368594026,-38.2744861239531,-53.3385071533002,-55.0285148035926,-33.9766668709567,-73.022181903593,-51.0874696563302,-44.3956760054193,-47.3772234906604,-42.8267045429127,-58.2690670923213,-41.689234663081,-70.8950924655082,-50.0105257351881,-29.124764596272,-58.3270379537011,-41.7412273829459,-57.1752119857401,-52.6139067166641,-55.5822484575096,-48.8748160892166,-26.9220160720595,-65.9469756398416,-44.8720833032193,-46.5365337202539,-61.5724581010488,-41.9602419640451,-50.4594194879985,-36.6905575495514,-59.5754851127604,-46.3091151150929,-37.051743330654,-69.9218652792228,-38.3223274349653,-46.7929044159521,-46.9161124475164,-43.3375281735666,-50.2208789645963,-40.3421426669335,-70.6025036406979,-38.0273785454318,-35.2259580197735,-55.0573028445303,-33.4707736031036,-56.0036670315819,-50.5845773923727,-55.7931720564131,-37.8511981666112,-28.3115962985294,-61.9773052496277,-34.3981523163549,-53.7316106476604,-57.2179346666454,-35.0982755761605,-42.2684212809743,-33.8908984741877,-59.3296521692563,-38.020878201041,-43.5512169137362,-60.6572751634361,-24.6938507292597,-47.080631078961,-42.9864796430985,-42.9018670681804,-42.8104731312592,-38.6959643372413,-61.0487714944623,-25.0376915643642,-42.0823188078958,-47.5373309132941,-26.1391875786405,-51.4743547076474,-42.9788261696908,-50.0163172246707,-27.7490967485682,-31.0726664871423,-50.2278628727768,-22.4545966997157,-55.9099684213578,-46.1434034214189,-27.9574092968394,-32.9044661701081,-27.2058316492732,-49.4406548295915,-27.5369835076013,-47.0315405688961,-43.8730864738104,-10.9200570843791,-40.7809952320926,-30.4806492924966,-36.9195178624808,-32.8728792201683,-32.5037518129863,-40.4569993408881,-8.31442739757714,-40.6151097373169,-30.761210443641,-16.8705712045437,-39.1028741166024,-24.6524718221876,-32.4407013443737,-12.0877227770209,-26.3527673678919,-27.2160421507264,-5.30964674237452,-43.4729152652308,-20.6285724080603,-13.0003050898852,-15.0193303965796,-9.48131618682576,-23.9125932230119,-6.29979990801508,-34.4528899350071,-12.4981877398184]

# N tiempo discreto.
dn = 0.0001
n_max = 0.1001
n_min = 0 

n = np.arange(n_min, n_max, dn)

def u(x):
    return sp.Heaviside(x, 1)

def delta(x):
    return u(x)-u(x-1)


def ej2 ():
    ax = plt.subplot(2,1,1)
    plt.legend(loc='best')
    ax.plot(calamar_pda)
    ax.set_title("Señal Calamar")
    ax.set_xlabel("t [ms]")
    ax.set_ylabel("f(calamar) [mV]")
    ax.grid()
    ax= plt.subplot(2,1,2)
    
    t = sp.Symbol('t')
    
    for i in [1,2,3,4]:
        a = i
        f = (u(t+a)-u(t-a))/2*a
        f_1 = sp.lambdify(t,f,['numpy'])
        f_convolve= np.convolve(f_1(n),calamar_pda,mode="same")
        ax.plot(f_convolve/1000, label = str(i))
        
    ax.set_title("Señal Calamar convolucionada con f1[n]")
    ax.set_xlabel("t [ms]")
    ax.set_ylabel("f(calamar) [mV] /1000")
    ax.grid()
    plt.legend(loc='best')
    plt.show()

def ej3_1(r=0):
    ax = plt.subplot(2,1,1)
    plt.legend(loc='best')
    ax.plot(calamar_pda)
    ax.set_title("Señal Calamar")
    ax.set_xlabel("t [ms]")
    ax.set_ylabel("f(calamar) [mV]")
    ax.grid()

    ax= plt.subplot(2,1,2)
    
    t = sp.Symbol('t')
    
    for i in [400,800,900]:
        b = i
        f = 1/b * sp.sinc((t-r)/b)
        f_1 = sp.lambdify(t,f,['numpy'])
        f_convolve= np.convolve(f_1(n),calamar_pda,mode="full")
        ax.plot(f_convolve, label = str(i))
    st1 = "Señal Calamar convolucionada con f2[n]"
    if(r!=0):
        st1+= " con n=(n - "+ str(r) +")"
    
    ax.set_title(st1)
    ax.set_xlabel("t [ms]")
    ax.set_ylabel("f(calamar) [mV] /1000")
    ax.grid()
    plt.legend(loc='best')
    plt.show()


def otro():
    ax = plt.subplot(2,1,1)
    ax.plot(calamar_pda)
    ax.set_title("Señal Calamar Filtrada y no Filtrada")
    ax.set_xlabel("t [ms]")
    ax.set_ylabel("f(calamar) [mV]")
    ax.grid()
    sos = sg.butter(50, 135, 'lp', fs=1000, output='sos')
    f_convolve= sg.sosfiltfilt(sos,calamar_pda)
    #f_convolve = np.convolve(calamar_pda,f_1(n),mode="full")
    ax.plot(f_convolve,"r-")
    ax= plt.subplot(2,1,2)
    #ax.set_xlim([-10, 10])
    #ax.set_ylim([, 5]) 
    ax.plot(np.fft.fftfreq(f_convolve.size,d=dn),np.fft.fft(f_convolve))
    ax.grid()
    plt.show()

if __name__ == '__main__':
    otro()
