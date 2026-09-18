from _common import *

page = dict(
    slug="hot-water-system-logan", kind="suburb", crumb="Hot water system Logan",
    title="Hot Water System Logan | Repairs, Supply & Install | Moyle",
    description='Hot water system repairs, supply and installation across Logan City from Yatala: Beenleigh to Springwood and Yarrabilba. Call (07) 3807 7327.',
    h1="Hot water system service across Logan",
    eyebrow="Logan City",
    intro="<p>A hot water system in Logan could be anything from an original electric tank on a 1970s Woodridge house to a continuous flow gas unit in a Yarrabilba new-build. Moyle Plumbing &amp; Gasfitting is based at Yatala on Logan's southern edge and repairs, replaces and installs all types across the city, with the cost settled up front.</p>",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Hot water system repairs and installation in Logan", area="Logan"),
    body=sec("""
<h2>Logan's households and the units that suit them</h2>
<table>
<thead><tr><th>Where</th><th>Typical housing</th><th>Common hot water setup</th><th>Usual advice</th></tr></thead>
<tbody>
<tr><td>Beenleigh, Eagleby, Woodridge, Kingston</td><td>1960s–80s homes, many rentals</td><td>Electric storage, often old</td><td>Replace like-for-like or heat pump; check tempering valve</td></tr>
<tr><td>Loganholme, Shailer Park, Springwood</td><td>1980s–90s family homes</td><td>Electric storage on off-peak</td><td>Heat pump upgrade when the tank fails</td></tr>
<tr><td>Yarrabilba, Logan Reserve, Flagstone</td><td>New estates</td><td>Continuous flow gas or electric</td><td>Check gas line size and tempering valve; pressure limiting valve</td></tr>
<tr><td>Logan Village, Cedar Creek, acreage</td><td>Tank water, LPG</td><td>LPG storage or continuous flow</td><td>Match unit to pump flow; check cylinder capacity</td></tr>
<tr><td>Unit and townhouse complexes</td><td>Compact lots</td><td>Small electric or gas</td><td>Compact replacement; body corporate paperwork</td></tr>
</tbody>
</table>
""") + soft("""
<h2>Repairs first, replacement when it is right</h2>
<p>Across Logan, most calls about lost hot water end in a repair: an element, a thermostat, a relief or tempering valve, a thermocouple on a gas unit. We test the failed part, look the tank over for corrosion and quote a firm repair figure, with a replacement figure beside it when the unit is on its way out. When the tank itself is leaking, replacement is the only fix, and a straightforward storage swap is usually a single visit.</p>
<h2>Rentals across Logan</h2>
<p>Logan has a high proportion of investment properties, and no hot water is one of the tenant complaints a property manager must act on quickly. We contact the tenant, attend, and either repair within the approval limit or send the owner a set price for replacement with a photo of the unit and its plate. See the """ + L("real-estate-property-manager", "property manager page") + """.</p>
""") + sec("""
<h2>Installing new in Logan</h2>
<p>New installs come with the tempering valve, the limiting and non-return valves, a safe relief drain, a base off the ground and, for gas, a tested and certified connection. Heat pumps need airflow and a spot away from bedroom windows. Continuous flow gas needs a gas line sized for it and, in most cases, a power point. We check all of that before quoting so the price does not move on the day.</p>
<p>Unit types are compared in general on the """ + L("hot-water", "hot water page") + """. Springwood has its own page: """ + L("hot-water-springwood", "hot water Springwood") + """. A cylinder flooding a laundry is urgent, and the """ + H("Logan emergency plumber page") + """ page says what to switch off. Logan suburbs we attend regularly include """ + L("plumber-beenleigh", "Beenleigh") + """, """ + L("plumber-loganholme", "Loganholme") + """ and """ + L("yarrabilba-plumber", "Yarrabilba") + """. Moyle Plumbing &amp; Gasfitting is a family firm licensed for plumbing and gas, described on the """ + M("Moyle Plumbing") + """ site.</p>
"""),
    faqs=[
        ("Do you cover all of Logan City?",
         "<p>From Yatala we regularly reach Beenleigh, Eagleby, Loganholme, Shailer Park, Springwood, Underwood, Yarrabilba and Logan Village. Phone about anywhere else in the city for a plain answer.</p>"),
        ("How long is a hot water replacement?",
         "<p>Replacing a common storage unit with the same type is normally a single visit. Heat pumps, solar and moves to a new location are scheduled jobs.</p>"),
        ("Can a tenant call you directly?",
         "<p>Tenants normally go through the agency, which sends us. If the unit is flooding, switch it off at the switchboard, close its inlet tap and ring us for help isolating it while the agency is contacted.</p>"),
        ("Is a heat pump worth it in Logan?",
         "<p>On a standard electricity tariff, usually yes: the running cost is a fraction of a plain electric unit. On a cheap off-peak tariff the saving is smaller. We work it through with you before you decide.</p>"),
    ],
    related=[
        ("hot-water", "Hot water overview"),
        ("hot-water-springwood", "Hot water Springwood"),
        ("hot-water-systems-brisbane-southside", "New systems southside"),
        ("real-estate-property-manager", "Property managers"),
        ("plumber-beenleigh", "Plumber Beenleigh"),
        ("plumber-loganholme", "Plumber Loganholme"),
        ("yarrabilba-plumber", "Plumber Yarrabilba"),
    ],
)
