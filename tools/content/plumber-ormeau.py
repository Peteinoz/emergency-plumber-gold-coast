from _common import *

page = dict(
    slug="plumber-ormeau", kind="suburb", crumb="Plumber Ormeau",
    title="Plumber Ormeau | Next Door to Our Yatala Base | Moyle",
    description='Plumber for Ormeau, Ormeau Hills and Kingsholme, beside our Yatala depot. Estates and acreage, tanks, pumps, gas and hot water. Call (07) 3807 7327.',
    h1="Plumber Ormeau, Ormeau Hills and Kingsholme",
    eyebrow="Ormeau QLD 4208",
    intro="<p>If you want a plumber in Ormeau who is genuinely local, Moyle Plumbing &amp; Gasfitting is about as close as it gets: our depot at 8 Belair Drive, Yatala, shares a boundary with the suburb. We work both sides of Ormeau, the estates near the station and the acreage of Ormeau Hills and Kingsholme, with the price set before work starts.</p>",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Plumbing services in Ormeau", area="Ormeau"),
    body=sec("""
<div class="two-col">
<div>
<h2>Estate homes near the station</h2>
<p>The estates on the flat side of Ormeau were mostly built from the 1990s through the 2010s. The work here is what you would expect of homes in their first or second decade: hot water units due for replacement, flexible hoses reaching the end of their life, mixer cartridges worn by high mains pressure, and the occasional builder defect surfacing in a drain. Many are rentals, so we do a good deal of """ + L("real-estate-property-manager", "property manager work") + """ in the suburb.</p>
</div>
<div>
<h2>Acreage in the hills</h2>
<p>Ormeau Hills and Kingsholme are another world: big parcels, many drawing water from tanks through pressure pumps, many with septic or treatment plants, and long pipe runs from the road to the house. Here the calls are about """ + L("pumps", "pumps") + """ that have stopped, tanks that have run dry, filters, and drains that belong to an on-site system rather than the council sewer. See """ + L("blocked-drains-ormeau", "blocked drains Ormeau") + """ for the drains side.</p>
</div>
</div>
""") + soft("""
<h2>Jobs we do in Ormeau every week</h2>
<ul class="checks">
<li>Electric and gas hot water replacement, and conversions to heat pump where the tariff makes it worthwhile.</li>
<li>Limiting valves on estate homes whose fixtures keep dying young.</li>
<li>Gas cooktop, oven and continuous flow connections on both LPG and natural gas streets; see """ + L("gas-fitting", "gas fitting") + """.</li>
<li>Bayonet points for the barbecue on the patio; see """ + L("bbq-gas-bottle", "BBQ gas") + """.</li>
<li>Tank pump replacement and mains changeover valves for acreage.</li>
<li>Toilet repairs and replacements; see """ + L("toilets", "toilets") + """.</li>
<li>Full-house maintenance visits that clear the backlog of small jobs in one go.</li>
</ul>
""") + sec("""
<h2>Being next door</h2>
<p>Because Ormeau is adjacent to the depot, it is often where a plumber is heading first thing or finishing last thing, which makes booking easy and urgent jobs quick to reach. If a hose has burst or a drain is backing up right now, shut off first, as described on the """ + H("emergency plumber for Ormeau and the Gold Coast") + """ and then ring """ + PHONE + """. """ + L("plumber-pimpama", "Pimpama") + """ to the south and """ + L("plumber-beenleigh", "Beenleigh") + """ to the north are covered the same way, and so is rural """ + L("plumbing-services-alberton", "Alberton") + """ towards the coast.</p>
<p>Moyle Plumbing has stayed family owned and operated since 1983, with both a plumbing and a gas licence. Company background is on the """ + M("Moyle Plumbing") + """ main site.</p>
""") + sec("""
<h2>Ormeau's newer stages</h2>
<p>The latest estates on the eastern side of Ormeau are still under construction or just past handover, and the first year in a new house is the time to catch defects while the builder is responsible. Floor wastes that hold water, stormwater lines with render in them, toilets that were never sealed to the floor and heaters with no tempering valve are the usual finds. We inspect, photograph and describe each item in the terms a builder needs, then fix what the builder will not. A limiting valve installed on the same visit protects every new fixture in the house.</p>
"""),
    faqs=[
        ("Are you really based next to Ormeau?",
         "<p>Yes. Our address is 8 Belair Drive, Yatala, in the industrial area just north of the Ormeau boundary.</p>"),
        ("My tank pump at Ormeau Hills has stopped. Can you come today?",
         "<p>A tank household with no water goes to the front of the queue. Ring us and we will tell you what the day looks like; we carry common pump parts and replacement pumps.</p>"),
        ("Can you fit a pressure limiting valve at the meter?",
         "<p>Yes. A quick job that shields every hose, mixer and appliance in the house, and it is worth doing on most estate homes in Ormeau.</p>"),
        ("Do you service septic systems?",
         "<p>We handle the plumbing side: drains to the tank, pump-outs arranged where needed, effluent pumps and the pipework of treatment plants. Tank cleaning itself is done by a pump-out contractor.</p>"),
    ],
    related=[
        ("blocked-drains-ormeau", "Blocked drains Ormeau"),
        ("hot-water", "Hot water"),
        ("gas-fitting", "Gas fitting"),
        ("pumps", "Pumps"),
        ("plumber-pimpama", "Plumber Pimpama"),
        ("plumber-beenleigh", "Plumber Beenleigh"),
        ("plumbing-services-alberton", "Plumbing Alberton"),
    ],
)
