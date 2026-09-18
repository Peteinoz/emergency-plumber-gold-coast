from _common import *

page = dict(
    slug="commercial-plumbing", kind="service", crumb="Commercial plumbing",
    title="Commercial Plumber Gold Coast & Logan | Moyle Plumbing",
    description='Commercial plumber for shops, cafes, workshops, schools and body corporates on the northern Gold Coast and Logan. Set pricing. Call (07) 3807 7327.',
    h1="Commercial plumber for the northern Gold Coast and Logan",
    eyebrow="Commercial",
    intro="<p>A commercial plumber has to fit around trading hours, tenants and compliance paperwork, not just fix the pipe. Moyle Plumbing &amp; Gasfitting looks after shops, cafes, workshops, warehouses, schools and body corporate buildings from Yatala, with licensed plumbing and gas work, insurance in place and pricing agreed before the job starts.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Commercial plumbing", area="Gold Coast"),
    body=sec("""
<h2>Who we work for</h2>
<ul class="cards cols-2">
<li class="card"><h3>Retail and hospitality</h3><p>Cafes, takeaway shops, restaurants and retail tenancies in the centres along the M1 from Coomera to Loganholme. Grease traps, dishwashers, gas cooking lines, hand basins and the drainage that keeps a kitchen open.</p></li>
<li class="card"><h3>Industrial and trade</h3><p>Yatala and Stapylton are full of workshops, food processors and warehouses. Trade waste, compressed air drops, wash-down bays, backflow prevention and amenities blocks.</p></li>
<li class="card"><h3>Body corporates and managed buildings</h3><p>Common-area plumbing in unit complexes and townhouse estates: shared mains, hot water plants, fire hose reels, stormwater and the leak that no single owner will claim.</p></li>
<li class="card"><h3>Schools, clubs and community</h3><p>Amenities with heavy use, bubblers, hot water for canteens and kitchens, and work scheduled outside of hours where it has to be.</p></li>
</ul>
""") + soft("""
<h2>Commercial services</h2>
<ul class="checks">
<li>Planned maintenance programs with a record of what was checked and when.</li>
<li>Backflow prevention devices installed, tested annually and reported to the water authority.</li>
<li>Thermostatic mixing valves for care, education and food settings, tested and recorded.</li>
<li>Grease trap connections, trade waste plumbing and drainage capable of taking commercial flows.</li>
<li>Gas fitting for commercial kitchens and workshops, with the installation tested and certified. See """ + L("gas-fitting", "gas fitting") + """.</li>
<li>Commercial hot water: larger storage, manifolded continuous flow banks and circulating systems. See """ + L("hot-water", "hot water systems") + """.</li>
<li>Blocked drains and sewer lines with jetting and camera inspection, which matters when a blocked kitchen line means lost trade. See """ + L("blocked-drains", "blocked drains") + """.</li>
<li>Fit-outs and defit work in coordination with builders, electricians and shopfitters.</li>
</ul>
""") + sec("""
<h2>How we work on commercial sites</h2>
<ol class="steps">
<li><strong>Scope and price.</strong> For anything beyond a simple repair we inspect first and give a written set price, itemised where you need it for approval.</li>
<li><strong>Scheduling.</strong> Work is booked to suit trading hours and tenant access. Early starts and after-trade slots are arranged on request.</li>
<li><strong>Site rules.</strong> Inductions, sign-in and safe work method statements are handled as a matter of course.</li>
<li><strong>Records.</strong> Test results, compliance certificates and photos are supplied with the invoice, so your files are audit-ready.</li>
<li><strong>Clean handover.</strong> Work areas are left clean, and anything you need to watch is explained.</li>
</ol>
<h2>Compliance that commercial owners are asked for</h2>
<p>Backflow devices must be registered and tested each year. Thermostatic mixing valves in relevant settings need scheduled servicing. Gas installations need compliance certification. Rental commercial premises may also need """ + L("water-compliancy", "water efficiency evidence") + """. We keep the schedule for clients who ask us to, and property managers can read more on the """ + L("real-estate-property-manager", "property manager page") + """.</p>
<p>Commercial emergencies, such as a burst main in a centre or a blocked sewer in a food premises, follow the same urgent process as the """ + H("commercial emergency plumber page") + """ page. Our commercial reach covers """ + L("plumber-beenleigh", "Beenleigh") + """, """ + L("plumber-loganholme", "Loganholme") + """, """ + L("plumber-eight-mile-plains", "Eight Mile Plains") + """, Yatala, Ormeau, Coomera and Helensvale. This family business, family run and trading since 1983, is introduced on the """ + M("Moyle Plumbing") + """ site.</p>
""") + sec("""
<h2>Yatala and Stapylton industrial</h2>
<p>Our depot sits inside one of South East Queensland's busiest industrial precincts, and a lot of our commercial work is within a few streets of it: food manufacturers with trade waste and wash-down plumbing, transport depots with truck wash bays, workshops with compressed air and amenities, and warehouses whose only plumbing is a staff kitchen and a toilet block that cannot be out of action. Being local means a leaking hose reel or a blocked amenities drain can often be dealt with between other jobs rather than waiting for a scheduled run, and it means we already know the estate managers, the trade waste requirements and the water authority's backflow program for the area.</p>
"""),
    faqs=[
        ("Can you provide a quote for a body corporate committee to approve?",
         "<p>Yes. We inspect, then provide a written set price with the scope described clearly enough for a committee or building manager to sign off without a site visit.</p>"),
        ("Do you carry public liability insurance?",
         "<p>Yes. Certificates of currency for insurance and the QBCC licence can be supplied for your contractor records before work starts.</p>"),
        ("Can you test our backflow device?",
         "<p>Yes. We test, tag and lodge the annual report, and can replace a failed device on the spot where a suitable unit is carried.</p>"),
        ("Do you work outside business hours for shops?",
         "<p>Work that cannot be done while a shop is trading can be booked for early starts or after close. Tell us the constraints when you ring and we will fit the schedule to them.</p>"),
    ],
    related=[
        ("blocked-drains", "Blocked drains"),
        ("hot-water", "Hot water systems"),
        ("gas-fitting", "Gas fitting"),
        ("water-compliancy", "Water compliance"),
        ("real-estate-property-manager", "Property managers"),
        ("plumber-beenleigh", "Plumber Beenleigh"),
        ("plumber-loganholme", "Plumber Loganholme"),
        ("plumber-eight-mile-plains", "Plumber Eight Mile Plains"),
    ],
)
