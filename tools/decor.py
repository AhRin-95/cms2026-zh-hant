"""Phrase-based translation for garage decoration/tool names (lines 9363-10142). Numbers/brand names are kept.
Usage: py tools/decor.py   (writes patches/010.txt, prints leftover English words for review)"""
import re
D = r'E:\SteamLibrary\steamapps\common\Car Mechanic Simulator 2026 Demo\Car Mechanic Simulator 2026 Demo_Data\StreamingAssets\Localizations\English.txt'
en = open(D, encoding='utf-8-sig').read().splitlines()
P = """Air Compressor=空氣壓縮機
Angle Grinder=手持砂輪機
Axe=斧頭
Bandsaw=帶鋸機
Large Battery=大型電瓶
Small Battery=小型電瓶
Belt Sander=帶式砂磨機
Bench Grinder=桌上型砂輪機
Bottle=瓶子
Wooden Shipping Crate=木製貨運箱
Big Group of Cardboard Boxes=大堆紙箱
Group of Cardboard Boxes=一堆紙箱
Cardboard Box=紙箱
Broom=掃把
Bucket with mop=附拖把的水桶
Bucket=水桶
Repair Table (Parts)=維修檯（零件）
Scrap salvage machine=廢料回收機
Wheel Changer=拆胎機
Wheel Balancer=輪胎平衡機
Oil Drain=廢油回收機
Battery Charger=電瓶充電器
Brake Lathe=煞車盤車床
Spring Clamp=彈簧壓縮器
Window Tint Toolkit=車窗隔熱紙工具組
Welder=電焊機
Interior Detailing Toolkot=內裝美容工具組
Engine Crane=引擎吊架
Engine Stand=引擎架
Lifter=舉升機
Old Computer=舊電腦
Computer=電腦
Phone=電話
Radio=收音機
(Warehouse)=（倉庫）
Wooden Wall Corner Cabinet=木製轉角吊櫃
Metal Wall Corner Cabinet=金屬轉角吊櫃
Wooden Wall Cabinet=木製吊櫃
Metal Wall Cabinet=金屬吊櫃
Wooden Wall Frame=木製牆面框架
Wooden Square Table=木製方桌
Metal Square Table=金屬方桌
Wooden Corner Table=木製轉角桌
Metal Corner Table=金屬轉角桌
Big Wooden Table=大型木桌
Big Metal Table=大型金屬桌
Small Wooden Table=小型木桌
Small Metal Table=小型金屬桌
Wooden Table=木桌
Metal Table=金屬桌
with cabinets=附櫃
with drawers=附抽屜
Wooden cabinets=木製櫃
Wooden Cabinet=木製櫃
Metal Cabinet=金屬櫃
Wooden Rack=木製置物架
Metal Rack=金屬置物架
Small Pegboard=小型洞洞板
Medium Pegboard=中型洞洞板
Big Pegboard=大型洞洞板
Pegboard=洞洞板
Type A=A 型
Type B=B 型
Type C=C 型
Type D=D 型
Chainsaw=鏈鋸
Charging Station=充電站
Circular Saw=圓鋸機
Clamp=夾具
Cutting Mat=切割墊
Drill Bit Set=鑽頭組
Earmuffs=耳罩
Fan=電風扇
Flashlight=手電筒
Glove=手套
Goggles=護目鏡
Hacksaw=鋼鋸
Halogen Lamp=鹵素燈
Hammer=鐵鎚
Impact Driver=衝擊起子
Jigsaw=線鋸機
Leveler=水平尺
Nail Gun=釘槍
Planner=電刨
Vacuum Cleaner=吸塵器
Power Drill=電鑽
Power Generator=發電機
Extension Cable in a roll=捲筒延長線
Extension Cable=延長線
Reciprocating Saw=軍刀鋸
Rotary Hammer=電鎚
Collapsible Table=折疊桌
Shop Stool=工作凳
Ladder=梯子
Knife=美工刀
Tape Measure=捲尺
Toolbox=工具箱
Tooth Saw=手鋸
Workbench=工作檯
Worklight=工作燈
Barrel=油桶
Gas Cylinder=瓦斯鋼瓶
Wall Lamp=壁燈
Can=罐子
Car Ramp=車用斜坡台
Group of Miscellaneous Stuff=雜物堆
Mechanics Trolley=技師工具車
Plastic Crate=塑膠箱
with bottles=附瓶子
Plastic Chair=塑膠椅
Big Screw Box=大型螺絲盒
Empty Screw Box=空螺絲盒
Screw Box=螺絲盒
Screw container=螺絲收納盒
Spray Paint=噴漆罐
Sign=招牌
Coffee Machine=咖啡機
Mop=拖把
Oil Bottle Small=小型機油瓶
Oil Bottle Big=大型機油瓶
Side mounted double Banner on frame=側掛雙面框架旗幟
Side mounted Banner on frame=側掛框架旗幟
Inclined Banner on frame=斜掛框架旗幟
Banner on frame=框架旗幟
Hanging Banner=吊掛旗幟
Picture in frame - Car detail=畫框 - 車輛細節
Picture in frame=畫框
Magazine in frame=雜誌畫框
Big Brown Leather Sofa=大型棕色皮沙發
Black Luxury Leather Sofa=黑色豪華皮沙發
Brown Luxury Leather Sofa=棕色豪華皮沙發
Red Luxury Leather Sofa=紅色豪華皮沙發
Black Luxury Leather Armchair=黑色豪華皮單人沙發
Brown Luxury Leather Armchair=棕色豪華皮單人沙發
Red Luxury Leather Armchair=紅色豪華皮單人沙發
Gray Fabric Sofa=灰色布沙發
Brown Fabric Sofa=棕色布沙發
Red Fabric Sofa=紅色布沙發
Black Leather Sofa=黑色皮沙發
Brown Leather Sofa=棕色皮沙發
Red Leather Sofa=紅色皮沙發
Gray Fabric Armchair=灰色布單人沙發
Brown Fabric Armchair=棕色布單人沙發
Red Fabric Armchair=紅色布單人沙發
Black Leather Armchair=黑色皮單人沙發
Brown Leather Armchair=棕色皮單人沙發
Red Leather Armchair=紅色皮單人沙發
Designer Garage Stool=設計師車庫凳
Repair Tool=維修工具
(Body)=（車身）
Car Lifter=舉升機
Bed Cover=床罩""".splitlines()
P = sorted((l.split('=') for l in P), key=lambda p: -len(p[0]))
out, left = [], set()
for n in range(9363, 10143):
    l = en[n - 1]
    if '=' not in l or l.startswith('!') or '|' in l:
        continue
    e = l.partition('=')[2]
    if not e:
        continue
    t = e
    for a, b in P:
        t = t.replace(a, b)
    t = re.sub(r'(?<=[\u4e00-\u9fff（）]) +(?=[\u4e00-\u9fff（）])', '', t)
    for w in re.findall(r'[A-Za-z]{3,}', re.sub(r'"[^"]*"', '', t)):
        left.add(w)
    out.append(f'{n}|{t}')
open('patches/010.txt', 'w', encoding='utf-8').write('\n'.join(out))
print(len(out), sorted(left))
