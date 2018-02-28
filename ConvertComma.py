#This program deal with original CSV document with commas embedded in values, which trigger exception or cause bugs while reading in CSV file. 
#This program recognizes and converts the commas in values into '/'. And the new file is saved as 'track_sample_comma.csv'
#Form of original CSV document is:
#orderid,userid,bikeid,starttime,startpositionx,startpositiony,endtime,endpositionx,endpositiony===track
#5,36269701,85321,2017-06-23 14:24:28.0,116.31602500,39.99167600,2017-06-23 14:25:51.0,116.31581697,39.99414352
#6,21892173,87331,2017-06-19 20:36:06.0,116.34319661,39.99151340,2017-06-19 20:42:15.0,116.35146041,39.99155921===#116.343378,39.991452;1497875775457#116.343341,39.991487;1497875776720#116.343327,39.991476;1497875778114#116.343362,39.991422;1497875820127#116.343372,39.991360;1497875823148#116.343392,39.991316;1497875826151#116.343404,39.991260;1497875830149#116.343398,39.991214;1497875832146#116.343398,39.991152;1497875835304#116.343398,39.991152;1497875836066#116.343393,39.991085;1497875838143#116.343409,39.991019;1497875841144#116.343467,39.990983;1497875843146#116.343541,39.990961;1497875845155#116.343606,39.990960;1497875847142#116.343669,39.990962;1497875849151#116.343734,39.990961;1497875851142#116.343796,39.990963;1497875853173#116.343858,39.990955;1497875856153#116.343915,39.990943;1497875859155#116.343975,39.990920;1497875862155#116.344048,39.990924;1497875865153#116.344128,39.990924;1497875868158#116.344206,39.990913;1497875871162#116.344290,39.990924;1497875874158#116.344368,39.990932;1497875877149#116.344432,39.990927;1497875881155#116.344489,39.990916;1497875888145#116.344554,39.990928;1497875895145#116.344554,39.990928;1497875895791#116.344567,39.990929;1497875896135#116.344639,39.990921;1497875902156#116.344715,39.990915;1497875905154#116.344799,39.990905;1497875908144#116.344876,39.990901;1497875911157#116.344937,39.990903;1497875914169#116.345019,39.990917;1497875917162#116.345094,39.990923;1497875919159#116.345161,39.990929;1497875922166#116.345228,39.990948;1497875924161#116.345306,39.990964;1497875926158#116.345385,39.990981;1497875928161#116.345458,39.990993;1497875930161#116.345527,39.991001;1497875932158#116.345595,39.991020;1497875934164#116.345658,39.991039;1497875937154#116.345722,39.991032;1497875940160#116.345787,39.991034;1497875942166#116.345871,39.991030;1497875945157#116.345936,39.991031;1497875947153#116.346008,39.991027;1497875949156#116.346088,39.991014;1497875951153#116.346160,39.990998;1497875953157#116.346251,39.990996;1497875955187#116.346299,39.991002;1497875956381#116.346346,39.991009;1497875957150#116.346419,39.991011;1497875959148#116.346475,39.990996;1497875961144#116.346550,39.990956;1497875963149#116.346606,39.990919;1497875965148#116.346663,39.990899;1497875967160#116.346747,39.990874;1497875970154#116.346813,39.990855;1497875973152#116.346873,39.990854;1497875975169#116.346957,39.990862;1497875978158#116.347041,39.990849;1497875981154#116.347100,39.990834;1497875983154#116.347176,39.990840;1497875986157#116.347235,39.990849;1497875988155#116.347291,39.990872;1497875990156#116.347358,39.990898;1497875992157#116.347420,39.990913;1497875994162#116.347487,39.990936;1497875996148#116.347553,39.990959;1497875998148#116.347624,39.990972;1497876000152#116.347694,39.990982;1497876002154#116.347757,39.990990;1497876004145#116.347819,39.990991;1497876006147#116.347881,39.990988;1497876008149#116.347944,39.990973;1497876010168#116.348012,39.990964;1497876014155#116.348031,39.990966;1497876015965#116.348061,39.990968;1497876016158#116.348136,39.990959;1497876018134#116.348233,39.990948;1497876020150#116.348315,39.990942;1497876022148#116.348375,39.990938;1497876024151#116.348438,39.990925;1497876026149#116.348526,39.990921;1497876028155#116.348639,39.990944;1497876030165#116.348740,39.990965;1497876032174#116.348829,39.990980;1497876034154#116.348923,39.990992;1497876036151#116.349009,39.991001;1497876038155#116.349092,39.991010;1497876040172#116.349181,39.991020;1497876042166#116.349261,39.991024;1497876044146#116.349338,39.991028;1497876046158#116.349414,39.991032;1497876048147#116.349493,39.991034;1497876050165#116.349571,39.991033;1497876052158#116.349648,39.991031;1497876054155#116.349725,39.991027;1497876056146#116.349805,39.991021;1497876058152#116.349889,39.991025;1497876060153#116.349974,39.991034;1497876062146#116.350063,39.991045;1497876064147#116.350144,39.991055;1497876066159#116.350216,39.991063;1497876068159#116.350290,39.991081;1497876070160#116.350364,39.991101;1497876072157#116.350441,39.991114;1497876074157#116.350481,39.991118;1497876075986#116.350561,39.991119;1497876077152#116.350625,39.991119;1497876079156#116.350688,39.991117;1497876081196#116.350759,39.991122;1497876083146#116.350824,39.991132;1497876085156#116.350890,39.991131;1497876087160#116.350961,39.991127;1497876089145#116.351038,39.991129;1497876091156#116.351100,39.991129;1497876093160#116.351184,39.991127;1497876096167#116.351276,39.991128;1497876099145#116.351342,39.991126;1497876101146#116.351417,39.991129;1497876103168#116.351475,39.991149;1497876105157#116.351508,39.991187;1497876107157#116.351523,39.991249;1497876109167#116.351544,39.991295;1497876111158#116.351562,39.991350;1497876114150#116.351574,39.991407;1497876117162#116.351536,39.991458;1497876122155

import pandas as pd
import numpy as np

#Seperate the f=CSV file with '==='
rawdata=pd.read_csv(r'track_sample.csv',sep='===' )

for index,row in rawdata.iterrows():
    if(type(row['track'])!=type(None)):
        a=row['track'].replace(',','|')
        row.loc['track']=a


rawdata.to_csv(r'track_sample_comma.csv',index=False,sep='/')




