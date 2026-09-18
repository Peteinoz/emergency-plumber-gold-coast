from _common import *

page = dict(
    slug="plumbing-services-alberton", kind="suburb", crumb="Plumbing services Alberton",
    title="Plumbing Services Alberton | Rural Blocks | Moyle Plumbing",
    description="Plumbing services for Alberton's rural and acreage properties, minutes from Yatala: tanks, pumps, septic, sheds, hot water and gas. Call (07) 3807 7327.",
    h1="Plumbing services Alberton",
    eyebrow="Alberton QLD 4207",
    intro="<p>Plumbing services in Alberton are rural plumbing services. The locality east of the M1 between Yatala and the coast is cane land, hobby farms and acreage homes, most on rainwater tanks with pumps and on septic. Moyle Plumbing &amp; Gasfitting shares Alberton's postcode and is a few minutes away, with the price agreed before any work starts.</p>",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Plumbing services in Alberton", area="Alberton"),
    body=sec("""
<h2>Acreage plumbing services</h2>
""" + cards([
    ("pumps", "Tank pumps", "Pressure pumps, controllers, dry-run protection and replacement pumps sized for the house and the tank layout."),
    ("water-filter-installation", "Tank water filtration", "Sediment, fine filtration and UV so tank water is clean at the tap and safe to drink."),
    ("blocked-drains", "Septic and drains", "House drains to the tank, effluent pumps, trench problems and pump-out arrangements."),
    ("hot-water", "Hot water on tank pressure", "Units that suit pump-fed homes, and LPG continuous flow where there is no mains gas."),
    ("gas-fitting", "LPG gas fitting", "Cylinder installations, cooktops, heaters and the bayonet for the shed barbecue."),
    ("leak-repairs", "Leaks on long pipe runs", "Finding the split in a poly line between tank, pump, house and shed without digging up the paddock."),
]) + """
""") + soft("""
<h2>Sheds, stables and second dwellings</h2>
<p>Alberton properties often add a shed with a toilet and sink, a granny flat, stables with troughs or a wash-down bay. Each needs water from the tank or bore, drainage to the septic or a new system, and sometimes gas. We plan the runs so the pump still delivers to the house when the shed is in use, and make sure any new drainage is approved and connected properly rather than run to a soakage pit that fails in the first wet season.</p>
<h2>Wet ground and floods</h2>
<p>The low country towards the Pimpama and Albert rivers holds water. Septic trenches struggle in wet years, buried poly moves as the ground swells and shrinks, and pump pits flood. When the drains play up only after rain, the trenches or the plant are the place to look rather than the house pipes.</p>
""") + sec("""
<h2>Close to home</h2>
<p>Alberton is a short drive from our depot at Yatala, so it is easy to fit in, and a tank household with a dry tap goes to the top of the list. The """ + H("Alberton emergency plumber page") + """ explains what to check first, including the switchboard for the pump circuit. Neighbouring """ + L("plumber-ormeau", "Ormeau") + """ and Stapylton are served on the same run, and similar acreage work takes us to """ + L("plumber-mount-cotton", "Mount Cotton") + """ across the Logan River. Moyle Plumbing &amp; Gasfitting has been in family hands since 1983, with details on """ + M("the plumbing business's own site") + """.</p>
""") + sec("""
<h2>Hobby farms and horses</h2>
<p>Alberton's blocks often carry a few animals, and their water is a plumbing job too: troughs with float valves, standpipes at the paddocks, wash-down bays and the long poly runs that feed them. Float valves stick, poly cracks where a vehicle has driven over it, and a leak in a paddock line can drain a tank overnight without anyone seeing water on the ground. We install and repair all of it, fit isolation valves so a paddock line can be shut without cutting the house off, and size the pump so the house still has pressure when a trough is filling.</p>
"""),
    faqs=[
        ("We have no water and the pump is silent. What do I check?",
         "<p>The pump's power point and the breaker at the switchboard first, then the tank level. If the pump has power and the tank has water, ring us; the controller or motor has probably failed.</p>"),
        ("Can you plumb a shed toilet to our septic?",
         "<p>Usually, if the tank and trenches have capacity and the fall works. Otherwise a small separate system or a pump station is needed. We look at the layout and tell you the options.</p>"),
        ("Is rainwater safe to drink without treatment?",
         "<p>It can carry bacteria and debris from the roof. A sediment filter, fine filter and UV unit on the house supply make it reliably safe, and are a modest cost compared to the tank and pump.</p>"),
        ("Do you install LPG for cooking and hot water?",
         "<p>Yes. We are licensed gasfitters and set up exchange cylinder installations with correct regulators, pipe sizing and testing.</p>"),
    ],
    related=[
        ("pumps", "Pumps"),
        ("water-filter-installation", "Water filters"),
        ("hot-water", "Hot water"),
        ("gas-fitting", "Gas fitting"),
        ("plumber-ormeau", "Plumber Ormeau"),
        ("plumber-mount-cotton", "Plumber Mount Cotton"),
    ],
)
